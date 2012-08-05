#!/usr/bin/python
import csv
import subprocess, threading

class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self, timeout):
        def target():
            print 'Thread started'
            self.process = subprocess.Popen(self.cmd, shell=True)
            self.process.communicate()
            print 'Thread finished'

        thread = threading.Thread(target=target)
        thread.start()

        thread.join(timeout)
        if thread.is_alive():
            print 'Terminating process'
            self.process.terminate()
            thread.join()
        print self.process.returncode


def capture(url, filename):
	command = Command('./webcapture ' + url + ' ../images/' + filename)
	command.run(timeout=30)

start = 1915
linkReader = csv.reader(open('../data/top-1m.csv', 'rb'), delimiter=',', quotechar='|')
i = 1
for row in linkReader:
	if i >= start:
		print 'capturing ' + row[1] + '...'
		capture(row[1], row[0] + '.png')
	i += 1



