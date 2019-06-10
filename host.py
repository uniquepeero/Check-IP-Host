import requests
import os
from time import sleep

apiurl = "http://api.whois.vu/?q="
ips = []

#list of IPs
with open('data.txt') as f:
	for line in f.readlines():
		if len(line) > 0:
			fline = line[:-1]
			ips.append(fline)

for ip in ips:
	try:
		while True:
			res = requests.get(f'{apiurl}{ip}')
			if res.status_code == requests.codes.ok:
				res = res.json()
				if 'google' in res['hostname']:
					with open('hosts.txt', 'a') as f:
						f.write(f"{res['hostname']}\n")
				break
			else:
				print(f'{ip} Code: {res.status_code}, res: {res}')
				sleep(2)
	except Exception as e:
		print(f'{ip} ERROR {e}')
		continue