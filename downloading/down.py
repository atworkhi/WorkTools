import requests
from contextlib import closing
"""
    下载文件并显示进度条
"""


class ProgressBar(object):
    """ 格式化的进度条显示模块 """

    def __init__(self, title, count=0.0, run_status=None, fin_status=None, 
                 total=100.0, unit='', sep='/', chunk_size=1.0):
        super(ProgressBar, self).__init__()
        self.info = "【%s】%s %.2f %s %s %.2f %s"
        self.title = title
        self.total = total
        self.count = count
        self.chunk_size = chunk_size
        self.status = run_status or ""
        self.fin_status = fin_status or " " * len(self.status)
        self.unit = unit
        self.seq = sep

    def __get_info(self):
        # 【名称】状态 进度 单位 分割线 总数 单位
        _info = self.info % (self.title, self.status,
                             self.count/self.chunk_size, self.unit, self.seq, 
                             self.total/self.chunk_size, self.unit)
        return _info

    def refresh(self, count=1, status=None):
        self.count += count
        # if status is not None:
        self.status = status or self.status
        end_str = "\r"
        if self.count >= self.total:
            end_str = '\n'
            self.status = status or self.fin_status
        print(self.__get_info(), end=end_str)


def txtToList(file):
    """获取txt文件中的下载地址"""
    with open(file) as f:
        result = f.read().splitlines()
        return result


def strToList(str):
    """string 按照 制表符 组装成list"""
    result = str.split("\t")
    return result


def downForUrl(name, url):
    """url实现下载并保存"""
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/" +
        "537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    with closing(requests.get(url, headers=header, stream=True)) as response:
        chunk_file_size = 1024  # 单次请求最大值
        content_size = int(response.headers['content-length'])  # 内容体总大小
        progress = ProgressBar(name, total=content_size, unit="KB",
                               chunk_size=chunk_file_size,
                               run_status="downing...",
                               fin_status="Download Over")

        with open(name, 'wb') as f:
            for data in response.iter_content(chunk_size=chunk_file_size):
                f.write(data)
                progress.refresh(count=len(data))


if __name__ == "__main__":
    file = '1.txt'
    list_result = txtToList(file)
    for line in list_result:
        result = strToList(line)
        name = result[0]+"-"+result[1]+".apk"
        downForUrl(name, result[3])
