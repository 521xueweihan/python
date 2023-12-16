import requests

def check_url(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=10)
        if response.status_code == 200:
            print(f"URL {url} is valid and accessible.")
            print(f"Content Type: {response.headers.get('Content-Type')}")
            print(f"Content Length: {response.headers.get('Content-Length')} bytes")
            print(f"Last Modified: {response.headers.get('Last-Modified')}")
        else:
            print(f"URL {url} returned status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error: {e}")
        return False

# Example usage:
url_to_check = "https://example.com/book-download"
check_url(url_to_check)
