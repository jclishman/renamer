# Renamer v1.0.3

Renames torrents of TV shows to a sane naming scheme.

Requires Python 3.6, and the Requests module. Get it with `python -m pip install requests`

Episode filenames must have an identifier (such as `S01E01` or `s10e02`) in order to work properly.


Flags:

-f <x> Change file type (Example: "renamer.py -f avi" will have it look for avi files. Default is mkv)
  
-s     Splits the name along spaces instead of periods

-u 	   Updates the script, replacing itself with the current files in master branch

-v     Outputs version
