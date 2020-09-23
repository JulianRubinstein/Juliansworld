import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from timeit import default_timer as timer
import seaborn as sns

start = timer()

pages = 30 #dont go over 190 pages, imdb url changes format
genre = "thriller"

movies=[]

#Defining a movie class, and a method to convert data to dict
class Movie:
    def __init__(self, name, year, length, rating, metascore):
        self.name = name
        self.year = year
        self.length = length
        self.rating = rating
        self.metascore = metascore
    def to_dict(self):
        return ({ 
                "name":self.name,
                "year":self.year,
                "length":self.length,
                "rating":self.rating,
                "metascore":self.metascore
                })

#Get movie info and place them in list. Function accepts movie genre and number of pages wanted.
def get_info(genre,pages):
    global movie_list
    movie_list = []
    for i in range(pages):
        index=50*i+1
        url = f"https://www.imdb.com/search/title/?title_type=movie&genres={genre}&sort=num_votes,desc&start={index}&explore=title_type,genres&ref_=adv_nxt"
        r=requests.get(url).content
        s=bs(r,"html.parser")
        movie_list=movie_list + s.find_all("div",{"class":"lister-item mode-advanced"})

#Creates a list of movie objects which contains the movie name, year, length and rating.
def make_list():
    for i in movie_list:
        try:
            name = i.find("h3",{"class":"lister-item-header"}).find("a").get_text()
        except:
            name = None
        try:
            year = int(i.find("span", {"class":"lister-item-year text-muted unbold"}).get_text().replace('(','').replace(')',''))
        except:
            year = None
        try:
            length = int(i.find("span",{"class":"runtime"}).get_text().split(' ')[0])
        except:
            length = None
        try:
            rating = float(i.find("strong").get_text())
        except:
            rating = None
        try:
            metascore = int(i.find("div", {"class":"inline-block ratings-metascore"}).get_text().split(' ')[0])
        except:
            metascore = None
        movies.append(Movie(name,year,length,rating, metascore))
 

    
#Unident this only when you want to reload data
get_info(genre,pages)
make_list()
        
#Creating various pandas date frames from the object list, making sure there
#no duplicate values and data is clean        (sorry if tbis part is a little messy)
def create_pandas():
    global df
    global df1
    global df_years
    global df_years1
    global df_print
    global df_modern
    global df_print2
    df1 = pd.DataFrame.from_records(i.to_dict() for i in movies).set_index('name')
    df1 = df1.loc[~df1.index.duplicated(keep='first')]
    df=df1[(df1.year >= 1970) & (df1.year<=2019)]
    df_years=df.groupby('year').agg(['mean','count'])
    df_years1=df.groupby('year').mean()
    df_print = df_years1.drop(['length'],axis=1)
    df_print['metascore']=df_print['metascore']/10
    df_print2 = df_years1.drop(['metascore'],axis=1)
    df_print2['length']=df_print2['length']/17
    df_modern=df1[(df1.year >= 2010) & (df1.year<=2020)]        
        
create_pandas()

pd.options.display.max_columns = 6

df.head(10000)

df.sort_values("rating",ascending=False).head(10000)
df_years.head(100)
df_high_modern=df_modern.drop('metascore', axis=1)[df_modern.rating>=7]
df_high_modern.head(50)

df_print.plot()
df_print2.plot()

sns.distplot(df['rating'], label = 'rating')
df.describe()

#Correlation between the rating of a movie and the length of it
df['rating'].corr(df['length'])
#Correlation between the move critic rating (metascore) and user rating
df['rating'].corr(df['metascore'])

#plots showing the scattering of rating, metascore and length. Notice that axis
#are not normalized.
sns.scatterplot(x=df['metascore'],y=df['rating'])
sns.scatterplot(x=df['length'],y=df['rating'])
sns.scatterplot(x=df_years1.index.values,y=df_years1['length'])

end = timer()
print(end - start)