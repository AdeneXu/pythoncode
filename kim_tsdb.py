# encoding: utf-8

import os
import traceback
import xlrd
import time, datetime
import requests
import json

dir1 = "G:\\DAC\\新版DAC\\AM\\welddata\\582-052"
#dir2 = "G:\\DAC\\新版DAC\\AM\\welddata\\582-093"

#dir_list = [(dir1, "GX100"), (dir2, "GX500")]
dir_list = [(dir1, "GX100")]

s = requests.Session()


def read_file_opne():
    """
        读取目录文件
    """
    try:
        for line in dir_list:
            full_path_in = line[0]
            programe_name = line[1]
            os.chdir(full_path_in)
            for root, dirs, files in os.walk(full_path_in):
                for file_name in files:
                    if os.path.isfile(file_name):
                        file_open(full_path_in, file_name, programe_name)
    except Exception as e:
        traceback.print_exc()


def file_open(full_path_in, file_name, programe_name):
    """
        打开文件
    :return:
    """
    try:
        cond_dicList = []
        print("--------file_open------------")
        print(full_path_in, file_name)
        full_path_in = os.path.join(full_path_in, file_name)
        data = xlrd.open_workbook(full_path_in)
        sheetname = "Sheet1"

        table = data.sheet_by_name(sheetname)
        colnames = table.row_values(1)
        for rownum in range(1, table.nrows):
            row = table.row_values(rownum)
            if row:
                ret = []
                for i in range(len(colnames)):
                    ret.append(row[i])

                timestamp = timestamp_modify(ret[4])

                for num, operation_value in enumerate(["TCP_X", "TCP_Y", "TCP_Z"]):
                    cond_dic = {}
                    tags = {}
                    tags["operationValue"] = operation_value
                    tags["bucketCode"] = int(ret[0])
                    tags["programName"] = programe_name
                    cond_dic["tags"] = tags
                    cond_dic["value"] = ret[num+1]
                    cond_dic["timestamp"] = timestamp
                    cond_dic["metric"] = "194"
                    print(cond_dic)
                    cond_dicList.append(cond_dic)

                weldNoDef = "焊缝编号"
                weldNoDef = weldNoDef.encode('unicode-escape')
                weldNoDef = weldNoDef.replace(b'\\u', b'')
                weldNoDef = weldNoDef.decode('unicode_escape')

                cond_dic = {}
                tags = {}
                tags["operationValue"] =weldNoDef
                cond_dic["tags"] = tags
                cond_dic["value"] = int(ret[0])
                cond_dic["timestamp"] = timestamp
                cond_dic["metric"] = "194"
                print(cond_dic)
                cond_dicList.append(cond_dic)

                if len(cond_dicList) >= 200:
                    send_data_post(cond_dicList)
                    # time.sleep(2)
                    cond_dicList = []

                print(ret)
        send_data_post(cond_dicList)
    except Exception as e:
        print("file_open::::")
        traceback.print_exc()

# insert_5_month = 5*30*24*60*60

def timestamp_modify(timestamp):
    """
        时间戳的值增加4个月
    :param timestamp:
    :return:
    """
    month = int(timestamp[6]) + 5
    timestamp = "2019-0" + str(month) + timestamp[7:]
    print(timestamp)
    time1 = time.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
    startTime = int(time.mktime(time1))
    return startTime


def send_data_post(cond_dicList):
    """
        写入tsdb
    :return:
    """
    try:
#         cond_dicList = [{'metric': '45', 'tags': {'operationValue': 'TCP_Z', 'bucketCode': 9, 'programName': 'GX100'}, 'value': 1281.422, 'timestamp': 1552121189}
# ,{'metric': '45', 'tags': {'operationValue': 'TCP_Y', 'bucketCode': 9, 'programName': 'GX100'}, 'value': 410.4927, 'timestamp': 1552121189},
#                         {'metric': '45', 'tags': {'operationValue': 'TCP_X', 'bucketCode': 9, 'programName': 'GX100'}, 'value': -386.2773, 'timestamp': 1552121189}
# ]
        r = s.post("http://192.168.3.111:4242/api/put", data=json.dumps(cond_dicList))
        if len(r.text) > 0:
            print(r.text)
        else:
            return None
    except Exception as e:
        traceback.print_exc()


if __name__ == "__main__":
    print("---start----")
    read_file_opne()
