import requests
from bs4 import BeautifulSoup
from pathlib import Path


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

def request_tester(url: str, tries: int = 5) -> str:

    try:
        response = requests.get(url=url, headers=HEADERS)
        print(f"[+] {url} {response.status_code}")
    except Exception as ex:
        if tries:
            print(f"[INFO] try={tries} => {url}")
            return request_tester(url, tries=(tries-1))
        else:
            raise
    else:
        return response


def main():
    with open('20 random urls.txt') as file:
        all_urls = file.read().splitlines()

    for url in all_urls:
        request_tester(url=url)

if __name__ == '__main__':
    main()