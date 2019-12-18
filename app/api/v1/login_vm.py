# -*- coding:utf-8 -*-
import time
import requests
from flask import current_app, jsonify
from app import constants
from app.libs.redprint import Redprint
from app.libs.error_code import NotFound, ServerError
from app.libs.vm_server import getVMinfo
from app.config.setting import REDIS_STORE, VM_URL_PATH

api = Redprint('vm')


@api.route('/login', methods=['POST'])
def vm_login():
    """
    四级员工登录虚拟机接口
    :return: 虚拟机秘钥
    """
    # data = request.form
    # user_name = data.get('user_name')
    # user_id = data.get('user_id')
    # data = data.get('token')
    # try:
    #     data = jwt.decode(data, SECRET_KEY, algorithms=['HS256'])
    # except Exception as e:
    #     current_app.logger.error(e)
    #     return AuthFailed(msg="口令不合法，非法登录")
    #
    # leader_id = data.get("leader_id")
    # leader_name = data.get("leader_name")
    # leader_role = data.get("leader_role")
    # leader_job_id = data.get("leader_job_id")
    # role = data.get("role")
    # role_id = data.get("role_id")
    # job_id = data.get("job_id")
    # department_id = data.get("department_id")
    # department = data.get("department")
    #
    # user_infos = {'user_name': user_name,
    #               'user_id': user_id,
    #               'payload': {"leader_id": leader_id,
    #                           "department": department, "department_id": department_id, "job_id": job_id,
    #                           "role_id": role_id, "role": role, "leader_job_id": leader_job_id,
    #                           "leader_name": leader_name, "leader_role": leader_role}}
    #
    # if not all([role, role_id, job_id, department_id, department]):
    #     raise ParameterException()
    #
    current_ip, secret = getVMinfo()
    user_infos = {'user_name': 'job', 'payload': {'leader_id': '9', 'leader_name': 'caiwu', 'leader_role': 'person', 'leader_job_id': '111', 'role': 'safeperson', 'role_id': '1', 'job_id': '11', 'department_id': '14', 'department': '安全管理部'}, 'user_id': 1}
    """
        打包用户信息到redis,目的是提交给虚拟机
        eg:{'user_name': 'job', 'payload': {}, 'user_id': 1}
    """
    try:
        REDIS_STORE.set(current_ip, user_infos)
        # REDIS_STORE.setex(current_ip, constants.USER_INFOS_REDIS_EXPIRE_SECOND, user_infos)
    except Exception as e:
        current_app.logger.error(e)

    if secret:
        with open('./record', 'a+') as f:
            f.write(time.strftime('%Y-%m-%d %H:%M:%S  ') + str(current_ip) + ' ' + str(user_infos))
            f.write('\n')
        try:
            ret = requests.get(VM_URL_PATH, timeout=5).text
            print(ret)
            current_app.logger.info("启动虚拟机工作")
        except Exception as e:
            current_app.logger.error(e)
            raise ServerError()
        val = {'status': 200, "data": secret}
        return jsonify(val)
        # resp_dict = dict(error_code=0, msg="OK", data=secret)
        # vm_data = json.dumps(resp_dict)
        #return vm_data, 200, {"Content-Type": "application/json"}
    else:
        current_app.logger.error(secret)
        return NotFound(msg="当前没有空闲的虚拟机")
