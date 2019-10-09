# conding:utf-8
# 获取apk信息-名字 md5 签名序号 大小 包名
import os, re
import subprocess
import hashlib
import time

date = str(time.strftime('%Y-%m-%d', time.localtime()))


# 签名
# keytool -printcert -jarfile xxx.apk  获取签名，需要安装jdk
def APPSIGN(file):
    cmd = 'keytool -printcert -jarfile '
    # print(cmd+file)
    p = subprocess.Popen(cmd + file, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE, shell=True)
    (out, err) = p.communicate()
    if out != '':
        try:
            result = str(out, encoding='gbk')
            # print(result)
            # 正则匹配 序列号: 4a92ecc4
            match = re.findall(r'序列号: (\w+)', result)
            return match[0]
        except Exception:
            return ' '
    return ' '


def APPNAME(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if output != '':
        try:
            name = output[19:-2]
            result = str(name, encoding='utf8')
            return result
        except Exception:
            return " "
    return " "


def APPMD5(file):
    m = hashlib.md5()
    with open(file, 'rb') as f:
        for line in f:
            m.update(line)
    md5code = m.hexdigest()

    return md5code


def APPSIZE(file):
    file_byte = float(os.path.getsize(file))
    file_M = file_byte / 1024 / 1024
    return round(file_M, 2)


def APPINFO(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE, shell=True)
    # 将结果按照字符串返回
    # package: name='com.xh.areadunc' versionCode='201' versionName='v1.19.2.20190820'
    (output, err) = p.communicate()
    if output != '':
        try:
            # 通过正则匹配，获取包名，版本号，版本名称
            result = str(output, encoding='utf8')
            match = re.compile(
                "package: name='(\S+)'").match(result)
            packagename = match.group(1)
            return packagename
        except Exception:
            return " "
    return " "


def fileEach(path):
    # 获取列表
    filenames = os.listdir(path)
    return filenames


if __name__ == '__main__':
    cmd = 'aapt.exe dump badging '
    path = input('请输入apk所在的文件夹:')
    list = fileEach(path)
    # 写入
    writeFile = open("F:\\WorkTools\\result\\" + date + "-apkinfo.txt", 'w', encoding='utf8')
    for apk in list:
        apk = path + '\\' + apk
        md5 = APPMD5(apk)
        appname = APPNAME(cmd + apk + ' | grep application-label:')
        appinfo = APPINFO(cmd + apk + ' | grep package')
        appsize = APPSIZE(apk)
        appsign = APPSIGN(apk)
        result = str(md5) + '\t' + str(appname) + '\t' + str(appinfo) + '\t' + str(appsize) + '\t' + str(appsign) + '\n'
        print(apk + " 写入中....")
        writeFile.writelines(result)
