#!/usr/bin/python
# Torrent Renamer

import requests
import json


class APIService():
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
