#!/usr/bin/env python3

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from urllib.request import *

'''
Credits : https://realpython.com/python-web-scraping-practical-introduction/
'''

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

def download_file(base_url, filename):
	file_url = '%s/%s' %(base_url, filename)

	print("Download %s" %(file_url))
        
	try:
		from tqdm import tqdm
	except:
		urlretrieve(file_url, filename)
		return

	# use tqdm to display the progress but too slow
	file_response = get(file_url, stream=True)
	with open(filename, 'wb') as handle:
		for data in tqdm(file_response.iter_content()):
			handle.write(data)

