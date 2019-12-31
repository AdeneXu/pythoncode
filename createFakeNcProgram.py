import os

# 桌面路径 windows下要加\\
path = "C:\\Users\\Admin\\Desktop\\NCFile500"

# 如果这个路径不存在就创建这个目录
if not os.path.exists(path):
    os.makedirs(path)

# 从1000到2000
# O+序号+.txt
for index in range(1,500):
    filename = os.path.join(path,"k222k_"+str(index)+".src")
    with open(filename,'w',encoding="utf-8") as f:
        f.write("this is test code!\nthis is test code!\nthis is test code!\n") 

