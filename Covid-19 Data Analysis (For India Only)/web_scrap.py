import pandas as pd
import bs4
from bs4 import BeautifulSoup as soup                   # parse text
from urllib.request import urlopen as uReq              # Web Client to grab something from interet
my_url = 'https://www.mohfw.gov.in/'
#Opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
#html parsing
page_soup = soup(page_html,"html.parser")
#grabs each product
containers = page_soup.findAll("div",{"class":"data-table table-responsive"}) #inside curly brace are the objects

from html_table_extractor.extractor import Extractor
table_doc = containers[0]
extractor = Extractor(table_doc).parse()
extractor.write_to_csv(path='.')

dataset = pd.read_csv('output.csv')
dataset = dataset[0:33]
dataset.to_csv('clean_output.csv')