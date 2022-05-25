import pyperclip
import sys

if __name__ == '__main__':
    """ Shorten Amazon URL"""
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else: 
        url = input("Enter Amazon URL to shorten: ")
    url = url.split(".com")[1]
    
    asin_id = [s for s in url.split("/") if len(s) == 10]
    if len(asin_id) != 1:
        print("Unable to find Amazon product ID from given URL\n")
        sys.exit(0)
    url = 'https://amzn.com/' + asin_id[0]
    pyperclip.copy(url)
    print(url)
    
