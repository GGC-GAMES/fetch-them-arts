import requests
import xml.etree.ElementTree as ET
import os
import urllib.request
from config import base_url, limit, max_pid


# Configure variables for URL parameters

# Create a directory to store downloaded images
output_dir = "downloaded_images"
os.makedirs(output_dir, exist_ok=True)


def download_image(url, save_path):
    """Download an image from a URL and save it to a local file path."""
    try:
        urllib.request.urlretrieve(url, save_path)
        print(f"Downloaded: {url}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")


def fetch_images(limit, max_pid):
    """Fetch images from multiple pages using the provided limit and max_pid."""
    for pid in range(max_pid):
        # Build the paginated URL
        url = f"{base_url}&limit={limit}&pid={pid}"
        print(f"Fetching page {pid} with limit {limit}")

        # Retrieve XML data from the URL
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch page {pid}: HTTP {response.status_code}")
            continue

        # Parse the XML response
        root = ET.fromstring(response.content)

        # Loop through each <post> element
        for post in root.findall('post'):
            # Get the file_url attribute
            file_url = post.get('file_url')
            if file_url:
                # Get the image name from the URL
                image_name = file_url.split('/')[-1]
                save_path = os.path.join(output_dir, image_name)

                # Download the image
                download_image(file_url, save_path)


# Run the script to fetch and download images
fetch_images(limit, max_pid)
