import redis
import time
from config import config

conf = config()

def redis_connect() -> redis.Redis:
    connect = redis.Redis(host=conf.host, port=conf.port, password=conf.password)
    return connect

if __name__ == '__main__':
    redis_connection = redis_connect()
    print('Connected to Redis')
    while True:
        try:
            resultList = redis_connection.hgetall(conf.key_origin)
            if len(resultList)==0:
                print('No data in cache')
            else:
                
                for key in resultList.keys():
                        #add elemented to sorted set
                        redis_connection.zadd(conf.key_destination, {resultList[key] : key})
                        #remove element from cache
                        redis_connection.hdel(conf.key_origin, key)
            time.sleep(conf.update_interval) #wait 1 second
                
        except Exception as e:
            print(e.args)
            
    