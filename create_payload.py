import xlrd
import math
import os

file = "G:\\测试\\10月项目\阈值告警性能测试\\产线1\\cx1-005采集项.xlsx"

payload = []
path = "G:\\测试\\10月项目\阈值告警性能测试\\产线1"
filename_base = "产线1-005"

def read_excel():

    data = xlrd.open_workbook(filename=file)
    sheetname = 'FINS_UDP'
    sheet = data.sheet_by_name(sheetname)

    for rownum in range(1,sheet.nrows):
        row_data = sheet.row_values(rownum)
        if row_data:
            ret = {}
            ret["mach_id"] = "90"
            ret["ip"] = row_data[7]
            ret["address"] = str(row_data[3])
            ret["function_code"] = row_data[2]
            ret["name"] = row_data[0]
            ret["data"] = "0"
            ret["data_type"] = row_data[8]
            ret["time"] = "2019-10-16 10:47:06"
            payload.append(ret)
    t = 0
    payload_100 = []
    mod = len(payload)

    for i in range(0 , math.ceil(len(payload)/100)):

        filename = os.path.join(path, filename_base+"_" + str(i+1) + ".txt")
        if mod > 100:
            for j in range(0, 100):
                payload_100.append(payload[t])
                t = t + 1
        else:
            for j in range(0, mod):
                payload_100.append(payload[t])
                t = t + 1
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(str(payload_100))
            payload_100.clear()
        mod = mod - 100

if __name__ == "__main__":
    read_excel()





