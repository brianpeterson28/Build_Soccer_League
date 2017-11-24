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
TEAM_NAMES = ["SHARKS", "DRAGONS", "RAPTORS"]
TEAMS_FILE = "teams.txt"
#Get data from file.
def main(): 

	player_info = read_player_info(PLAYER_INFO)
	experienced_players = []
	unexperienced_players = []
	sharks = []
	dragons = []
	raptors = []
	teams = []

	for player in player_info:
		player = create_player_dict(player)
		if player['name'] == 'Name':
			pass
		else:
			if player['experience'] == 'YES':
				experienced_players.append(player)
			else:
				unexperienced_players.append(player)

	while len(experienced_players) > 0:
		sharks.append(experienced_players.pop(random.randrange(
			len(experienced_players))))
		dragons.append(experienced_players.pop(random.randrange(
			len(experienced_players))))
		raptors.append(experienced_players.pop(random.randrange(
			len(experienced_players))))

	while len(unexperienced_players) > 0:
		sharks.append(unexperienced_players.pop(random.randrange(
			len(unexperienced_players))))
		dragons.append(unexperienced_players.pop(random.randrange(
			len(unexperienced_players))))
		raptors.append(unexperienced_players.pop(random.randrange(
			len(unexperienced_players))))

	teams = [sharks, dragons, raptors]
	create_team_list(teams)

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

def create_team_list(list_of_teams):
	index = 0
	with open(TEAMS_FILE, "a") as file:
		for team in list_of_teams:
			file.write(TEAM_NAMES[index] + "\n")
			index += 1
			for player in team:
				name = player['name']
				experience = player['experience']
				guardian_name = player['guardian_name']
				file.write(name + ", " + experience + ", " + guardian_name
					+ "\n")
			file.write("\n")

#Sort players by exerpience level 
#Randomly and equally assign players of each experience level to a team object. 
#Write team objects to teams.txt file in proper format.
#Generate welcome letters. 

if __name__ == "__main__":
	main()