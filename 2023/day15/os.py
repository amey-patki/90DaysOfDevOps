
            
import yaml
import json

with open('fruits.yaml', 'r') as file:
    configuration = yaml.safe_load(file)

with open('new.json', 'w') as json_file:
    json.dump(configuration, json_file)
    
output = json.dumps(json.load(open('new.json')), indent=2)
print(output)
