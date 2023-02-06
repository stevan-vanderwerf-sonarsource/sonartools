import json
import re

results = {}

def extraction(i,j):
    '''extracts alphanumeric characters or digits from string'''
    return ''.join(re.findall(j, i)) 

def sumdigits(i):
    '''calculates the number of digits in string'''
    return sum(c.isdigit() for c in extraction(i,j='\d+'))

def dictionary_entry(i,sumdigits):
    '''creates dictionary entry as short-form/long-form of SonarQube docker tag/edition'''
    if sumdigits == 3:
        results[extraction(i,j='[a-z]+')[0] + 'e' + extraction(i,j='\d+')] = i

def update_dictionary():
    # Opening JSON file
    with open('sonartagmaster.json') as json_file:
        data = json.load(json_file)

        # Iterates through Docker tags, creating corresponding short form as dictionary, e.g. {ee891:8.9.1-enterprise}
        for i in data['tags']:
            if i.startswith(("9", "8", "7")):
                dictionary_entry(i,sumdigits(i))

    # Writing results to file
    with open('sonartagdictionary.json', 'w') as convert_file:
        convert_file.write(json.dumps(results))