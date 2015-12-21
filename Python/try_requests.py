# encoding: utf-8

import requests

def read_response():
    # Request的HTTP请求，获取到一个Response对象
    # r = requests.post("http://httpbin.org/post")
    # r = requests.put("http://httpbin.org/put")
    # r = requests.delete("http://httpbin.org/delete")
    # r = requests.head("http://httpbin.org/get")
    # r = requests.options("http://httpbin.org/get")

    #获取github的公共时间线
    r = requests.get('https://api.github.com/users/octocat/orgs')
    print(r.headers) #服务器响应头
    print(r.text)  #响应内容文字
    print(r.encoding)  #响应内容的编码
    print(r.content) #响应内容
    print(r.json()) #采用内置JSON解码器解析JSON内容，返回一个dict
    print(r.raw)  #原始响应内容

def put_params_to_url():
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get('http://httpbin.org/get', params = payload)
    print(r.url)

#put_params_to_url()
read_response()


