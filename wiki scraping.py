from bs4 import BeautifulSoup as bs
import requests

#defining global variables
letter_list=[]
count = {}

#Extracts info from website, run this only once when changing URL
def get_info():
    global paragraphs
    url = "https://en.wikipedia.org/wiki/Phoenix,_Arizona"
    r=requests.get(url).content
    s=bs(r,"html.parser")
    paragraphs=s.find_all("p")

#Makes a list of letters out of all paragraphs
def convert_to_letters():
    for paragraph in paragraphs:
        for sentance in paragraph.find_all(text=True):
            for letter in sentance:
                clean_letter=letter.replace("\n","")
                if clean_letter.isalpha() == True:
                    letter_list.append(clean_letter.lower())

#Adds letters to dictionary and counts them
def add_to_dictionary():
    for letter in letter_list:
        count.setdefault(letter,0)
        count[letter]+=1

#Prints out letters by descending balues
def print_by_value():
    values_and_keys=[(value,key) for key , value in count.items()]
    values_and_keys.sort(reverse=True)
    for value_and_key in values_and_keys:
        print("letter " + str(value_and_key[1]) + " has been shown " + str(value_and_key[0]) +" times.")

#Running the function
def run():
    get_info()
    convert_to_letters()
    add_to_dictionary()
    print_by_value()

run()



