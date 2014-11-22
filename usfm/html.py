from jinja2 import Environment, PackageLoader
import parsley
from ometa.runtime import ParseError, EOFError
from os import listdir
from .log import get_logger
import re

y = parsley.makeGrammar("""
w = ' '*
text = <((anything):x ?(x not in '}') -> x)*>:s '}' ws-> s
p = '\p' text
mt = '\mt' text
verse = '\\v' w <digit+>:s w text:verse ws p* -> {'num': s, 'verse': verse}
verses =  verse+
chapter = '\c' w <digit+>:s '}' ws p* verses:vs -> {'chapter':s, 'verses': vs}
chapters = chapter+
book = text{7} mt{1,4} chapters:c-> c
""",{})

html_env = Environment(loader=PackageLoader('usfm', 'html_templates'))

template = html_env.get_template('template.html')

def print_book(file):
	txt = open(file)
	lines = txt.readlines()
	out = open(file[:-5]+".html", 'w')
	temp = open('temp', 'w')
	for line in lines:
		if(len(line) >2):
			line = line.rstrip('\n')
			line = line + '}'
			temp.write(line +'\n')
	temp.close()
	text = open('temp').read()
	chapters = y(text).book()
	for line in lines:
		if len(line) == 0:
			continue
		words = line.split(" ")
		id = words[0]
		if id == "\\toc2":
			title = line[5:]
		if id == "\h":
			book_name = line[2:]
	out.write(template.render(title = title, book_name = book_name, chapters = chapters))
	out.close()

def convert_usfm_to_html(config_path):
	for file in listdir(config_path):
                if re.match(".*.usfm$", file):
                        print_book(config_path+"/"+file)
