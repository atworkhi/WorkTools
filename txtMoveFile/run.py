# _*_coding:utf-8_*_
# ==========================================
#   FileName:Hello.py
#   User: hanxx
#   Date: 2019/9/12
#   Desc: python 根据txtmd5 查找移动文件
# ===========================================
#
import shutil


# 按行读取并存入list
def readTxtLine(file):
    with open(file, 'r') as f:
        content = f.read().splitlines()
        return content


# 移动文件
def moveFile(oldpath, newpath):
    try:
        shutil.move(oldpath, newpath)
    except Exception:
        pass


if __name__ == '__main__':
    file = 'md5.txt'
    md5 = readTxtLine(file)
    old = input('请输入源路径：')
    new = input('请输入新路径：')
    for f in md5:
        print('移动:' + f)
        moveFile(old + "\\" + f + '.apk', new + '\\' + f + '.apk')
