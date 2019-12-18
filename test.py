import redis
from app.config import setting

redis_store = redis.StrictRedis(host=setting.REDIS_HOST, port=setting.REDIS_PORT, decode_responses=True)
# user_name = "job"
# user_id = 1
# payload = {"leader_id": "9", "leader_name": "caiwu", "leader_role": "人事", "leader_job_id": "111", "role": "安全管理员",
#            "role_id": "1", "job_id": "11", "department_id": "14", "department": "安全管理部"}
#
current_ip = "172.16.6.100"
# new_dict = {
#     "user_name": user_name,
#     "payload": payload,
#     "user_id": user_id
# }
# redis_store.setex(current_ip, constants.USER_INFOS_REDIS_EXPIRE_SECOND, new_dict)
# print("存储完成")
ret = redis_store.get(current_ip)
print(ret)
# redis_store.delete(current_ip)
# print("删除成功")
# ret = redis_store.get(current_ip)
# print(ret)

