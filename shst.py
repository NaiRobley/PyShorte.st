# -*- coding: utf-8 -*-
#!/usr/bin/env python

import requests
from requests.exceptions import ConnectionError
import json
import os
import sys

__author__ = 'Robley Adrian < robleyadrian@gmail.com >'
__version__ = '0.0.1'

usage = """
	Welcome to sh.st url shortener.

	Usage: python shst.py URL1 URL2 URL3...

	Example: python shst.py google.com twitter.com facebook.com

	More information at: http://github.com/NaiRobley/PyShorte.st

	"""

def shorten():
	userUrls = [url for url in sys.argv[1:]] # Get the URLs from the user and add them to a list
	try:
		for userUrl in userUrls:
			response = requests.put("https://api.shorte.st/v1/data/url", {"urlToShorten":userUrl}, headers={"public-api-token": "fee07e5aeff511b07b1dd67e06fddffe"})
			shortened_url = json.loads(response.content)
			print('')
			print(userUrl+' : '+shortened_url['shortenedUrl']+' -- Status: '+shortened_url['status'])
			print('')

	except IndexError:
		print (usage)

	except ConnectionError as e:
		print (' Ensure you are connected to the internet')

if __name__ == '__main__':
	print (usage)
	shorten()
