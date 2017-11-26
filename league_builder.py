'''
Brian Peterson | Github: brianpeterson28 | teamtreehouse.com/brianpeterson

Treehouse Tech Degree - Project 1 - Build A Soccer League

This script opens a csv file containing soccer player information and uses
that information to automatically sort the players into three teams. It also 
automatically generates personalized welcome letters for each player's 
parent/legal gaurdian.*    
'''

import csv
import random

#Create constant data objects that will be used throughout the script. 
PLAYER_INFO = "soccer_players.csv"
TEAM_NAMES = ["SHARKS", "DRAGONS", "RAPTORS"]
TEAMS_FILE = "teams.txt"

#The main function contains the core logic of the script. 
#Step 1: Create player data objects.
#Step 2: Sort player data objects by experience level. 
#Step 3: Assign each player to a team. 
#Step 4: Create team list file. 
#Step 5: Create individual files for personalized letters to parents. 
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

	add_team_name_to_players(sharks, "SHARKS")
	add_team_name_to_players(dragons, "DRAGONS")
	add_team_name_to_players(raptors, "RAPTORS")

	teams = [sharks, dragons, raptors]
	create_team_list(teams)
	create_letters(teams)

#This is a helper function that opens the csv file and stores the player
# data into a python list object for use by the main function. 
def read_player_info(file_name):
	player_info = []
	with open(file_name, newline="") as file:
		reader = csv.reader(file)
		for item in reader:
			player_info.append(item)
	return player_info

#This is a helper function that creates a dictionary object for each player. 
#The dicitonary object holds all the relevant information about the player. 
def create_player_dict(player):
	name, height, experience, guardian_name = player
	player_dict = {'name' : name, 
		       'height' : height, 
	               'experience' : experience,
		       'guardian_name' : guardian_name}
	return player_dict

#This is a helper function that drafts the teams.txt file which lists all the
#players organized by team. 
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

#This is a helper function that drafts personalized letters to each player's 
#legal guardian(s). 
def create_letters(list_of_teams):
	players = []
	for team in list_of_teams:
		for player in team:
			players.append(player)
			file_name = create_letter_file_name(player['name'])
			with open(file_name, "w") as letter:
				guardian_name = player['guardian_name']
				player_name = player['name']
				team_name = player['team_name']
				date_and_time = "Wednesday, May 2, 2018 at 5:00 PM"
				letter.write("Dear " + guardian_name + ", \n")
				letter.write("\n")
				letter.write("Welcome to the Soccer League. ")
				letter.write(player_name + " will be on the " + team_name + 
					         ".\n\n")
				letter.write("The first practice is on " + date_and_time)
				letter.write("\n\n")
				letter.write("We look forward to seeing you. \n")

#This is a helper function that formats the file names for use in the 
#create_letters function. 
def create_letter_file_name(player_name):
	file_name = player_name.lower().replace(" ", "_")
	file_name += ".txt"
	return file_name

#This is a helper function that updates the player dictionaries with the 
#name of the team they have been assigned to. 
def add_team_name_to_players(team, team_name):
	for player in team:
		player['team_name'] = team_name
	return team

#The main function executes when league_builder.py is run from the 
#command line. 
if __name__ == "__main__":
	main()
