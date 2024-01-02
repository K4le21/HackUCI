from googlesearch import search
from bs4 import BeautifulSoup as soup

def searchAddress(address):
    query = address
    
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        if j[ 0 : 23 ] == "https://www.zillow.com/":
            return j
    return "Addess Not Found"

if __name__ == "__main__":
    print(searchAddress("8593 Hollywood Blvd, Los Angeles, CA 90069"))