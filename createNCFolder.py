import os
import random
import time

#path = "G:\\NC程序"
suffix = ['src','pgf','mod','txt','dat','nc']

#创建文件夹
dir = 'G:\\NC程序\\NCDir'

#创建文件
for i in range(2,10):
   new_dir = dir + str(i)
   if not os.path.exists(new_dir):
       os.makedirs(new_dir)
   print("第%s个文件夹名称 %s" %(str(i),new_dir))
   for j in range(1,201):
       filename = os.path.join(new_dir,"NCFile"+str(j)+"."+random.choice(suffix))
       with open('G:\\NC程序\\NC_all\\gai_500kv_6.src','r') as f1:
           with open(filename,'w',encoding="utf-8") as f2:
               f2.write(f1.read())
           print("生成文件个数 %s,文件名称：%s" %(str(j),filename))
   dir = new_dir + "\\NCDir"




