from urllib.parse import urlparse
import requests
from requests import Session, post, get
import sys, os, asyncio
from socket import AF_INET
import random
import asyncio
import aiohttp
import time
import csv
import re
#ADMIN PINDER NIH
spech = time.ctime().split(' ')
ez = 0
connec = lambda: aiohttp.TCPConnector(family=AF_INET,
									  verify_ssl=False,)

def tolol():
	jfla = input('your list => ')
	sukses = []
	lala = open(jfla, 'r').readlines()
	for z in lala:
		abi = z.strip()
		parsed = urlparse(abi)
		jaja =  parsed.netloc
		zzz = parsed.scheme
		dor = jaja
		sukses.append(dor)
		print (dor)
		with open(jfla, "w") as f:
			for s in sukses:
				f.write(str(s + '\n'))


if __name__ == "__main__":
	tolol()