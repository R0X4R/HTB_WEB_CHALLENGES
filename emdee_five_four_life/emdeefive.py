#!/usr/bin/python
import requests
import re
import hashlib
import sys
if len(sys.argv)<2:
 print("Syntax:python %s <port>")%(sys.argv[0])
else:
 print('-'*55)
 print("HTB WEB-CHALLENGE coded by ZyperX Emdee four FOR lIFE")
 print('-'*55)
 def gexer(ops):
  ops=re.search("<h3 align='center'>.*?</h3>",ops.text)
  ops=re.search(">.*?<",ops.group())
  ops=str(ops.group())
  ops=ops.replace('<','')
  ops=ops.replace('>','')
  return ops
 def lexer(ops):
  ops=re.search("<p align='center'>.*?</p>",ops.text)
  ops=re.search(">.*?<",ops.group())
  ops=str(ops.group())
  ops=ops.replace('<','')
  ops=ops.replace('>','')
  return ops

 url="http://docker.hackthebox.eu:"
 port=sys.argv[1]
 url=url+port
 r=requests.session()
 try:
  op=r.get(url)
 except requests.exceptions.Timeout:
  print("check port number")
 
 print("[*]Sending get request")
 op=gexer(op)
 print("[*]plaintext to encrypt: %s")%(op)
 op=hashlib.md5(op).hexdigest()
 print("[*]md5 encoded data :%s")%(op)
 data={'hash':op}
 op=r.post(url,data)
 op=lexer(op)
 print("[*]FLAG - %s")%(op)
