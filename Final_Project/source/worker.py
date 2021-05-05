from jobs import q, update_job_status, rd_jobs, rd_data
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

@q.worker 
def execute_job(jid):
    
    update_job_status(jid, "in progress")
    
    lat_vals=[]
    long_vals=[]
    
    start= rd_jobs.hget(jid, 'start').decode('utf-8')
    end= rd_jobs.hget(jid, 'end').decode('utf-8')   
    
    for key in rd_data.keys():
        if(start  <= rd_data.hget(key, 'latitude') <= end):
            long_vals.append(float(rd_data.hget(key, 'longitude')))
            lat_vals.append(float(rd_data.hget(key, 'latitude')))
    
    bbox= (-98.0044, -97.4702, 30.3734, 30.1588)
    im= plt.imread('Austin.png')
    implot= plt.imshow(im, zorder=0,extent= [bbox[0], bbox[1], bbox[2], bbox[3]])
    
    plt.scatter(long_vals, lat_vals, zorder=1, c='b', s=10)
    plt.title('Plotting Traffic Incidents on an Austin Map')
    plt.xlim(bbox[0],bbox[1])
    plt.ylim(bbox[2],bbox[3])
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.show()
    plt.savefig('plot.png')

    with open('plot.png', 'rb') as f:
        img= f.read()
    
    rd_jobs.hset(jid, 'image', img)
    update_job_status(jid, "complete")
    
execute_job()
