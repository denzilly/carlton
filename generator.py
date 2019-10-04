from random import *
import csv

from bs4 import BeautifulSoup
import requests

#### This script generates personal information
#name
#phone number
#email address
#address


################### GET PHONE NUMBER ####################################

def get_phone():
    phone_no = "064" + str(randint(1000000,9999999))

    return phone_no

#################### GET NAME AND EMAIL ADDRESS ############################

def get_name_email():


    #Select first and last name at random from a list
    firstnum = randint(1,9500)
    lastnum = randint(1,9500)
    def nameget(index, filename):
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            rows = [row[0] for idx, row in enumerate(csv_reader) if idx in(index, index)]

            return rows


    #seperate call statements because we need these for the emails
    first_name = nameget(firstnum,'data/resources/voornamen.csv')[0]
    last_name = nameget(lastnum,'data/resources/achternamen.csv')[0]

    full_name = first_name + " " + last_name
    print (full_name)



    r1 = randint(1,3)
    r2 = randint(1,3)
    r3 = randint(1,2)
    r4 = randint(0,5)

    #abbreviate name in email?
    if (r1 == 1):
        fname = first_name[0]
        lname = last_name
    elif (r1 == 2):
        fname = first_name[:len(first_name)-1]
        lname = last_name[0]
    else:
        fname = first_name[:len(first_name)-1]
        lname = last_name

    #period or underscore separator?
    if (r2 == 1):
        sep = ""
    elif(r2 == 2):
        sep = "."
    else:
        sep = "_"

    #Number at the end?
    if (r3 == 1):
        num = randint(23,99)
    else:
        num = ""

    # Select a Domain
    domains = ["@gmail.com", "@yahoo.com", "@xs4all.nl", "@kpnmail.nl", "@hotmail.com", "@live.com"]
    domain = domains[r4]

    #Piece it all together
    email = fname + sep + lname + str(num) + domain

    print(email)
    return full_name, email



#################Address#############

def get_address():


    count = 0

    #Generate a real postcode, which we will use to find a street to live on
    postcode = str(randint(1000,9999))



    url = "https://www.postcode.nl/zoek/" + postcode

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")


    #Scrape an actual streetname from a postcode website
    for link in soup.find_all('a'):
        p = str(link.get('href'))

        if p[0] == "s":
            d = p.split("/")
            num = d[len(d)-2:len(d)]
            e = d[2].split("%")

            street = e[0] + " " + str(e[1][2:3])


            break

    #Find City Name
    for row in soup.find_all('td'):
        count += 1
        if count == 3:
            city = row.text.strip()
            break


    address = [street, postcode, city]
    print(address)
    return address
