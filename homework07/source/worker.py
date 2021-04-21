from jobs import q, update_job_status, set_ip
import time
  
@q.worker
def execute_job(jid):
    update_job_status(jid, "in progress")
    set_ip(jid)
    time.sleep(15)
    update_job_status(jid, "complete")
    
execute_job()
