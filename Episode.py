# Torrent Renamer

import re




class Episode():

	show = None
	ident = None
	title = None

	def __init__(self, episode_str):
		
		print (episode_str)
		ep_bits = episode_str.split('.')
		identifier = re.compile('S[0-9]{1,2}E[0-9]{1,2}')

		found_ident = False
		

		for i in ep_bits:

			if not found_ident:
				
				if identifier.match(i):
					found_ident = True
					self.ident = i
					

				else:
					self.show = i if self.show == None else self.show + ' ' + i
					

				

	def __str__(self):
		return ("show: " + self.show + "\n" + "ident: " + self.ident + "\n")
