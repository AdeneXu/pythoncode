# coding:utf-8
file = '..\\txt_graph\\log_file\\error.log'

nc_time = []
summ = 0.0
with open(file, 'r', encoding='utf-8') as f:
    for line in f.readlines():

        nc_time.append(line.split()[9].split('秒')[0])

nc_time = list(map(float, nc_time))
for i in nc_time:
    summ += i
print(summ)