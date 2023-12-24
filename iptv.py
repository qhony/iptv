import requests
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import random
import time
import re

# 检查单个直播流是否有效的函数
def check_stream(name_url_pair):
	# 分离出频道名称和URL
    name, url = name_url_pair  

    # 设置HTTP请求头，伪装成浏览器
    headers = {'User-Agent': 'Mozilla/5.0 ... Chrome/58.0.3029.110 Safari/537.3'}
    try:
	    # 向URL发送请求
        response = requests.get(url, headers=headers, timeout=10)  

        # 随机延时，模拟人类用户
        time.sleep(random.randint(1, 2))  

        # 检查响应状态码，判断是否有效
        if response.status_code == 200:
            print(f"{name}: 有效")
            # 将有效的流写入文件，请自行修改名称。
            with open('有效的源-2.m3u', 'a', encoding='utf-8') as f:
                f.write(f"{name},{url}\n")
            return True
        else:
            print(f"{name}: 无效")
            return False
    except requests.RequestException:
        print(f"{name}: 无效")
        return False

# 检查多个直播流
def check_streams(name_url_pairs, max_workers=100):
    # 使用线程池并行处理
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # tqdm显示进度条
        list(tqdm(executor.map(check_stream, name_url_pairs), total=len(name_url_pairs)))

# 从M3U文件读取并解析每个直播流的名称和URL
def read_m3u_file(file_path):
    name_url_pairs = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # 正则表达式匹配频道名称
            if line.startswith('#EXTINF'):
                match = re.search(r'tvg-id="([^"]+)"', line)
                if match:
                    current_name = match.group(1)
            # 获取URL
            elif line.startswith('http'):
                url = line.strip()
                name_url_pairs.append((current_name, url))
    return name_url_pairs

# 主程序执行
m3u_file_path = 'index.nsfw.m3u'  # M3U文件路径，请自行修改源文件。
name_url_pairs = read_m3u_file(m3u_file_path)  # 读取并解析M3U文件
check_streams(name_url_pairs)  # 检查并输出有效的直播流
