from colorama import Fore
import requests

sourcefile = r'C:\Users\rakeshkirola\PycharmProjects\Scripts\urls.txt'

with open(sourcefile, 'r') as file:
    for raw_url in file:
        url = raw_url.strip()
        if url.startswith("https://") is False:
            url = "https://"+url
        try:
            response = requests.options(url)
            if "Allow" in response.headers:
                if "TRACE" in response.headers['Allow']:
                    print(url, Fore.RED + "TRACE is enabled")
                else:
                    print(url, Fore.GREEN + "TRACE is not enabled")
            elif "Access-Control-Allow-Methods" in response.headers:
                if "TRACE" in response.headers['Access-Control-Allow-Methods']:
                    print(url, Fore.RED + "TRACE is enabled")
                else:
                    print(url, Fore.GREEN + "TRACE is not enabled")
            else:
                print(url, Fore.GREEN + "No header with name Allow or Access-Control-Allow-Methods")
        except requests.exceptions.ConnectionError as connerror:
            print(url, "Connection error", connerror)
        except requests.exceptions.Timeout as timeout:
            print(url, "Timeout encountered", timeout)
        except requests.exceptions.HTTPError as httperror:
            print(url, "Http error", httperror)
        except requests.exceptions.RequestException as reqexception:
            print(url, "Connection error", reqexception)
