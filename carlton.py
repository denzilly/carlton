from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from random import *
import csv
import os
import time

from bs4 import BeautifulSoup
import requests


############LIST OF XPATHS##############
cookie1 = "/html/body/div[1]/div/div/div/div[4]/ul/li[1]/div/label[2]"
cookie2 = "/html/body/div[1]/div/div/div/div[4]/ul/li[2]/div/label[2]"
cookiebtn = "/html/body/div[1]/div/div/div/div[5]/button"



textentry = "/html/body/div[1]/div/div/div[3]/div[2]/div/div[1]/div/div/div[1]/div/input"
slayerbtn = "/html/body/div[1]/div/div/div[3]/div[2]/div/ul/div/div/li/div/div/div/div/div[3]/button[2]"

songnext = "/html/body/div[1]/div/div/div[3]/div[2]/div/div[2]/div/div/div/div/a"
motiveernext = "/html/body/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/a/div/span[2]"

name = '//*[@id="name"]'
email = '//*[@id="email"]'

tandc = '//*[@id="accept"]'









############Email Generator###################
