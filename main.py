import requests
import xml.etree.ElementTree as ET
import os
from config import base_url, limit, max_pid, remote_server_ip, remote_server_port, secret_key


# Configure variables for URL parameters

# Create a directory to store downloaded images
output_dir = "downloaded_images"
os.makedirs(output_dir, exist_ok=True)

proxy_server_url = f"http://{remote_server_ip}:{remote_server_port}/download_image"


def get_image_via_proxy(image_url, save_path):
    # Remote proxy server URL (replace with your server's IP)
    params = {'url': image_url, 'password': secret_key}

    try:
        # Make a GET request to the proxy server with the image URL as a parameter
        response = requests.get(proxy_server_url, params=params, stream=True)
        response.raise_for_status()

        # Save the image content to a local file
        image_name = image_url.split('/')[-1]
        with open(os.path.join(output_dir, image_name), 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Downloaded image via proxy: {image_name}")
        return image_name  # Return the saved image filename

    except requests.RequestException as e:
        print(f"Failed to download image via proxy: {e}")
        return None

# def download_image(url, save_path):
#     """Download an image from a URL and save it to a local file path."""
#     try:
#         urllib.request.urlretrieve(url, save_path)
#         print(f"Downloaded: {url}")
#     except Exception as e:
#         print(f"Failed to download {url}: {e}")


def fetch_images(limit, max_pid):
    """Fetch images from multiple pages using the provided limit and max_pid."""
    for pid in range(max_pid):
        # Build the paginated URL
        url = f"{base_url}&limit={limit}&pid={pid}"
        print(f"Fetching page {pid} with limit {limit}")

        params = {'url': url, 'password': secret_key}

        # Retrieve XML data from the URL
        response = requests.get(proxy_server_url, params=params)
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
                get_image_via_proxy(file_url, save_path)


# Run the script to fetch and download images
fetch_images(limit, max_pid)
