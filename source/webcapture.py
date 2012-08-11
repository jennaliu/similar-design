#!/usr/bin/python
import csv
import subprocess, threading
from Queue import Queue
import cProfile
import time
import os
import signal

# Globals
finished_url_entry_count = 0

# Thread for convert a url to an image
class WebCapture(threading.Thread):
    def __init__(self, thread_name, url, filename, output_folder):
        self.url = url
        self.filename = filename
        self.output_folder = output_folder
        self.process = None
        self.start_time = 0
        self.thread_name = thread_name
        threading.Thread.__init__(self)
    def run(self):
        cmd = './webcapture ' + self.url + " " + self.output_folder + self.filename
        print cmd
        self.process = subprocess.Popen(cmd, shell=True)
        self.process.communicate()

def get_urls(start, url_entries_file):
    url_entry_queue = Queue()
    i = 1
    url_entries_reader = csv.reader(open(url_entries_file, 'rb'), delimiter=',', quotechar='|')
    for row in url_entries_reader:
        if i >= start:
            url_entry_queue.put({"url": row[1], "filename": row[0] + ".png"})
        i += 1
    return url_entry_queue

def feed(threads, url_entry_queue, total_url_entry_count):
    global finished_url_entry_count
    while finished_url_entry_count < total_url_entry_count:
        for i in range(8):
            if threads[i].isAlive() and time.time()-threads[i].start_time > 30:
                    try:
                        if(threads[i].process):
                            threads[i].process.terminate()
                        else:
                            print "Process is none"
                    except OSError:
                        print "Fail to stop process " + str(threads[i].process.pid)
            if not threads[i].isAlive():
                #print str(threads[i].process) + "finished"
                url_entry = url_entry_queue.get()
                threads[i] = WebCapture(threads[i].thread_name, url_entry["url"], url_entry["filename"], output_folder)
                threads[i].start()
                threads[i].start_time = time.time()
                finished_url_entry_count += 1

url_entry_queue = get_urls(17680, "../data/top-1m.csv")
total_url_entry_count = url_entry_queue.qsize()
output_folder = "../images/"
threads = []

# Initialize threads
for i in range(8):
    url_entry = url_entry_queue.get()
    thread = WebCapture("Thread-" + str(i), url_entry["url"], url_entry["filename"], output_folder)
    thread.start()
    thread.start_time = time.time()
    threads.append(thread)
                
feed_thread = threading.Thread(target=feed, args=(threads, url_entry_queue, total_url_entry_count))
feed_thread.start()
feed_thread.join()