# api.py
import json
import redis
import form
import uuid
import datetime
from flask import Flask, request, send_file
from jobs import rd_jobs, rd_data, getdata, add_job

app = Flask(__name__)

@app.route('/', methods=['GET'])
def instructions():
    return """
    Here are the routes:
    /           Instructions
    /jobs       Running a job where incidents between a certain min and max latitude are plotted [ANALYSIS]
    /joblist    Returns all the jobs in the queue
    /add        Adds a new inncident to the database [CREATE]
    /dates      Find incidents between a 'start' and 'end' date [READ]
    /edit       Edits the issue of one of the incidents [UPDATE]
    /delete     Delete an incident from the database [DELETE]
    /reset      Resets the redis database
"""

@app.route('/delete', methods=['GET', 'DELETE']) #DELETE OPERATION
def delete():
    #Can delete in the redis database
    if request.method == 'DELETE':
           this_trafficid = str(request.form['trafficid']) 
           rd_data.delete(this_trafficid)
           return f'Traffic ID number {this_trafficid} deleted\n'

    else:
        return """
    This is a route for deleting traffic data from the database.
    Use the form curl -X DELETE -d "trafficid=hrf5jr" 10.99.161.74:5000/delete
"""

@app.route('/jobs', methods=['GET','POST'])#ANALYSIS OPERATION
def run_jobs():
    #Only input if plotting start and end date over time using query or .json data
    #Analysis doesn't change the data
    #Worker.py saving image into the redis database
    if request.method == 'POST':
        try:
            job = request.get_json(force=True)
        except Exception as e:
            return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
        return json.dumps(add_job(job['start'], job['end']))
    else:
        return """
    This is a route for running an analysis job for traffic date. Please enter a start and end date and the number of accidents will be plotted over time.
    Use the form curl -X POST -H "content-type: application/json" -d '{"start": "START", "end": "END"}' 10.99.161.74:5000/jobs
"""

@app.route('/joblist', methods=['GET']) #List of Jobs
def get_jobs():
    redis_dict = {}
    for key in rd_jobs.keys():
        redis_dict[str(key.decode('utf-8'))] = {}
        redis_dict[str(key.decode('utf-8'))]['status'] = rd_jobs.hget(key, 'status').decode('utf-8')
    return json.dumps(redis_dict, indent=4)

@app.route('/dates', methods=['GET']) #READ OPERATION
def get_dates(): 
    trafficData= getdata()
    output= []
    start= request.args.get('start')
    end= request.args.get('end')
    
    startDate= datetime.datetime.strptime(start, '%Y-%m-%dT%H:%M:%S.%f%z')
    endDate= datetime.datetime.strptime(end, '%Y-%m-%dT%H:%M:%S.%f%z')

    for x in trafficData:
        date  = datetime.datetime.strptime(rd_data.hget(x,'published_date'),'%Y-%m-%dT%H:%M:%S.%f%z')
        if startDate <= date <= endDate:
            output.append(x)
        
    return json.dumps(output, indent=2)

@app.route('/add', methods= ['GET','POST']) #CREATE OPERATION
def add_data():
    if request.method == 'POST':
        try:
            data = request.get_json(force=True)
        except Exception as e:
            return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})

        new_data= add_data(data['date'], data['issue'], data['latitude'], data['longitude'], data['address'])
        
        return new_data

    else:
        return """
    This is a route for adding new traffic data to the database. Please enter a published date, the issue, latitude, longitude, and address of the incident.
    Use the form curl -X POST -H "content-type: application/json" -d '{"date": "DATE", "issue": "ISSUE", "latitude": "LATITUDE", "longitude": "LONGITUDE", "address": "ADDRESS"}' 10.99.161.74:5000/add
"""

@app.route('/edit', methods= ['GET']) #CREATE OPERATION
def update_data():
    trafficid= request.args.get('trafficid')
    issue= request.args.get('issue')
    
    rd_data.hset(trafficid, 'issue_reported', issue)
    
    return f'Traffic ID {trafficid} issue has been changed to {issue}\n' 

@app.route('/reset', methods= ['GET'])#Fills the redis database with the .json data
def reset():
    rd_data.flushall()
    rd_jobs.flushall()

    form.list_to_dict()
    with open("new_data.json","r") as json_file:
        trafficData= json.load(json_file)
    
    for item in trafficData['traffic02']:
        rd_data.hmset(item['traffic_report_id'], item)
    
    return "The database has been reset.\n"

def create_data(jid, date, issue, latitude, longitude, address):
    if type(jid) == str:
        return {'id': jid,
                'date': date,
                'issue': issue,
                'latitude': latitude,
                'longitude': longitude,
                'address': address
        }
    return {'id': jid.decode('utf-8'),
            'date': date.decode('utf-8'),
            'issue': issue.decode('utf-8'),
            'latitude': latitude.decode('utf-8'),
            'longitude': longitude.decode('utf-8'),
            'address': address.decode('utf-8')

    }

def save_data(data_key, data_dict):
    """Save the new data object in the Redis database."""
    rd_data.hmset(data_key, data_dict)

def add_data(date, issue, latitude, longitude, address):
    """Add data to the redis database."""
    jid = str(uuid.uuid4())
    data_dict = create_data(jid, date, issue, latitude, longitude, address)
    save_data(jid, data_dict)
    return data_dict

@app.route('/download/<jobid>', methods=['GET'])
def download(jobid):
    path = f'/download/{jobid}.png'
    with open(path, 'wb') as f:
        f.write(rd_jobs.hget(jobid, 'image'))
    return send_file(path, mimetype='image/png', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
