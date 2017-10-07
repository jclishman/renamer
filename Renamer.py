#!/usr/bin/python
# Torrent Renamer

import os
import re
import glob
import time
import argparse
from Episode import Episode
from APIService import APIService

# Filetype & Split argument
parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, help="select filetype")
parser.add_argument("-s", action="store_true", help="splits titles on spaces instead of periods")
args = parser.parse_args()

# Default filetype, unless specified otherwise
filetype = '.mkv'
switch_split_modes = False

if args.f:
    filetype = '.' + args.f
    print("Filetype changed to: " + args.f)
if args.s:
    print("Changing split mode to spaces")
    switch_split_modes = True

sel = input('\nEnter directory: ')
os.chdir(sel)
print("Changed to: " + os.getcwd())

start_time = time.time()
list_of_episode_strings = glob.glob('*' + filetype)
list_of_episode_objects = []

print("\n-----LIST OF EPISODES-----\n")
for ep_str in list_of_episode_strings:
    ep = Episode(ep_str, switch_split_modes)
    list_of_episode_objects.append(ep)

    if len(list_of_episode_objects) == 0:
        raise Exception("Error: No files found")
        # print(ep)

print("\n-----DATA-----")
for episode_obj in list_of_episode_objects:

    # Gets the ID of the show, and the raw season/episode numbers

    show_id = APIService.getID(episode_obj.show)
    season_str = str(episode_obj.get_season())
    episode_str = str(episode_obj.get_episode())
    # show_str = str(episode_obj.get_show())
    ident_str = str(episode_obj.get_ident()).upper()

    # print("\nAPI ID: " + str(show_id))

    show_str = APIService.getShowTitle(show_id)
    print("\nShow Title: " + show_str)
    print("Season Number: " + season_str)
    print("Episode Number: " + episode_str)

    title = APIService.getDetails(show_id, season_str, episode_str)
    title_clean = re.sub('[:?]', '', title)
    if title != title_clean:
        print("[WARNING] Episode title dirty, sanitizing")

    print("Episode Title: " + title_clean)

    # Creates the file name
    file_name = show_str + ' ' + ident_str + ' - ' + title_clean + filetype

    print("Fixed File Name: " + file_name)

    # print (episode_obj.get_orig_filename())
    os.rename(episode_obj.get_orig_filename(), file_name)

elapsed_time = time.time() - start_time
print("\nAll done! " + episode_str + " episode names were changed. Took " + str(round(elapsed_time, 2)) + " seconds.")
