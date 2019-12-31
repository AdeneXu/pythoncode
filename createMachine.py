import requests
import pytest
import xlrd

dac_url = 'http://119.3.64.173:7777'

url = dac_url + '/tm/new_ncdevice'
token = "4ba0cf18e1e05119c4cb0ff12b2ecd9392061caf"
#gateMac = "9C:5C:8E:8F:D1:D2"
gateMac = "00:E0:4C:36:01:25"
gateType = "GW_AR"

filename = "C:\\Users\\Admin\\Desktop\\other\\shareFolder_url.xlsx"

def createFTPMachine():
    for n in range(1,21):
        deviceName = "FTP" + str(n)
        deviceCode = "1226-F-" + "%03d" % n
        ftpDir = "C:\FTPServer\\" + str(n)
        ftpUserName = "CNC" + str(n)

        send_info = {
            'token': token,
            'gateMac': gateMac,
            'gateType': gateType,
            'deviceName': deviceName,
            'deviceCode': deviceCode,
            'deviceDesc': "",
            'ftpDir': ftpDir,
            'ftpUserName': ftpUserName,
            # 'type': type
            'dirType': "ftp",
            }

        response = requests.post(url=url, data=send_info)

        print("第%s个 " % str(n)+"===============")
        print(response.json())

        assert response.status_code == 200

def createShareMachine():
    ftpdir = []
    ftpDir_data = xlrd.open_workbook(filename)
    tables = ftpDir_data.sheets()[0]

    ftpdir = tables.col_values(0, start_rowx=0, end_rowx=tables.nrows)

    for n in range(1,76):
        deviceName = "Share" + str(n)
        deviceCode = "1226-S-" + "%03d" % n

        send_info = {
            'token': token,
            'gateMac': gateMac,
            'gateType': gateType,
            'deviceName': deviceName,
            'deviceCode': deviceCode,
            'deviceDesc': "",
            'ftpDir': ftpdir[n-1],
            'ftpUserName': None,
            # 'type': type
            'dirType': "share",
            "machineIndex":n
            }

        response = requests.post(url=url, data=send_info)

if __name__ == "__main__":
    createFTPMachine()
    createShareMachine()