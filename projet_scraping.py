# -*- coding: utf-8 -*-
"""
@author : ndohvich
"""

#Importation des librairies 

from bs4 import BeautifulSoup 
import requests 
import csv
import os 
import urllib.request

#Stockage des liens et des genres 

liste_liens = []
liste_genres = []

lien  = "http://books.toscrape.com/"
response = requests.get(lien)
soup = BeautifulSoup(response.text,'html.parser')
soup = soup.find(class_="nav nav-list")