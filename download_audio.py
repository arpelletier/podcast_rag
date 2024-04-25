'''
This script downloads a list of .mp3 files from url RSS feed.
'''

import os
import sys 
import requests
from tqdm import tqdm
import re
#import xml.etree.ElementTree as ET


def format_title(title):
    ''' Need to format title for a file format '''

    # Remove "<![CDATA[" and "]]>" if present
    cleaned_title = re.sub(r'<\!\[CDATA\[(.*?)\]\]>', r'\1', title)
    
    # Remove invalid characters
    cleaned_title = re.sub(r'[^\w\s.-]', '', cleaned_title)
    
    # Trim whitespace and replace spaces with underscores
    cleaned_title = cleaned_title.strip().replace(' ', '_')
    
    return cleaned_title + '.mp3'


def read_rss(url):
    r = requests.get(url)

    # Parse using element tree
    # root = ET.fromstring(r.content)
    # Too complicated, opt to use regex for proof of concept

    # Pair output file name and link in a list
    matches = extract_title_link_pairs(r.content.decode("utf-8"))
    files_to_download = []
    for title, link in matches:
        files_to_download+=[(format_title(title),link)]
    return files_to_download[::-1] # oldest first


def extract_title_link_pairs(html_content):
    pattern = r"<title>(.*?)<\/title>.*?<enclosure url=\"(.*?)\" length"
    matches = re.findall(pattern, html_content, re.DOTALL)
    return matches


def get_file(url, file_name):
    r = requests.get(url)
    open(file_name, 'wb').write(r.content)


def download_audio(url, output_folder):

    # Parse input file
    files_to_download = read_rss(url)
    print(f"{len(files_to_download)} files to download.")

    # Make a new directory if does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Download all files
    count = 0
    pbar = tqdm(total=len(files_to_download), desc="Downloading files", unit="files")
    for output_name, url_path in files_to_download: 
        output_path = os.path.join(output_folder, output_name)
        get_file(url_path, output_path)
        count += 1
        pbar.update(1)
    pbar.close()
    print(f"Downloaded {count} files to {output_folder}")


### Parse arguments ###
if len(sys.argv) < 3:
    print("Incorrect usage.")
    print("python download_audio.py <rss_feed_url> <output_folder>")
    print("Example: python download_audio.py <rss_feed_url> ./audio")
    sys.exit(0)

# get file names
input_file = sys.argv[1]
output_folder = sys.argv[2]

download_audio(input_file, output_folder)
