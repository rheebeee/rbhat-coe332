import json
from flask import Flask, request

app= Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello World!\n"

@app.route('/animals', methods= ['GET'])
def get_animals():
    return json.dumps(getdata(), indent=2)

@app.route('/animals/legs/', methods= ['GET'])
def get_legs():
    animaldata= getdata()
    number= request.args.get('number')
    output = [x for x in animaldata if x['legs'] == int(number)]

    return json.dumps(output, indent=2)

@app.route('/animals/head/', methods=['GET'])
def get_animal_head():
    animaldata= getdata()
    name= request.args.get('name')
    output= [x for x in animaldata if x['head'] == name]
    return json.dumps(output, indent=2)

def getdata():
    with open("animals.json","r") as json_file:
        animaldata= json.load(json_file)
    return animaldata

if __name__ == '__main__':
    app.run(debug= True, host= '0.0.0.0', port= '5003')
