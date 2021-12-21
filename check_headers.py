from colorama import Fore
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

sourcefile = r'C:\Users\rakeshkirola\PycharmProjects\Scripts\urls.txt'

expected_headers = ['Connection', 'Content-Encoding', 'TE', 'Transfer-Encoding', 'Cache-Control', 'Content-Language']

with open(sourcefile, 'r') as file:
    for raw_url in file:
        url = raw_url.strip()
        try:
            response = requests.head(url, allow_redirects=True)
            print(response.headers)
            for header in expected_headers:
                if header not in response.headers:
                    print(url, Fore.RED + header, "Header is not there in response")
                else:
                    print(url, Fore.GREEN + header, "Header exists in response")
        except requests.exceptions.ConnectionError as connerror:
            print(url, "Connection error", connerror)
        except requests.exceptions.Timeout as timeout:
            print(url, "Timeout encountered", timeout)
        except requests.exceptions.HTTPError as httperror:
            print(url, "Http error", httperror)
        except requests.exceptions.RequestException as reqexception:
            print(url, "Connection error", reqexception)
