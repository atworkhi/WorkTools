# 遍历目录下的目录文件放到指定目录下
import os
import shutil

root = input("请输入源路径：")
newpath = input("请输入目的路径：")


def moveFile(oldpath, newpath):
    try:
        shutil.move(oldpath, newpath)
    except Exception:
        pass


def fileEach(root):
    files = os.listdir(root)
    for fi in files:
        dirfile = os.path.join(root, fi)
        if os.path.isdir(dirfile):
            fileEach(dirfile)
        else:
            filepath = os.path.join(root, dirfile)
            print(os.path.join(root, dirfile))

            moveFile(filepath, newpath)


if __name__ == "__main__":
    fileEach(root)
