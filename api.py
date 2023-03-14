from cgitb import reset
import csv
from dataclasses import dataclass
from datetime import date, datetime
from email import message
from enum import unique
from hashlib import new
from http import server
from re import X
import re
from sqlite3 import Timestamp
from tkinter import INSERT
from unittest import result
from utils import exec_sql_file
from utils import *
from psycopg2.extensions import AsIs



from utils import connect

def addProduct(productName, SKU, amount, dateExpired):

    exec_commit('Insert INTO ExpirationDates (productName, SKU, amount, dateExpired) values (%s, %s, %s, %s)', 
                [productName, SKU, amount, dateExpired])
    
def deleteProduct(productName):

    exec_commit('')