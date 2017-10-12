#!/usr/bin/python
# Torrent Renamer

import requests
import json
import urllib
import os
import re
ver = "1.0.5"


class Service():
    @staticmethod
    def getID(show):

        # Requests JSON of whatever show
        resp = requests.get('http://api.tvmaze.com/singlesearch/shows?q=' + show + "&embed=episodes")
        data = resp.json()

        # Basic error handling
        if resp.status_code != 200:
            raise Exception("Error: Status code is not 200")

        # Returns ID
        return data['id']

    @staticmethod
    def getShowTitle(show_id):

        # Requests JSON of show details
        resp = requests.get('http://api.tvmaze.com/shows/' + str(show_id))
        data = resp.json()

        # Basic error handling
        if resp.status_code != 200:
            raise Exception("Error: Status code is not 200")

        # Returns title
        return data['name']

    @staticmethod
    def getDetails(show_id, season, episode):

        # Requests JSON of show details
        resp = requests.get('http://api.tvmaze.com/shows/' + str(show_id) + '/episodebynumber?season=' + season + '&number=' + episode)
        data = resp.json()

        # Basic error handling
        if resp.status_code != 200:
            raise Exception("Error: Status code is not 200")

        # Returns title
        return data['name']


    @staticmethod
    def getUpdate():
       

        
        # Downloads and opens README.md from master branch
        urllib.request.urlretrieve("https://raw.githubusercontent.com/jclishman/Renamer/master/README.md", "ren_temp.md")
        file = open('ren_temp.md')

        # Gets the version number from the first line of README
        master_ver = re.sub('[# Renamer]', '', file.readline())

        print("\nMaster branch is: " + master_ver)

        # Deletes master branch README.md
        os.remove("ren_temp.md")

        # Ouputs currently running version

        update = input("Currently on: v" + ver + "\nAre you sure? (y/n): ")


        if update.upper() == "Y":

            print("Getting update...")


            # Downloads files
            urllib.request.urlretrieve ("https://raw.githubusercontent.com/jclishman/Renamer/master/Service.py", "Service.py")
            print("Downloaded Service.py")
            urllib.request.urlretrieve ("https://raw.githubusercontent.com/jclishman/Renamer/master/Episode.py", "Episode.py")
            print("Downloaded Episode.py")
            urllib.request.urlretrieve ("https://raw.githubusercontent.com/jclishman/Renamer/master/Renamer.py", "renamer.py")
            print("Update complete. Closing.")
            exit()

        else:
            print("Update aborted, exiting")
            exit()

