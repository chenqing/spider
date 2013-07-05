#!/usr/bin/pythom
from dytt8.dytt8 import dytt8

t = dytt8(4)
print t.list_url()
for url in t.http_url():
	print url
