# _*_coding:utf-8_*_
# ==========================================
#   FileName:Hello.py
#   User: hanxx
#   Date: 2019/9/12
#   Desc: 修改文件名添加apk
# ===========================================
import os


def renanme():
    path = os.path.join(input("请输入文件目录："))
    # 获取列表
    filenames = os.listdir(path)

    for file in filenames:
        oldname = path + '\\' + file
        newname = path + '\\' + file + '.apk'
        try:
            os.rename(oldname, newname)
        except:
            pass


if __name__ == '__main__':
    renanme()
