# _*_coding:utf-8_*_
# ==========================================
#   FileName:Hello.py
#   User: hanxx
#   Date: 2019/9/12
#   Desc: 腾讯在线查找MD5
# ===========================================

import urllib.request, urllib.parse, urllib.error
import json

# https://m.qq.com/security_lab/scans_online.jsp
# https://m.qq.com/security_lab/scans_online.jsp
# https://m.qq.com/security_lab/check_result_json.jsp
index_url = 'https://m.qq.com/security_lab/check_state_json.jsp'
real_url = 'https://m.qq.com/security_lab/check_result_json.jsp'

header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
# 保持会话
openurl = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())

# 创建文件保存结果
txt = open('result.txt', 'wb')


# 检测结果
def scan_resp(data):
    try:
        req = urllib.request.Request(real_url, data=urllib.parse.urlencode(data).encode(encoding='UTF8'),
                                     headers=header)
        resp = openurl.open(req)
        json_data = json.loads(resp.read().decode("UTF8"))['info']
        softName = json_data['softName']
        conclusion = json_data['conclusion']
        try:
            virusName = json_data['virusName']
            virusDesc = json_data['virusDesc']
        except Exception:
            virusName = 'null'
            virusDesc = 'null'
        result = u"%s\t%s\t%s\t%s\t%s\n" % (data['data'], softName, virusName, virusDesc, conclusion)
        return result
    except urllib.error.URLError as ue:
        print(ue)
    except urllib.error.HTTPError as he:
        print(he)


# 访问请求 保持会话
def scan_req(data):
    try:
        req = urllib.request.Request(index_url, data=urllib.parse.urlencode(data).encode(encoding='UTF8'),
                                     headers=header)
        resp = openurl.open(req)
        json_data = json.loads(resp.read().decode("UTF8"))
        # print(json_data)
        result = json_data['result']
        if result == '1':
            # 获取真实检测地址
            check = scan_resp(data=data)
            print(check)
            txt.write(check.encode('utf8'))
        else:
            print('no result')

    except urllib.error.URLError as ue:
        print(ue)
    except urllib.error.HTTPError as he:
        print(he)


# 获取文件md5
# 按行读取并存入list
def readTxtLine(file):
    with open(file, 'r') as f:
        content = f.read().splitlines()
        return content


if __name__ == '__main__':
    file = 'md5.txt'
    md5List = readTxtLine(file)
    for md5 in md5List:
        data = {
            "type": "md5",
            "data": md5
        }
        scan_req(data)
    print('检测结束')
