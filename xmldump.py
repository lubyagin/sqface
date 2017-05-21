#!/usr/bin/python
#-*- coding: utf-8 -*-

from sys import argv
from xml.parsers import expat
from re import compile,sub

SEP = ":"
ENC = "UTF-8"
r = compile("---+")
TagsOnly = False

class CXmlParser:
  def __init__(self):
    self.names = []
    self.data = ""

  def StartElement(self,name,attrs):
    #print name,attrs
    self.names.append(name)

  def EndElement(self,name):
    #print name
    path = SEP.join(self.names)
    if TagsOnly:
      print path
    else:
      print path,self.data.strip()
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
