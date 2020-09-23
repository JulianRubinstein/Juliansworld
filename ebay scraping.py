import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import timeit
import math

pd.set_option('display.max_rows', 300)
pd.set_option('display.max_columns', 300)

def time_cal(s):
    b=[0]*4
    a=s.split()
    for item in a:
        if "d" in item:
            b[0]=int(item.replace("d",""))*24*60
        if "h" in item:
            b[1]=int(item.replace("h",""))*60
        if "m" in item:
            b[2]=int(item.replace("m",""))
        if "s" in item:
            b[3]=int(item.replace("s",""))/60
    minute=b[0]+b[1]+b[2]+b[3]
    return minute


start = timeit.default_timer()
pages=5

r=[0]*pages

for i in range (1,pages+1):
    r[i-1]=(requests.get("https://il.ebay.com/b/Wristwatches/31387/bn_2408451?LH_Auction=1&rt=nc&_pgn="+str(i))).content

b=r[0]

for i in range(1,pages):
    b=b+r[i]

s=bs(b,"html.parser")

stop = timeit.default_timer()
print('Time: ', stop - start) 

k=s.find_all("li",{"class":"s-item "})

a=[]

#run from this part when not changing page num

item_name=[0]*48*pages
item_price=[0]*48*pages
time_left=[0]*48*pages
time_left_min=[0]*48*pages  

for i in range (48*pages):
    item_name[i]=((k[i].find("a",{"class":"s-item__link"}).text).replace("New Listing","")).lower()
    item_price[i]=(k[i].find("span",{"class":"s-item__price"}).text)
    try:
        time_left[i]=(k[i].find("span",{"class":"s-item__time-left"}).text)
        time_left_min[i]=time_cal((k[i].find("span",{"class":"s-item__time-left"}).text))
    except:
        time_left[i]="unavailable"
        time_left_min[i]="unavailable"
    a.append([math.ceil(i/48),item_name[i],item_price[i],time_left[i],time_left_min[i]])
        
    
df=pd.DataFrame(a,columns=['page','item_name','item_price','time left','time left in min']).sort_values(by=['time left in min'])

print(df)


