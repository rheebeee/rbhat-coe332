# jobs.py
import uuid
from hotqueue import HotQueue
from redis import StrictRedis

q = HotQueue("queue", host='10.109.236.250', port=6379, db=1)
rd = StrictRedis(host='10.109.236.250', port=6379, db=0)
worker_ip = os.environ.get('WORKER_IP')

def _generate_jid():
    return str(uuid.uuid4())
def _generate_job_key(jid):
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
def _save_job(job_key, job_dict):
    """Save a job object in the Redis database."""
    rd.hmset(job_key, job_dict)
def _queue_job(jid):
    """Add a job to the redis queue."""
    q.put(jid)
    print("Hi")
def set_ip(jid):
    rd.hset(jid,'worker', worker_ip)
def add_job(start, end, status="submitted"):
    """Add a job to the redis queue."""
    jid = _generate_jid()
    job_dict = _instantiate_job(jid, status, start, end)
    # update call to save_job:
    _save_job(_generate_job_key(jid), job_dict)
    print("Part 1")
    # update call to queue_job:
    _queue_job(jid)
    print("Part 2")
    return job_dict
def update_job_status(jid, new_status):
    """Update the status of job with job id `jid` to status `status`."""
    jid, status, start, end = rd.hmget(_generate_job_key(jid), 'id', 'status', 'start', 'end')
    job = _instantiate_job(jid, status, start, end)

    if job:
        job['status'] = new_status
        _save_job(_generate_job_key(job['id']), job)
    else:
        raise Exception()
