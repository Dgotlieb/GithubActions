import os
import requests

def main():
    url = os.getenv('TARGET_URL', 'https://www.google.com')  # Default to Google if no URL is provided
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    print(f"Response URL: {response.url}")

if __name__ == "__main__":
    main()
