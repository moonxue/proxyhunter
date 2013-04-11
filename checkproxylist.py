#! /usr/bin/env python
#coding=utf-8
import ConfigParser
import requests
import re

config = ConfigParser.ConfigParser()
config.read("config.ini")
c = dict(config.items('setting'))
timeout = int(c.get("timeout", '1'))
isPrint = c.get("isprint","True").lower()
isRewrite = c.get("isrewrite","True").lower()
outfn = c.get("outfn", 'proxylist.txt')
testlist = c.get("testlist","http://www.hust.edu.cn").split('|')
afn = c.get("availablelist","availablelist.txt")

def test(ip_port):
    proxies = {
    "http":"http://"+ip_port
    }
    isDone = True
    af = open(afn,'a')
    #print proxies["http"]
    for url in testlist:
        if isPrint == "true":
            print "test",ip_port
        try:
            r = requests.get(url = url, proxies = proxies ,timeout = timeout)
            if isPrint == "true":
                print url+"\ndone..."
        except:
            if isPrint == "true":
                isDone = False
                print url+"\nabsorb..."
    if isDone:
        af.write(ip_port+'\n')
    af.close()

if isRewrite == "true":
    af = open(afn,'w')
    af.close()
f = open(outfn,'r')
while(True):
    try:
        ip_port = f.readline()[:-1]
    except:
        break
    test(ip_port)