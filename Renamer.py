# Torrent Renamer

import os
import glob
from Episode import Episode
from APIService import APIService



#sel = input('Enter directory: ')

os.chdir("The Expanse")
print("Currently at: " + os.getcwd())
ingest = glob.glob('*.mkv')




ep_list = []
print ("-----LIST OF EPISODES-----\n")
for ep_str in ingest:
	ep = Episode(ep_str)
	ep_list.append(ep)
	print(ep)



for episode in ep_list:
	APIService.getID(ep.show)