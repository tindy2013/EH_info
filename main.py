import requests
from bs4 import BeautifulSoup
import re
import argparse

def get_ex_info(url):
    if re.match('(.*)ex', url):
        url = re.sub('x', '-', url, 1)
        print(url)

    html_page = requests.get(url)
    if html_page.status_code == 200:

        soup = BeautifulSoup(html_page.text, "lxml")
        
        info = {}

        info["title"] = soup.find("h1", id = "gj").string
        info["favcount"] = soup.find("td", id = "favcount").string
        info["rating"] = soup.find("td", id = "rating_label").string
        info["artist"] = soup.find("a", href = re.compile('artist')).string
        
        return info
    else:
        return 'Unfound Page! Status:%s' % html_page.status_code

 
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='get URL')
    parser.add_argument('-u',type=str,default=None)
    arg = parser.parse_args()
    url = arg.u
    if url:
        print(get_ex_info(url))
    else:
        print("Need An URL!!\nUsage: -u 'https://example.com'")

