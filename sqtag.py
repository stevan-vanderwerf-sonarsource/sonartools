# importing the module
import json
import re
 
# Opening JSON file
with open('sqtagmaster.json') as json_file:
    data = json.load(json_file)

    for i in data['tags']:
        if i.startswith("9") or i.startswith("8") or i.startswith("7"):
            rawdigits = re.findall("\d+", i)
            digits = ''.join(rawdigits)
            rawalpha = re.findall("[a-z]+", i)
            alpha = ''.join(rawalpha)
            if alpha == 'datacenter':
                edition = 'dce'
                print(edition + digits)
            elif alpha.startswith('de'):
                edition = 'dev'
                print(edition + digits)
            elif alpha.startswith('e'):
                edition = 'ee'
                print(edition + digits)
            elif alpha.startswith('c'):
                edition = 'ce'
                print(edition + digits)
        elif i.startswith("lts"):
            print(i)
        elif i.startswith("c") or i.startswith("d") or i.startswith("e"):
            print(i)