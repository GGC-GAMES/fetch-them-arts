# SEARCH PARAMS
image_count = 10
search_term = "hatsune_miku+-comic"  # Search term for the images
base_url = f"https://safebooru.org/index.php?page=dapi&s=post&q=index&tags={search_term}"
# base_url = f"https://***booru.com/index.php?page=dapi&s=post&q=index&tags={search_term}" # UNCOMMENT AND CHANGE TO NEEDED ***BOORU, COMMENT THE LINE ABOVE

use_alt_download_method = False  # Set to True to use the alternative download method (***booru)
use_proxy_server = False  # Set to True to use the proxy server


# PROXY SERVER CONFIG
remote_server_ip = "127.0.0.1"  # IP address of the remote proxy server
remote_server_port = 5001  # Port number of the remote proxy server
download_path = "downloaded_images"  # Path to save downloaded images
secret_key = 'your_secret_key' # Secret key for the proxy server

# PAGINATION CONFIG (AUTOMATICALLY SET BY THE SCRIPT)
limit = 20  # Number of images per page (can be modified as needed)
max_pid = image_count // limit + 1  # Maximum page number (can be modified as needed)