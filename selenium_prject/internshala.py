import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd


class requiresData:
    url = 'https://opentender.eu/all/download'
    #https: // opentender.eu / all / download
    r = requests.get(url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent,'html.parser')
    value = soup.find_all(attrs={'class': 'container-outer downloads'})
    downloadRow = soup.find_all(attrs={'class': 'download-row'})
    # title =soup.title       # get the title of html page
    #print(downloadRow)
    #print(value)
print(requiresData.downloadRow)
