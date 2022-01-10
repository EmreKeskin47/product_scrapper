import json
from bs4 import BeautifulSoup
from selenium import webdriver
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

def AmazonProductScrapper(URL):
    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()
    price = soup2.find("span",{'class':'a-offscreen'}).get_text()
    image = soup2.find("img",{'id':'landingImage'})['src']
    about = soup2.find("ul",{'class':"a-unordered-list a-vertical a-spacing-mini"}).get_text()
    delivery = soup2.find(id = "mir-layout-DELIVERY_BLOCK-slot-DELIVERY_MESSAGE").get_text()    
    product_json = json.dumps({"title":title.strip(), "price":price.strip(), "image":image.strip(), "about":about.strip(), "delivery":delivery.strip(), "URL":URL})
    return product_json

