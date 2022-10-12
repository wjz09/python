"""
coding:utf-8
@Software:PyCharm
@Time:2022/10/3 13:50
@Author:WangDengdeng
"""
import requests

url = 'https://wallhaven.cc/'
headers = {
    # 'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.wikipedia.org/',
    'Connection': 'keep-alive',
}
response =requests.get(url).headers
print(response)
print('hahaha')