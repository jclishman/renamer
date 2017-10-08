#!/usr/bin/python
# Torrent Renamer

import requests
import json
import urllib

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
        resp = requests.get(
            'http://api.tvmaze.com/shows/' + str(show_id) + '/episodebynumber?season=' + season + '&number=' + episode)
        data = resp.json()

        # Basic error handling
        if resp.status_code != 200:
            raise Exception("Error: Status code is not 200")

        # Returns title
        return data['name']


    @staticmethod
    def getUpdate():
       
        urllib.urlretrieve ("https://raw.githubusercontent.com/jclishman/Renamer/master/Service.py", "Service.py")
        print("Downloaded Service.py")
        urllib.urlretrieve ("https://raw.githubusercontent.com/jclishman/Renamer/master/Episode.py", "Episode.py")
        print("Downloaded Episode.py")
        urllib.urlretrieve ("https://raw.githubusercontent.com/jclishman/Renamer/master/Renamer.py", "renamer.py")
        print("Downloaded renamer.py")
        print("Update complete. Closing.")