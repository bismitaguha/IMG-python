import mysql.connector
from mysql.connector import Error
import requests
import urllib3
from bs4 import BeautifulSoup
from Exception import DataException

def decorator(func):
    def inner(x):
        try:
            mySQLconnection = mysql.connector.connect(host='localhost',
                                                    database='main',
                                                    user='bismita',
                                                    password='biscuit@7777')
            query = "SELECT * FROM user;"
            cursor = mySQLconnection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            check= False
            for row in records:
                if x == row[0]:
                    check = True
            if check:
                print(x,' exists')
                returned_value = func(x)
            else:
                raise Exception('does not exist')
            cursor.close()
            return returned_value
        
        except Error as e:
            print("Error while conn to mysql", e)
    return inner        

def scrape(name):
    URL = f"https://en-gb.facebook.com/{name}"
    for person in person_scrapped:
        if person.username == name:
            return person.show_values()
    try:        
        page = requests.get(URL)

    except: 
        print("user doesn't exist")

    soup = BeautifulSoup(page.content, 'html.parser')
    Name = soup.find('a', class_='_2nlw _2nlv').get_text()
    City = soup.find('span', class_='_2iel _50f7').get_text()
    print("Current City: ", end=' ')
    print(City) 
    Work = []

    try:
        for tags in soup.find(attrs={'class':'_4qm1'}).findAll(attrs={'class': '_2lzr _50f5 _50f7'}):
            Work.append(tags.find('a').contents[0])
    except:
        print("Work does not exist")
    categories = {}
    print("Work: ")
    print(Work)

    try:
        for rows in soup.find(attrs={'class': 'mtm _5e7- profileInfoTable _3stp _3stn'}).findAll('tbody'):
            if rows.find(attrs={'class': 'labelContainer'}).contents[0] != 'Other':
                categories.update({rows.find(attrs={'class':'labelContainer'}).contents[0]: rows.find(attrs={'class':'mediaPageName'}).contents[0]})
    except:
        pass
    
    if len(categories) == 0:
        print('Favourites does not exist')
    else:
        print('Favourites: ', end=' ')
        print(categories)
    person = Person(name, Name, Work, City)
    person_scrapped.append(person)
    return "Bismita"


class Person:
    def __init__(self, username=None, name=None, work=[], city='Roorkee'):
        if username != None:
            self.username = username
        self.name = name
        if work != []:
            self.work = work
        self.city = city
    
    def show_values(self):
        self.message =  f"My name is {self.name} and my current city is {self.work}"
        print(self.message)
        return self.message

global person_scrapped
person_scrapped = []

if __name__ == '__main__':
    while True:
        x = input("Find users ")
        scrape(x)
        
        
    
