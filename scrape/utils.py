
import requests
from bs4 import BeautifulSoup

# Given URL, create request and get HTML contents
def readURL(url):
    # page = requests.get(url)
    with open(url, 'r') as myfile:
        data = myfile.read()
    return data


# Given HTML, create and return BeautifulSoup object
def html2Soup(htmlContent):
    soup = BeautifulSoup(htmlContent, 'html.parser')
    return soup


# Given bs4.element.Tag, get and clean the text
def getTagText(tag):
    if tag:
        return tag.get_text().strip()
    else:
        return 'Empty'


# Given a non-null string which != 'Empty' convert it to int
def getInt(str):
    return str
    # return int(str) if str is not 'Empty' else 0


# Given a non-null string which != 'Empty' convert it to float
def getFloat(str):
    return str
    # return float(str) if str is not 'Empty' else 0.0
