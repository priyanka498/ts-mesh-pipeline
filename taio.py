# -*- coding: utf-8 -*-
"""TAIO.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OQUnyE4D9P9fDq2R0Jw_RbnIz5o7bEsu
"""

url='https://www.contractsfinder.service.gov.uk/Search/Results'

from bs4 import BeautifulSoup
import requests

result=requests.get(url)
webpage=result.content

sl_soup=BeautifulSoup(webpage,'html.parser')
result.close()
sl_soup.contents

print(sl_soup.prettify)

print(sl_soup.head)

sl_soup.title

tender=sl_soup.find_all('div', class_='wrap-text')
print(tender)

tender=sl_soup.find_all('div', class_='search-result')
print(tender)

sl_soup.prettify

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



