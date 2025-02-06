import redis

def redis_client():
    db = redis.Redis(host='localhost', port=6379, decode_responses=True)
    db.hset("menu", mapping={"types": str(['pepperoni', 'mexicana', 'tres quesos', 'carnes frias'])})
    return db