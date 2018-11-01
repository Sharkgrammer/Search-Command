import sys
from lxml import html
from lxml.html import document_fromstring
from lxml import etree
import requests
from colorama import init, Fore, Back, Style
init(convert=True)
searchLen = 1
try:
    searchLen = int(sys.argv[len(sys.argv) - 1])
except:
    searchLen = 1
count = 1
highestlen = 0

def f(x):
    return {
        '-l': '&tbm=nws&tbs=sbd:1',
        '-n': '&tbm=nws'
        #'-s': '',
    }.get(x)

def googledata(page):
    global count
    global highestlen
    doc = document_fromstring(str(page.content))
    if count == 1:
        if "503" in str(page):
            print("[91;1m " + str(page) + "[0m")
        else:
            print("[92;1m " + str(page) + "[0m")
    #newsDataGoogle = doc.xpath('//h3[@class="r"]//a/text()')
    newsDataGoogle = doc.xpath('//h3[@class="r"]//a')
    newsDateGoogle = doc.xpath('//span[@class="f"]/text()')
    maxlen = 0
    strvar = ""
    for x in range(0, len(newsDataGoogle)):
        tempStr = ""
        workingStr = str(etree.tostring(newsDataGoogle[x]))
        for y in range(1, len(workingStr.split(">"))):
            tempStr += workingStr.split(">")[y].replace("<b", "").replace("</b", "").replace("</a", "").replace("\\", "").replace("...", "").replace("'", "").replace(";", "").replace("&#8220","").replace("&#8221","")
        for y in range(0, len(tempStr)):
            if len(tempStr) > maxlen:
                maxlen = len(tempStr)
                if maxlen > highestlen:
                    highestlen = maxlen
                else:
                    maxlen = highestlen
    
    for x in range(0, len(newsDataGoogle)):
        tempStr = ""
        workingStr = str(etree.tostring(newsDataGoogle[x]))
        for y in range(1, len(workingStr.split(">"))):
            tempStr += workingStr.split(">")[y].replace("<b", "").replace("</b", "").replace("</a", "").replace("\\", "").replace("...", "").replace("'", "").replace(";", "").replace("&#8220","").replace("&#8221","")
        strvar = ""
        for z in range(0, maxlen - len(tempStr)):
                strvar += " "
        countstr = ""
        
        if ((searchLen * 10) < 100):
            if len(str(count)) == 1: countstr = " " + str(count)
            else: countstr = str(count)
        else:
            if len(str(count)) == 1: countstr = "  " + str(count)
            elif len(str(count)) == 2: countstr = " " + str(count)
            else: countstr = str(count)
        
        print("[92;1m" + countstr + "[0m " + tempStr + strvar + " [91m" +  newsDataGoogle[x].get("href").split("&sa=")[0].replace("/url?q=","") + "[0m")
        count += 1
        
flag = ""
strname = ""
switch = 0
if searchLen != 1:
    switch = 1
    
if (len(sys.argv) - 1) != 1:
    for x in range(1, len(sys.argv) - switch):
        if str(f(sys.argv[x])) != "None":
            flag = str(f(sys.argv[x]))
        else:
            strname += sys.argv[x].replace(" ", "+")
    strname = strname.replace("1", "")
else:
    strname = sys.argv[1].replace(" ", "+")

googledata(requests.get('https://www.google.ie/search?q=' + strname + flag))
for x in range(1, searchLen):
    googledata(requests.get('https://www.google.ie/search?q=' + strname + flag + '&start=' + str(x * 10)))