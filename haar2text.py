#!/usr/bin/python
#-*- coding: utf-8 -*-

from sys import argv
from xml.parsers import expat
from re import compile,sub

SEP = ":"
ENC = "UTF-8"
r = compile("---+")

def f(names,data):
  # 2011 OpenCV
  if len(names) > 1:
    if names[-1] == "size":
      print ">>>",data
  if len(names) > 3:
    if names[-1] == "_" and names[-2] == "rects" and  names[-3] == "feature":
      print ">>>",data
  if len(names) > 3:
    if names[-1] == "threshold" and names[-2] == "_" and  names[-3] == "_":
      print ">>>",data
  if len(names) > 3:
    if names[-1] == "left_val" and names[-2] == "_" and  names[-3] == "_":
      print ">>>",data
  if len(names) > 3:
    if names[-1] == "right_val" and names[-2] == "_" and  names[-3] == "_":
      print ">>>",data
  if len(names) > 3:
    if names[-1] == "stage_threshold" and names[-2] == "_" and  names[-3] == "stages":
      print ">>>",data

class CXmlParser:
  def __init__(self):
    self.names = []
    self.attrs = []
    self.data = ""

  def StartElement(self,name,atd):
    #print name,atd
    self.names.append(name) # tag name
    self.attrs.append(atd) # dictionary

  def EndElement(self,name):
    #print name
    path = SEP.join(self.names)
    print path,self.data.strip()
    f(self.names,self.data.strip())
    del self.names[-1]
    self.data = ""

  def CharacterData(self,data):
    #print data
    self.data = data

  def Parse(self,filename):
    Parser = expat.ParserCreate(ENC)
    Parser.StartElementHandler = self.StartElement
    Parser.EndElementHandler = self.EndElement
    Parser.CharacterDataHandler = self.CharacterData
    text = open(filename,"r").read()
    text = r.sub("--",text)
    ParserStatus = Parser.Parse(text,1)

filename = argv[1]
parser = CXmlParser()
element = parser.Parse(filename)
