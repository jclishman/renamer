# Torrent Renamer

import os
import glob
import re

# STEP 0


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
					ident = i
					print ("ident: " + ident)



# STEP 1

sel = input('Enter directory: ')
os.chdir(sel)
print("Currently at: " + os.getcwd())
ingest = glob.glob('*.mkv')


# STEP 2

ep_list = []
print ("-----LIST OF EPISODES-----")
for ep_str in ingest:
	ep_list.append(Episode(ep_str))

