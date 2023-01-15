import yaml

with open('fruits.yaml') as yaml_file:
    output=yaml.load(yaml_file,Loader=yaml.FullLoader)
    
    
    
#read yaml file
print(output)