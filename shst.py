# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import requests
import json
import os
import sys

__author__ = 'Robley Adrian < +254 722 161224 >'

usage = """
	Welcome to sh.st url shortener.

	Usage: python shst.py URL1 URL2 URL3...

	Example: python shst.py google.com twitter.com facebook.com

	More information at: http://github.com/NaiRobley/PyShorte.st


	"""

def main():
	userUrls = [url for url in sys.argv[1:]]
	if userUrls > 0:
		# userUrls = [url for url in sys.argv[1:]]
		for userUrl in userUrls:
			response = requests.put("https://api.shorte.st/v1/data/url", {"urlToShorten":userUrl}, headers={"public-api-token": "fee07e5aeff511b07b1dd67e06fddffe"})
			shortened_url = json.loads(response.content)
			print('')
			print(userUrl+' : '+shortened_url['shortenedUrl']+' -- Status: '+shortened_url['status'])
			print('')

	elif userUrls == 0:
		print (usage)

if __name__ == '__main__':
	print (usage)
	main()