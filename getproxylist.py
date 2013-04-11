#! /usr/bin/env python
#coding=utf-8
import ConfigParser
import requests
import re

config = ConfigParser.ConfigParser()
config.read("config.ini")
c = dict(config.items('setting'))
isPrint = c.get("isprint", "True").lower()
baseurl = c.get("baseurl", 'http://www.cnproxy.com/proxy%d.html')
outfn = c.get("outfn", 'proxylist.txt')

def get_list():
    htmls = []
    ips = []
    for i in range(1, 11):
        url = baseurl %(i)
        if isPrint == "true":
            print url
        html = requests.get(url).content.replace(' ', '')
        html= html.replace('\r', '').replace('\n', '').replace('\t', '').replace('+', '')
        htmls.append(html)
        r = re.findall('<tr><td>([\d,\.]*?)<SCRIPTtype=text/javascript>document.write\(":"(.*?)\)', html)
        for j,k in r:
            if "r" in k or "d" in k:
                continue
            k = k.replace('x', '8').replace('f', '0').replace('m', '4').replace('w', '6')
            k = k.replace('z', '3').replace('c', '1').replace('a', '2').replace('b', '5')
            k = k.replace('l', '9')
            ips.append(j+":"+k)
            if isPrint == "true":
                print j,k
    return ips


ips = get_list()
f = open(outfn,'w')
for i in ips:
    f.write(i+'\n')
f.close()
