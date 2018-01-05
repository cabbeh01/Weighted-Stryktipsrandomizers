# Importing Library
import random
import msvcrt as m
import urllib2
import re
import os
from bs4 import BeautifulSoup

clear = lambda: os.system('cls')

def wait():
    m.getch()
    return

def random13():

    rad = 0

    # Declares Arrays
    one = []
    cross = []
    two = []
    procent_box=[]
    hteam_box=[]

    # Importing information from the week's matches
    quote_page = 'http://tipsrader.se/spel/stryktips'
    page = urllib2.urlopen(quote_page)
    soup = BeautifulSoup(page, "html.parser")

    # Picks out the 13 rows
    procent_box = soup.findAll("td", attrs={"class": "percentinfo"})
    hteam_box = soup.find("span", attrs={"class": "hometeam"})

    for rad in range(0, 13):
        # Cleans the rows from html
        procent = procent_box[rad].text.strip()


        # Sorts the rows in to 1|x|2
        sortname = re.split(r"-\s", procent)

        # Coverting string to Float
        one = float(re.search(r'\d+', sortname[0]).group())
        cross = float(re.search(r'\d+', sortname[1]).group())
        two = float(re.search(r'\d+', sortname[2]).group())

        # Converting from int till decimals
        ONE = one/100
        CROSS = cross/100
        TWO = two/100

        # Makes the line number order line up with each other
        NR = int(rad + 1)
        if NR < 10:
            NR = "%d " % NR

        #Structuring a 13-rows system
        elements = ['%s -  1| | ' % NR, '%s -   |X| ' % NR, '%s -   | |2' % NR]

        #Adds percentage on several factors 1,X or 2
        weights = [ONE, CROSS, TWO]

        #Randomizes with a percentage
        from numpy.random import choice
        print(choice(elements, p=weights))

        rad+=1
    return


while True:
    random13()
    wait()
    clear()
