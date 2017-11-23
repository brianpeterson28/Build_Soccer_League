'''
Brian Peterson | Github: brianpeterson28 | teamtreehouse.com/brianpeterson

Treehouse Tech Degree - Project 1 - Build A Soccer League

This script opens a csv file containing soccer player information and uses
that information to automatically sort the players into three teams. It also 
automatically generates welcome letters for each player's parent/legal 
gaurdian.  

Teams = (1) Sharks, (2) Dragons, and (3) Raptors. 
'''

import csv
import random

PLAYER_INFO = "soccer_players.csv"
#Get data from file.
def main(): 
	player_info = read_player_info(PLAYER_INFO)
	for player in player_info:
		player = create_player_dict(player)
		if player['name'] == 'Name':
			pass
		else:
			print(player)

	#Create list of empty team objects
		sharks = []
		dragons = []
		raptors = []

#Create list of player objects (dicts)
def read_player_info(file_name):
	player_info = []
	with open(file_name, newline="") as file:
		reader = csv.reader(file)
		for item in reader:
			player_info.append(item)
	return player_info


def create_player_dict(player):
	name, height, experience, guardian_name = player
	player_dict = {'name' : name, 
				   'height' : height, 
				   'experience' : experience,
				   'guardian_name' : guardian_name}
	return player_dict
#Sort players by exerpience level 
#Randomly and equally assign players of each experience level to a team object. 
#Write team objects to teams.txt file in proper format.
#Generate welcome letters. 




if __name__ == "__main__":
	main()