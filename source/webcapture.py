#!/usr/bin/python
import csv
import subprocess, threading
from Queue import Queue
import cProfile

class WebCapture(threading.Thread):
    def __init__(self, url, filename, output_folder):
        self.url = url
        self.filename = filename
        self.output_folder = output_folder
        self.process = None
        threading.Thread.__init__(self)
    def run(self):
        cmd = './webcapture ' + self.url + " " + self.output_folder + self.filename
        print cmd
        self.process = subprocess.Popen(cmd, shell=True)
        self.process.communicate()

def urls_to_images(url_entries, output_folder):
    def producer(q, url_entries, output_folder):
        for url_entry in url_entries:
            thread = WebCapture(url_entry["url"], url_entry["filename"], output_folder)
            thread.start()
            q.put(thread, True)
    finished = []
    def consumer(q, url_entries, url_entries_len):
        while len(finished) < url_entries_len:
            thread = q.get(True)
            thread.join(30)
            if thread.is_alive():
                print 'Terminating process'
                thread.process.terminate()
                thread.join()
            finished.append(thread.url)
    q = Queue(20)
    prod_thread = threading.Thread(target=producer, args=(q, url_entries, output_folder))
    cons_thread = threading.Thread(target=consumer, args=(q, url_entries, len(url_entries)))
    prod_thread.start()
    cons_thread.start()
    prod_thread.join()
    cons_thread.join()

def get_urls(start, url_entries_file):
    url_entries = []
    i = 1
    url_entries_reader = csv.reader(open(url_entries_file, 'rb'), delimiter=',', quotechar='|')
    for row in url_entries_reader:
        if i >= start and i <= 2020:
            url_entries.append({"url": row[1], "filename": row[0] + ".png"})
        i += 1
    return url_entries

url_entries = get_urls(2000, "../data/top-1m.csv")
cProfile.run('urls_to_images(url_entries, "../images/")') #keep "/" at the end of the folder path
