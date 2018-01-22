#!/usr/bin/python
# Torrent Renamer

import os
import re
import glob
import time
import argparse
from Episode import Episode
from Service import Service

# Filetype & Split argument
parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, help="select filetype")
parser.add_argument("-s", action="store_true", help="splits titles on spaces instead of periods")
parser.add_argument("-u", action="store_true", help="updates the script from master branch, use with caution")
parser.add_argument("-v", action="store_true", help="version")
args = parser.parse_args()

# Default variables
filetype = '.mkv'
switch_split_modes = False
ver = "1.0.7"
counter = 0

if args.f:
    filetype = '.' + args.f
    print("Filetype changed to: " + args.f)

if args.s:
    print("Changing split mode to spaces")
    switch_split_modes = True

if args.u:
    Service.getUpdate()

if args.v:
    print("Renamer v" + ver)
    exit()
    
current_working_directory = input('\nEnter directory: ')

def file_loop(current_working_directory):
	os.chdir(current_working_directory)
	#print("[DIRECTORY CHANGE] " + os.getcwd())

	for entry in glob.glob('*', recursive=True):
		if(os.path.isdir(entry)): 
			print('\n[DIRECTORY FOUND] ' + entry + '\\')
			file_loop(entry)

		else:	
			print('[FILE FOUND] ' + entry)
			rename_file(entry)

	os.chdir('../')

def rename_file(file_name):
	global counter

	# Gets the ID of the show, and the raw season/episode numbers
	episode_obj = Episode(file_name, switch_split_modes)
	show_id = Service.getID(episode_obj.show)
	season_str = str(episode_obj.get_season())
	episode_str = str(episode_obj.get_episode())
	ident_str = str(episode_obj.get_ident()).upper()

    # print("\nAPI ID: " + str(show_id))

	show_str = Service.getShowTitle(show_id)
	print("     [SHOW TITLE] " + show_str)
	print("     [SEASON] " + season_str)
	print("     [EPISODE] " + episode_str)

	title = Service.getDetails(show_id, season_str, episode_str)
	title_clean = re.sub('[:?]', '', title)
	if title != title_clean:
	    print("     [WARNING] Episode title dirty, sanitizing")

	print("     [TITLE] " + title_clean)

    # Creates the file name
	fixed_file_name = show_str + ' ' + ident_str + ' - ' + title_clean + filetype

	print("     [FIXED FILE NAME] " + fixed_file_name + '\n')

    # print (episode_obj.get_orig_filename())
	os.rename(episode_obj.get_orig_filename(), fixed_file_name)
	counter += 1

start_time = time.time()
file_loop(current_working_directory)
elapsed_time = time.time() - start_time
print("\nAll done! " + str(counter) + " episode names were changed. Took " + str(round(elapsed_time, 2)) + " seconds.")