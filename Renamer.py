# Torrent Renamer

import os
import glob
from Episode import Episode
from APIService import APIService



#sel = input('Enter directory: ')
filetype = '.mkv'
os.chdir("The Expanse")
print("Currently at: " + os.getcwd())
list_of_episode_strings = glob.glob('*' + filetype)




list_of_episode_objects = []

print ("\n-----LIST OF EPISODES-----\n")
for ep_str in list_of_episode_strings:
	ep = Episode(ep_str)
	list_of_episode_objects.append(ep)
	#print(ep)



print("\n-----DATA-----")
for episode_obj in list_of_episode_objects:

	# Gets the ID of the show, and the raw season/episode numbers
	

	show_id = APIService.getID(episode_obj.show)
	season_str = str(episode_obj.get_season())
	episode_str = str(episode_obj.get_episode())
	show_str = str(episode_obj.get_show())
	ident_str = str(episode_obj.get_ident())

	print("\nAPI ID: " + str(show_id))
	print("Show Title: " + show_str)
	print("Season Number: " + season_str)
	print("Episode Number: " + episode_str)

	title = APIService.getDetails(show_id, season_str, episode_str)
	print ("Episode Title: " + title)

	# Creates the file name
	file_name = show_str + ' ' + ident_str + ' - ' + title + filetype
	print ("Fixed File Name: " + file_name) 
	
	#print (episode_obj.get_orig_filename())
	os.rename(episode_obj.get_orig_filename(), file_name)