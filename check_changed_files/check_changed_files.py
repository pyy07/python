#!/usr/bin/env python 
# -*- coding: utf-8 -*-

'file change'
import os, time, threading

fileList = {}
scan_paths = ["d:\\mlong\\nxx_ui\\", "d:\\temp\\"]

def create_file_list(base_path, level):
	ret = {}
	for f in os.listdir(base_path):
		path = os.path.join(base_path, f)
		if os.path.isdir(path):
			if level < 10:
				files = create_file_list(os.path.join(base_path,f), level + 1)
				ret.update(files)
			else:
				print("stop scan path " + path)
		else:
			if os.path.exists(path):
				mTime = os.path.getmtime(path) 
				ret[path] = mTime

	return ret


def run_scan(path):
	newList = create_file_list(path, 1)
	content = ""
	for k, v in newList.items():
		if fileList[path].get(k) == None:
			content = content + "\nfile " + k + " is created at " + time.ctime(v)
			fileList[path][k] = v
		else:
			if fileList[path].get(k) == v:
				pass
			else:
				content = content + "\nfile " + k + " is modified at " + time.ctime(v)
				fileList[path][k] = v

	with open("log.txt", "a") as file:
		file.write(content)

def run_scan_modify_only(path):
	content = ""
	for k, v in fileList[path].items():
		newMTime = os.path.getmtime(k)
		if newMTime == v:
			pass	
		else:
			content = content + "\nfile " + k + " is modified at " + time.ctime(v)
			fileList[path][k] = newMTime

	with open("log.txt", "a") as file:
		file.write(content)
					

def print_mem_usage():
	import os
	import psutil
	process = psutil.Process(os.getpid())
	print process.memory_info()

def main():
	for p in scan_paths:
		fileList[p] = create_file_list(p, 1)

	while True:
		# print_mem_usage()
		threadList = []
		for p in scan_paths:
			t = threading.Thread(target = run_scan_modify_only, name = "thread_" + p, args=(p,))
			t.start()
			threadList.append(t)
		
		for th in threadList:
			th.join()

		time.sleep(10)

if __name__ == '__main__':
	main()



