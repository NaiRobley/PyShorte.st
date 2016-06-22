# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import requests
import json
import os
import sys

__author__ = 'Robley Adrian < +254 722 161224 >'


def main():
	usage = """
	Welcome to sh.st url shortener.

	Usage: python shst.py [URL].

	Example: python shst.py google.com

	So far you can only shorten a single URL at a time.

	Refer to the README at http:


	"""
	try:
		userUrl = sys.argv[1]
		response = requests.put("https://api.shorte.st/v1/data/url", {"urlToShorten":userUrl}, headers={"public-api-token": "fee07e5aeff511b07b1dd67e06fddffe"})
		shortened_url = json.loads(response.content)
		print('')
		print('Shortened URL: '+shortened_url['shortenedUrl'])
		print('')
		print('Status: '+shortened_url['status'])

	except IndexError:
		print (usage)

if __name__ == '__main__':
	main()