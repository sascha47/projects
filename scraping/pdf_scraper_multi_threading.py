#!/usr/bin/python3

import os
import requests
from bs4 import BeautifulSoup
import sys
import concurrent.futures # multi-threading

link = str(sys.argv[1])
# https://www.bellevuecollege.edu/publications/
#https://www.bellevuecollege.edu/careers/
# get the HTML content

try:
    response = requests.get(link)
except requests.exceptions.RequestException as e:
    print(f"There was a problem: {e}")

# parse the content and create beautiful soup object
soup = BeautifulSoup(response.content, "html.parser")


# final all links ending in .pdf
pdf_links = soup.find_all('a', href=lambda x: x and '.pdf' in x)

#find all links ending in .jpg
pic_links = soup.find_all('img',src=lambda x: x and ".png" in x)

# find the href in pdf_links
url = [link.get('href') for link in pdf_links]
url += [link.get('src')for link in pic_links]

def download_file(url):
    try:
# recieve DOM elements
        file_response = requests.get(url)
# file name
        file_name = os.path.split(url)[-1]

        
        with open(file_name,'wb') as file:
            for chunk in file_response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        print(f"{file_name} Downloaded")
    except Exception as e:
        print(f"There was a problem {e}")

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_file,url)
