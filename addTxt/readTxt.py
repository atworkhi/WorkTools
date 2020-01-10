# coding = utf-8
# 把目录下的txt合并成一个txt
import os
import time

date = str(time.strftime('%Y-%m-%d',time.localtime()))

path = os.path.join(input("请输入需要爬取的路径："))
# 获取列表
filenames = os.listdir(path)
# 写入
writeFile = open(date+"-result.txt", 'w', encoding='utf8')

for filename in filenames:
    print(filename+" 写入中....")
    for line in open(path+"\\"+filename, encoding='utf8', errors='ignore'):
        writeFile.writelines(line)
