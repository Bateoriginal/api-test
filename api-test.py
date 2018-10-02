'''
	api-test.py
	Bat-Orgil Batjargal, 1 October, 2018
	
	Used NASA Astroid API
	Data: Retrieve a list of Asteroids based on their closest approach date to Earth. 
	GET https://api.nasa.gov/neo/rest/v1/feed?start_date=START_DATE&end_date=END_DATE&api_key=API_KEY

	QUERY PARAMETERS
	Parameter	Type	Default	Description
	start_date	YYYY-MM-DD	none	Starting date for asteroid search
	end_date	YYYY-MM-DD	7 days after start_date	Ending date for asteroid search
	api_key	string	DEMO_KEY	api.nasa.gov key for expanded usage

	Assignment goal is to allow users
	(1) get a list of things
	(2) get details about a single thing
	Ex: You might allow the user to (1) get a list of all senators and (2) given a senator's name 
	(or ID number, or whatever the API uses to uniquely identify a senator), print detailed information about that senator.
'''

import sys 
import argparse
import json
import urllib.request

def get_astroid_names():
 	url = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=T0dyzDdd835vwrdufEiFjOFyasdZKcSb4WkUhOfG'
    data_from_server = urllib.request.urlopen(url).read() 
    string_from_server = data_from_server.decode('utf-8')
    astroid_list = json.loads(string_from_server)
    result_list = []
    for astroid_dictionary in astroid_list:
        name = astroid_dictionary['name']
        result_list.append(name)
    return result_list

def get_astroid_detail(name):
    url = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=T0dyzDdd835vwrdufEiFjOFyasdZKcSb4WkUhOfG'
    data_from_server = urllib.request.urlopen(url).read() 
    string_from_server = data_from_server.decode('utf-8')
    astroid_list = json.loads(string_from_server)
    result_list = []
    for astroid_dictionary in astroid_list:
        if name == astroid_dictionary['name']:
        	estimated_diameter = astroid_dictionary['astroid_dictionary']['kilometers']
        	is_potentially_hazardous_asteroid = astroid_dictionary['is_potentially_hazardous_asteroid']

        	result_list.append({'estimated_diameter':estimated_diameter, 'is_potentially_hazardous_asteroid':is_potentially_hazardous_asteroid})
    return result_list

def main(args):
    if args.action == 'names':
        names_of_astroids = get_astroid_names()
        for i in names_of_astroids:
            print(i)

    elif args.action == 'details':
        astroid_details = get_astroid_detail(args.name)
        for info in astroid_details:
    
            diameter = info['estimated_diameter']
            hazard = info['is_potentially_hazardous_asteroid']
            if hazard:
            	print(arge.name' has {0}km diameter and IS a danger to humanity]'.format(diameter))
        	else:
        		print(arge.name' has {0}km diameter and IS NOT a danger to humanity]'.format(diameter))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Get info about Astroids')

    parser.add_argument('action', metavar='action', help='action to perform on the data ("names" or "detail")',
                        choices=['names', 'detail'])

    parser.add_argument('name', help='name the asteroid of detail you want')
    args = parser.parse_args()
    main(args)