# Torrent Renamer

import requests




class APIService():
	
	@staticmethod
	def getID(show):

		req = requests.get('http://api.tvmaze.com/singlesearch/shows?q=' + show)
		print(req.text)


	@staticmethod
	def getDetails():
		pass