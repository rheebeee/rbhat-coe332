import json, uuid

def list_to_dict():
    data= {}
    data['traffic02']= []

    with open('data.json','r') as json_file:
        trafficData= json.load(json_file)
        for rows in trafficData:
            data['traffic02'].append(rows)
        
        for x in data['traffic02']:
            x['traffic_report_id']= str(uuid.uuid4())

        
    with open('new_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)


