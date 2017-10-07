# Torrent Renamer

import re




class Episode():

	show = None
	ident = None
	original_filename = None

	def __init__(self, episode_str, switch_split_modes):
		
		print (episode_str)
		self.original_filename = episode_str.strip("?")
		ep_bits = episode_str.split('.')
		
		if switch_split_modes:
			ep_bits = ""
			if ep_bits == "": ep_bits = episode_str.split(' ')

		#print(ep_bits)
		identifier = re.compile('[sS][0-9]{1,2}[eE][0-9]{1,2}')

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

	def get_orig_filename(self):
		return self.original_filename

	def get_ident(self):
		return self.ident

	def get_show(self):
		return self.show

	def get_season(self):

		ident_reg = re.compile('[sS]([0-9]{1,2})')
		ident_num = ident_reg.match(self.ident)
		
		# Basic error handling
		if ident_num == None:
			raise Exception("Error: No season regex match")

		return int(ident_num.group(1))

	def get_episode(self):

		ident_reg = re.compile('[eE]([0-9]{1,2})')
		ident_num = ident_reg.search(self.ident)
		
		# Basic error handling
		if ident_num == None:
			raise Exception("Error: No episode regex match")

		return int(ident_num.group(1))