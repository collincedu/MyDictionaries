

#open file for reading
txt_file = open("WorldSeriesWinners.txt", 'r')

#first dictionary:names of the teams as keys, number of wins as values
teams_dict = {}

#second dictionary: years as keys, team name as value
years_dict = {}


#counter
start_year = 1903

#input
year = int(input("Enter year for corresponding winning team ")) 

while year != 0 and year < 1903 or year > 2009:
        print('Invalid year, range 1903 - 2009')
        year = int(input("Enter the year for corresponding win "))

#loop
for team in txt_file:
    