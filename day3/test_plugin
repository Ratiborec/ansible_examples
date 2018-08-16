#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from ansible.module_utils.basic import *
from subprocess import *
import requests
import re
import psutil

def collect_data_proc(proc):
    data = []
    pids = check_output(["pidof", proc]).rstrip().split(" ")
    for con in psutil.net_connections('all'):
        if con.status == "LISTEN" and str(con.pid) in pids:
            tmp = {
                "proccess": proc,
                "pid": con.pid,
                "port": con.laddr.port
            }
            data.append(tmp)

    return data


def collect_curl_data(url, con, head):
    data = {}
    req = requests.get(url)
    match_con = re.findall(re.template(con), str(req.content))
    p = subprocess.Popen(["curl", "-ILs", "http://tut.by"], stdout=subprocess.PIPE)
    match_head = re.findall(re.template(head), str(p.communicate()[0]))
    data.update(
        {
            'content': {
                'responce_code': req.status_code,
                'contains': match_con
            },
            'header': {
                'header': match_head
            }
        })
    req.close()
    return data


def main():
    module = AnsibleModule(
        argument_spec=dict(
            proc=dict(required=True, type='str'),
            url=dict(required=True, type='str'),
            regexp_con=dict(required=True, type='str'),
            regexp_head=dict(required=False, type='str')
        )
    )
    proc = module.params["proc"]
    url = module.params["url"]
    regexp_con = module.params["regexp_con"]
    regexp_head = module.params["regexp_head"]
    proc_info = collect_data_proc(proc)
    match_content = collect_curl_data(url, regexp_con, regexp_head)

    result = dict(
        msg='',
        changed=False,
        proccess=proc_info,
        match=match_content
        #application_url="{}{}".format(url, url)
    )

    module.exit_json(changed=False, result=result)
    module.fail_json(msg="Error getting info", result=result)


if __name__ == '__main__':
    main()

from ansible.module_utils.basic import *
from subprocess import *
import requests
import re
import psutil

def collect_data_proc(proc):
    data = {}
    pids = check_output(["pidof", proc]).rstrip().split(" ")
    for con in psutil.net_connections('all'):
        if con.status == "LISTEN" and str(con.pid) in pids:
            tmp = {
                "proccess": proc,
                "pid": con.pid,
                "port": con.laddr.port
            }
            data.update(tmp)

    return data


def collect_curl_data(url, regexp):
    data = {}
    req = requests.get(url)
    pattern = r"regexp"
    match = re.findall(pattern, str(req.content))
    
    data.update({
        'responce_code': req.status_code,
        'contains': match.__len__() == 0
    })
    req.close()


    return data


def main():
    module = AnsibleModule(
        argument_spec=dict(
            proc=dict(required=True, type='str'),
            url=dict(required=True, type='str'),
            regexp=dict(required=True, type='str')
        )
    )
    proc = module.params["proc"]
    url = module.params["url"]
    regexp = module.params["regexp"]
    proc_info = collect_data_proc(proc)
   # curl_info =

    result = dict(
        msg='',
        changed=False,
        context=proc_info,
        application_url="{}{}".format(url, url)
    )

    module.exit_json(changed=True, result=result)
    module.fail_json(msg="Error getting info", result=result)


if __name__ == '__main__':
    main()


