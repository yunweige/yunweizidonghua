import redis
r = redis.Redis(host='192.168.1.31',
                port=6379,
                db=0)

def get_redis(host_ip='192.168.1.31',port=6379,db=0):
    return redis.Redis(host=host_ip, port=port, db=db)