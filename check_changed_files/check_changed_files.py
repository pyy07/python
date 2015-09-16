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
					

def main():
	for p in scan_paths:
		fileList[p] = create_file_list(p, 1)

	while True:
		threadList = []
		for p in scan_paths:
			t = threading.Thread(target = run_scan, name = "thread_" + p, args=(p,))
			t.start()
			threadList.append(t)
		
		for th in threadList:
			th.join()

		time.sleep(10)

if __name__ == '__main__':
	main()



