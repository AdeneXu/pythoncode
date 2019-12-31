import requests
import json
from requests_toolbelt import MultipartEncoder
import os,random

url = "http://192.168.3.222:4002/request?rname=i_plc.Page.NcProgram.views.procedure_manage"
# url = "http://localhost:8000/request?rname=i_plc.Page.NcProgram.views.procedure_manage"

header = {
    "Cookie":"sessionid=9u70a991410y3025n9f6hrxg9ev6s2j4;rmbUser=false",
    "Content-Type":"application/x-www-form-urlencoded"
}

# data_info = {
#     "funcType":"/nc/create_program",
#     "name":"folder4",
#     "type":"2",
#     "parentId":"0"
# }

导入文件
# file_url = 'C:\\Users\\Admin\\Desktop\\other\\NC_locale\\DW\\D004918-CC-1'
file_url = 'C:\\Users\\Admin\\Desktop\\other\\NC_locale\\DW'

# 'paths':'[{\"id\":\"file1\",\"path\":\"D004918-CC-2\"}]'



data_info = MultipartEncoder(
    fields={
        'parentId':'6405',
        'funcType':'/nc/import_program',
        'paths':'[{"id":"file1","path":"D004918-CC-1"}]',
        'file1':(os.path.basename(file_url),open(file_url,'rb'),'application/octet-stream')
    },
         boundary='-----------------------------' + str(random.randint(1e28, 1e29 - 1))

)

header["Content-Type"]=data_info.content_type
# """
# -----------------------------41981780627043
# Content-Disposition: form-data; name="parentId"
#
# 6405
# -----------------------------41981780627043
# Content-Disposition: form-data; name="file1"; filename="D000047-2"
# Content-Type: application/octet-stream
#
# %
# O0406(D000047-2)
# G97G99
# M08
# T0101M03S650F0.16
# G0X24Z0
# G1X-1
# G0X18.6Z2
# G1Z0
# X22A-60
# G0X230Z230
# M30
# %
# -----------------------------41981780627043
# Content-Disposition: form-data; name="funcType"
#
# /nc/import_program
# -----------------------------41981780627043
# Content-Disposition: form-data; name="paths"
#
# [{"id":"file1","path":"D000047-2"}]
# -----------------------------41981780627043--
# """

response = requests.post(url=url, data=data_info, headers=header)

print(response.text)
