#imports
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import requests
import gspread
import json

def get_sheet_client():
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    return client

class Port:
    def __init__(self, name, desc, link):
        self.name = name
        self.desc = desc
        self.link = link


def createObjects(portnames, portdescs, portlinks):
    ports = []
    for i in range(len(portnames)):
        x = Port(portnames[i], portdescs[i], portlinks[i])
        ports.append(x.__dict__)
    return ports


def main():
    sheet = get_sheet_client().open("portydb").worksheet('main')
    portnames = sheet.col_values(1)
    portdescs = sheet.col_values(2)
    portlinks = sheet.col_values(3)
    return createObjects(portnames, portdescs, portlinks)