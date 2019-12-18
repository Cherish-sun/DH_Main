import redis

#REDIS_HOST = '127.0.0.1'
REDIS_HOST = '172.16.13.1'
REDIS_PORT = 6379
REDIS_STORE = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
# VM_URL_PATH = "http://192.168.1.103:5000/v1/vm/working"
VM_URL_PATH = "http://172.16.11.11:5000/vm/working"