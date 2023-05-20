#!/usr/bin/env python3

import re
import csv

# examples 

bio = "Ig: eeny.__"

#bio = "Check out my Instagram account: Instagram: something"
#bio = "Hey I am a docter and my insta is this Insta: simo "
#bio = "hey bro I am just writing some nonsese " 

#bios = [bio1, bio2, bio3, bio4]

# Define regular expressions for matching Instagram handles
regex1 = r'IG:\s*(\S+)'  # Matches "IG: " followed by non-whitespace characters
regex2 = r'Instagram:\s*(\S+)'  # Matches "Instagram: " followed by non-whitespace characters
regex3 = r'Insta:\s*(\S+)'  # Matches "Insta: " followed by non-whitespace characters
regex4 =  r"(?i)(?:ig|insta(?:gram)?)[\s:]([a-zA-Z0-9._]+)"

# Define a function to extract Instagram handles from a user profile
def extract_instagram_handle(bio):
    ig_handle1 = re.search(regex1, bio)
    ig_handle2 = re.search(regex2, bio)
    ig_handle3 = re.search(regex3, bio)
    ig_handle4 = re.search(regex4, bio)
    ig_handle = ig_handle1 or ig_handle2 or ig_handle3 or ig_handle4

    if ig_handle:
        return ig_handle.group(1)
    else:
        return None

# Open the output file and write the extracted Instagram handles to it

def make_file():
    with open('instagram_handles.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:  # Check if the file is empty
            writer.writerow(['Bio', 'Instagram'])
        ig_handle = extract_instagram_handle(bio)
        writer.writerow([bio, ig_handle if ig_handle else ''])

make_file()
