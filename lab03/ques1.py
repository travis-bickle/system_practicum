from multiprocessing import Process
import os
import webbrowser
import time

file_name  = "abcd.txt"
sleep_duration = 3
site = "http://goo.gl/3v6wUh"

def info(title):
	print(title)
	# print('module name:', __name__)
	# if hasattr(os, 'getppid'):  # only available on Unix
	# 	print('parent process:', os.getppid())
	# print('process id:', os.getpid() )

def file_edit(name):
	info('file_edit: Start')
	with open(file_name, "ab+") as f:
		for line in f:
			line = line.replace(" ","\t")
	info('file_edit: End')

def sleep_fn(duration):
	info('Sleep Fn: Start')
	time.sleep(duration)
	info('Sleep Fn: End')

def open_browser(site):
	info('Open Chrome: Start')
	webbrowser.open(site)
	info('Open Chrome: End')

def fork_bomb():
	for x in range(1000000):
		os.fork()
	info('Fork Bomb: Start')
	for x in range(1000):
		pass
	info('Fork Bomb: End')

def fork_bomb2():
	info("Dummy Fork!")

if __name__ == '__main__':
	info('main line')
	p1 = Process(target=file_edit, args=(file_name,))
	p2 = Process(target=sleep_fn,args=(sleep_duration,))
	hog1 = Process(target=open_browser,args=(site,))
	hog2 = Process(target=fork_bomb)
	
	p2.start()
	hog1.start()
	p1.start()
	hog2.start()

	p1.join()
	p2.join()
	hog1.join()
	hog2.join()
