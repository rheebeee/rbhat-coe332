# jobs.py
import uuid
import json
from hotqueue import HotQueue
from redis import StrictRedis

rd_data= StrictRedis(host= '10.105.231.136', port=6379, db=2, decode_responses= True)
q = HotQueue("queue", host= '10.105.231.136', port=6379, db=1)
rd_jobs = StrictRedis(host= '10.105.231.136', port=6379, db=0)

def _generate_jid():
    return str(uuid.uuid4())

def _generate_job_key(jid):
    if type(jid) == bytes:
        jid = jid.decode('utf-8')
    return 'job.{}'.format(jid)

def _instantiate_job(jid, status, start, end):
    if type(jid) == str:
        return {'id': jid,
                'status': status,
                'start': start,
                'end': end
        }
    return {'id': jid.decode('utf-8'),
            'status': status.decode('utf-8'),
            'start': start.decode('utf-8'),
            'end': end.decode('utf-8')
    }

def _save_job(jid, job_dict):
    """Save a job object in the Redis database."""
    rd_jobs.hmset(jid, job_dict)

def _queue_job(jid):
    """Add a job to the redis queue."""
    q.put(jid)

def add_job(start, end, status="submitted"):
    """Add a job to the redis queue."""
    jid = _generate_jid()
    job_dict = _instantiate_job(jid, status, start, end)
    # update call to save_job:
    _save_job(jid, job_dict)
    # update call to queue_job:
    _queue_job(jid)
    return job_dict

def update_job_status(jid, new_status):
    """Update the status of job with job id `jid` to status `status`."""
    jid, status, start, end = rd_jobs.hmget(jid, 'id', 'status', 'start', 'end')
    job = _instantiate_job(jid, status, start, end)

    if job:
        job['status'] = new_status
        _save_job(job['id'], job)
    else:
        raise Exception()

def getdata():
    return rd_data.keys()
