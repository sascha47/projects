#!/usr/bin/python3

import os
import requests
from bs4 import BeautifulSoup
import sys

link = str(sys.argv[1])

# get the HTML content
response = requests.get(link)

# parse the content and create beautiful soup object
soup = BeautifulSoup(response.content, "html.parser")

#Print the parsed content

a_tags = soup.find_all('a')

# for link in a_tags:
#     print(link.get('href'))

# final all links ending in .pdf
pdf_links = soup.find_all('a', href=lambda x: x and '.pdf' in x)

#download the pdf files
for links in pdf_links:
    #print(link.get('href'))
    pdf_url = links.get('href')

    # send a GET request to the pdf URL
    pdf_response = requests.get(pdf_url)

    # The PDF file name will be the last part of the url
    pdf_name = os.path.split(pdf_url)[-1]

    # we write the content of the response to the file
    with open(pdf_name,'wb') as file:
        file.write(pdf_response.content)
    
    print(f"Downloaded {pdf_name}!")
