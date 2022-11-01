from bs4 import BeautifulSoup
import csv
from urllib.request import Request, urlopen
import pandas as pd
import time 
import datetime

def MOD_CALL_PRC():
    nombre='REGISTRO-'
    ct = datetime.datetime.now().strftime("%Y-%m-%d")
    NOMBREFINAL=nombre+ct
    #obteniendo link
    site= "https://www.prensadigital.cl/resultados-kino"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site,headers=hdr)
    page = urlopen(req)
    #soup = BeautifulSoup(page)
    #print(soup)
    soup = BeautifulSoup(page)
    div=soup.find(class_="post-data-container")
    '''
    contenido=div.find_all('a',href=True)
    print(contenido['href'])
    '''
    for a in div.find_all('a', href=True):
        nueva=a['href']

    #buscando los numeros
    site2= nueva
    hdr2 = {'User-Agent': 'Mozilla/5.0'}
    req2 = Request(site2,headers=hdr2)
    page2 = urlopen(req2)
    soup2 = BeautifulSoup(page2)
    divx=soup2.find(id="resultados-kino")
    div2x=divx.find(class_="kino")
    spansx=div2x.find_all(class_="bola")


    listx=[]
    for x in spansx:
        listx.append(x.text)


    NOMBREFINAL=nombre+ct

    DIRECTORIO='F:\\ProyectoLoteSSIS\\EntradaGeneraDia\\'+nombre+ct+'.csv'
    with open(DIRECTORIO, 'w', newline='') as csvfile:
        fieldnames = ['n1', 'n2', 'n3', 'n4','n5', 'n6', 'n7', 'n8','n9', 'n10', 'n11', 'n12','n13', 'n14']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        #creamos diccionario
        diccionario={}
        encabezados=['n1', 'n2', 'n3', 'n4','n5', 'n6', 'n7', 'n8','n9', 'n10', 'n11', 'n12','n13', 'n14']
        my_list=listx
        contador=0

        for x in encabezados:
            diccionario[x]=listx[contador]
            contador=contador+1
        writer.writerow(diccionario)
