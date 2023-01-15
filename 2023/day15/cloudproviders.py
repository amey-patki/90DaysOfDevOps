import json

#opening json file
with open('service.json') as json_file:
    data=json.load(json_file)
    
    
#print type of data
print(("Type:",type(data)))

#print the data of dictionary
print("Cloud Services \n",data['cloud_providers'] )

