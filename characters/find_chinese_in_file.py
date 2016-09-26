import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import re 
import os

def find_chinese_in_file(file):
	content = open(file, 'r').read()
	line = content.strip().decode('utf-8')
	# line = line.split('--', 1)[0]
	p2 = re.compile(ur'[^\u4e00-\u9fa5]')                
	def f(x):
		return x != ""

	zh = "\n".join(filter(f, p2.split(line))).strip()
	if zh != "":
		print file
		print zh

def scan_folder(folder):
	for r, d, f in os.walk(item):
		for x in f:
			if x.find(".lua") == -1:
				continue
			find_chinese_in_file(os.path.join(r,x))
	
if __name__ == "__main__":
	scan_list = ["D:\\mlong\\HiRun\\trunk\\src\\base", "D:\\mlong\\HiRun\\trunk\\src\\core", "D:\\mlong\\HiRun\\trunk\\src\\define",
				"D:\\mlong\\HiRun\\trunk\\src\\graph", "D:\\mlong\\HiRun\\trunk\\src\\legacyUI", "D:\\mlong\\HiRun\\trunk\\src\\ui"]
	for item in scan_list:
		scan_folder(item)

# check_file("base\\MultiLang.lua")