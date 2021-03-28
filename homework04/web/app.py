import json
import datetime
import redis
from flask import Flask, request

#rd= redis.StrictRedis(host= '127.0.0.1', port= 6379, db=0)
rd= redis.StrictRedis(host= 'redis', port= 6379, db=0)
app= Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello World!\n"

@app.route('/animals', methods= ['GET'])
def get_animals():
    return json.dumps(getdata(), indent=2)

@app.route('/animals/legs', methods= ['GET'])
def get_legs():
    animaldata= getdata()
    number= request.args.get('number')
    output = [x for x in animaldata if x['legs'] == int(number)]

    return json.dumps(output, indent=2)

@app.route('/animals/head', methods=['GET'])
def get_animal_head():
    animaldata= getdata()
    name= request.args.get('name')
    output= [x for x in animaldata if x['head'] == name]
    return json.dumps(output, indent=2)

@app.route('/animals/dates', methods=['GET'])
def get_dates(): 
    animaldata= getdata()
    output= []
    start= request.args.get('start')
    end= request.args.get('end')
    
    startDate= datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S.%f')
    endDate= datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S.%f')

    for x in animaldata:
        created_on = datetime.datetime.strptime(x['created_on'],'%Y-%m-%d %H:%M:%S.%f')
        if startDate <= created_on <= endDate:
            output.append(x)
        
    return json.dumps(output, indent=2) 

@app.route('/animals/delete', methods=['GET'])
def get_dates_delete(): 
    animaldata= getdata()
    my_animals=[]
    start= request.args.get('start')
    end= request.args.get('end')
    output= []

    startDate= datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S.%f')
    endDate= datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S.%f')
    
    for x in animaldata:
        created_on = datetime.datetime.strptime(x['created_on'],'%Y-%m-%d %H:%M:%S.%f')
        if startDate <= created_on <= endDate:
            output.append(x)
    
    for x in output:
        animaldata.remove(x)

    return json.dumps(output, indent=2)

@app.route('/animals/uid', methods=['GET'])
def get_uid():
    animaldata= getdata()
    uid= request.args.get('uid')
    output= [x for x in animaldata if x['uid'] == uid]
    return json.dumps(output, indent=2)

@app.route('/animals/edit', methods=['GET'])
def get_edit():
    animaldata= getdata()
    uid= request.args.get('uid')
    head= request.args.get('head')
    body= request.args.get('body')
    arms= request.args.get('legs')
    tail= request.args.get('tail')
    
    output= [x for x in animaldata if x['uid'] == uid]
    
    for x in output:
        x['head']= head
        x['body']= body
        x['arms']= arms
        x['tail']= tail
    
    return json.dumps(output, indent=2)

@app.route('/animals/avglegs', methods=['GET'])
def get_avg_legs():
    animaldata= getdata()
    total=0
    for x in animaldata:
        total= total + int(x['legs'])
    avg= total/ len(animaldata)
    return "Average of all the legs is " + str(avg) + "\n"

@app.route('/animals/total', methods=['GET'])
def get_total():
    animaldata= getdata()
    return "Total count of animals is " + str(len(animaldata)) + "\n"

@app.route('/data/reset', methods= ['GET'])
def reset():
    with open("animals.json","r") as json_file:
        animaldata= json.load(json_file)
    rd.set('rhea-reset', json.dumps(animaldata))
    return "The database has been cleared."

def getdata():
    return json.loads(rd.get('rhea-data').decode('utf-8'))
    #with open("animals.json","r") as json_file:
    #    animaldata= json.load(json_file)
    #return animaldata

#Create app route to reset reddis data

if __name__ == '__main__':
    #port = '5000'
    app.run(debug= True, host= '0.0.0.0')
