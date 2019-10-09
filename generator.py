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



    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'k', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z',] 


    count = 0

    #Generate a real postcode, which we will use to find a street to live on
    postcode_getal = str(randint(1000,9999))
    postcode = str(postcode_getal) + " " + letters[randint(0,24)] + letters[randint(0,24)]
    


    #Select first and last name at random from a list
    citynum = randint(1,354)
    streetnum = randint(1,174)
    def nameget(index, filename):
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            rows = [row[0] for idx, row in enumerate(csv_reader) if idx in(index, index)]

            return rows


    #seperate call statements because we need these for the emails
    city = nameget(citynum,'data/resources/addresses.csv')[0]
    street = nameget(streetnum,'data/resources/street.csv')[0]

    


    address = [street, postcode, city]
    
    return address


