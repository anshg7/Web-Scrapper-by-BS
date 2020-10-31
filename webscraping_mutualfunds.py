from bs4 import BeautifulSoup
import requests
import csv
import os
import datetime
import time

t1=time.time()
while(1):
    try:
        dt=input('enter the date in dd/mm/yyyy format ')
        date,month,year=dt.split('/')
        break
    except ValueError:
        print('please enter the date in given format')

csv_scrap=open('mutualfunds1.csv','w',encoding='utf-8')
csv_writer=csv.writer(csv_scrap)

source=requests.get(f'http://portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx?frmdt={month}-{date}-{year}').text 

soup=BeautifulSoup(source,'lxml')


data=soup.p.text

# print(data.split('\r\n\r\n')[4].split(';')[0].split('\r\n'))
# print(data.split('\r\n\r\n')[5].split(';'))

for i in data.split('\r\n\r\n'): 
    row=list()
    ele=list()
    row=i.split(';')
    if ('\r\n' in row[0]):
        check=0
        ele=row[0].split('\r\n')
        row[0]=ele[-1]
        if(ele[check]==''):
            new_ls=list()
            new_ls.append(ele[check+1])
            csv_writer.writerow(new_ls)
        elif(ele[check]!=''):
            new_ls=list()
            new_ls.append(ele[check])
            csv_writer.writerow(new_ls)

    if len(row)>8:
        n=len(row)//8
        for i in range(n+1):
            j=0
            csv_writer.writerow(row[j:j+8])
            
            j=j+8
    else:
            csv_writer.writerow(row)

csv_scrap.close()
t2=time.time()
print(t2-t1)