import os

Cur_Dir = 'C:\\Users\\Admin\\Desktop\\other\\manyfiles\\'

for url,dirs,files in os.walk(file_url):
    # 遍历文件
    for f in files:
        file_url = os.path.join(url,f)
        file_name = os.path.basename(datainfo['file_url'])
        print("file_url=",file_url)
        print("filename=",file_name)


    # 遍历文件夹
    for d in dirs:
        print(os.path.join(url,d))

data_info = MultipartEncoder(
    fields={
        'parentId':'6405',
        'funcType':'/nc/import_program',
        'paths':'[{"id":"file1","path":"D004918-CC-1"}]',
        'file1':(os.path.basename(file_url),open(file_url,'rb'),'application/octet-stream')
    },
         boundary='-----------------------------' + str(random.randint(1e28, 1e29 - 1))

)