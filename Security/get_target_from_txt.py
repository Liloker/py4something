import launch_poc
import time
import concurrent.futures


def run_poc(ip_port, timeout_seconds):

    # 函数用于执行Poc测试
    try:
        start_time = time.time()
        launch_poc.poc_post(ip_port)
        end_time = time.time()
        elapsed_time = end_time - start_time
        if elapsed_time > timeout_seconds:
            print("等待时间超过10秒，跳过该目标")
    except Exception as e:
        print(f"发生异常：{e}")


def get_ipport_from_txt():
    # 打开文件并读取数据
    with open('xaws.site.mmxaws8888-10000.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 提取IP:Port数据并存储在列表中
    ip_port_list = [line.split()[0] for line in lines if line.strip()]

    # 获取列表中的数据（每次获取10个）
    batch_size = 10  # 每次获取的数量
    timeout_seconds = 2  # 设置超时时间（秒）
    workers = 10  # 设置线程数

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        start_index = 100  # 开始索引
        while start_index < len(ip_port_list):
            batch = ip_port_list[start_index:start_index + batch_size]
            print('开始', start_index, '到第', start_index + 10, '', batch)

            # 对每批batch进行poc验证,限制10个线程
            for index, ip_port in enumerate(batch, start=1):  # batch[8:10] 左闭右开，从0开始
                # print(f"开始测试第 {index} 个结果: {ip_port}")
                # 使用线程来执行Poc测试，设置超时时间
                executor.submit(run_poc, ip_port, timeout_seconds)

            time.sleep(3)  # 暂停10s让并发线程好看些
            start_index += batch_size


if __name__ == '__main__':
    get_ipport_from_txt()
