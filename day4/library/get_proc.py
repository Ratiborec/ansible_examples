#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from __future__ import absolute_import, division, print_function
__metaclass__ = type
from ansible.module_utils.basic import *
from subprocess import *
import requests
import re
import psutil

DOCUMENTATION = r''' 
---
module: get_proc 
version_added: "0.0.1" 
short_description: my first ansible module 
description: 
  - module for getting pid,listning port and regex matchin in headers and content for process
author: 
  - "Mikhail Znak" 
''' 


def collect_data_proc(proc):
    data = []
    try:
        pids = subprocess.check_output(["pidof", proc]).rstrip().split(" ")
    except Exception:
        return data

    for con in psutil.net_connections('all'):
        if con.status == "LISTEN" and str(con.pid) in pids:
            tmp = {
                "proccess": proc,
                "user": subprocess.Popen(['ps', '-o', 'user=', '-p', str(con.pid)], stdout=subprocess.PIPE).communicate()[0],
                "pid": con.pid,
                "port": con.laddr.port 
            }
            data.append(tmp)

    return data


def collect_curl_data(url, con, head):
    data = {}
    try: 
        req = requests.get(url)
    except Exception:
        return data
    
    match_con = re.findall(re.template(con), str(req.content))
    p = subprocess.Popen(["curl", "-ILs", url], stdout=subprocess.PIPE)
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
            regexp_head=dict(required=True, type='str')
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
    )

    module.exit_json(changed=False, result=result)
    module.fail_json(msg="Error getting info", result=result)


if __name__ == '__main__':
    main()
