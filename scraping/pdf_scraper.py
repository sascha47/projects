#!/usr/bin/python3

import os
import requests
from bs4 import BeautifulSoup
import sys

link = str(sys.argv[1])
# https://www.bellevuecollege.edu/publications/
#https://www.bellevuecollege.edu/careers/
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

#find all links ending in .jpg
pic_links = soup.find_all('img',src=lambda x: x and ".png" in x)

for links in pic_links:
    pic_links = links.get('src')
    pic_response = requests.get(pic_links)
    pic_name = os.path.split(pic_links)[-1]
    with open(pic_name,'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)

#download the pdf files
for links in pdf_links:
    #print(link.get('href'))
    pdf_url = links.get('href')
    

    # send a GET request to the pdf URL
    pdf_response = requests.get(pdf_url)
    

    # The PDF file name will be the last part of the url
    pdf_name = os.path.split(pdf_url)[-1]
    

    # we write the content of the response to the file 
    # same name as the file
    with open(pdf_name,'wb') as file:
        #file.write(pdf_response.content)
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)

    
    
   
