#!/usr/bin/env python
#_*_coding:utf-8_*_
import requests   #http请求包
import json       #json解析包
from urllib.parse import quote

import yaml       #配置文件解析包: pyyaml
import random     #随机数包
import hashlib    #MD5加密包
import time       #延时包
import sys        #参数包

try:
  f = open("config.yml",'r',encoding='utf-8')
  f.close()
except FileNotFoundError:
    print("[!]提示：未找到配置文件 生成默认配置文件中")
    f = open("config.yml",'w',encoding='utf-8')
    f.write(
      "Config:\n"
      "#百度API帮助地址：http://api.fanyi.baidu.com/doc/21\n"
      "  #API地址默认为百度翻译的通用翻译API\n"
      '  api_url: "http://api.fanyi.baidu.com/api/trans/vip/translate"\n'
      '  app_id: #此处填写你的AppID\n'
      '  secret: "" #此处填写你的密钥\n'
      '  transfrom: en #从 from 翻译 为 to\n'
      '  transto: zh\n'
      '  #不翻译以下列表的字符\n'
      '  DetranslateList:\n'
      '  - "&"\n'
      '  - "*"\n'
      '  - ":"\n'
      '  - "!"\n'
      "  #过滤模式：whitelist 或 blacklist 分别匹配下方的白名单和黑名单\n"
      "  listmode: whitelist\n"
      "  Whitelist:\n"
      "  - lore\n"
      "  Blacklist:\n"
      "  - lore\n"
    )
    f.close()
except PermissionError:
  print("[*]错误 ==> 没有权限访问配置文件！请检查程序权限\n\t|| (?)尝试使用管理员权限打开程序")


#载入配置文件
f = open("config.yml",'r',encoding='utf-8')

config = yaml.load(f.read(), Loader=yaml.FullLoader)

api_url = str(config['Config']['api_url'])
app_id = str(config['Config']['app_id'])
secret = str(config['Config']['secret'])
detrans = config['Config']['DetranslateList']
transfrom = str(config['Config']['transfrom'])
transto = str(config['Config']['transto'])
whitelist = config['Config']["Whitelist"]
blacklist = config['Config']["Blacklist"]
listmode = str(config['Config']['listmode'])

jsonpath = ""

def error_code_parse(code):
  if code == "52001":
    return "请求超时 请检查你的网络"
  elif code == "52002":
    return "系统错误 请重试"
  elif code == "52003":
    return "未授权用户 请检查您的appid是否正确，或者服务是否开通"
  elif code == "54000":
    return "缺少必填参数 检查你的配置文件"
  elif code == "54001":
    return "签名错误 请检查您的签名生成方法"
  elif code == "54003":
    return "访问频率受限 请降低您的api调用频率"
  elif code == "54004":
    return "账户余额不足 请前往管理控制台为账户充值"
  elif code == "54005":
    return "长query请求频繁 请降低长query的发送频率，3s后再试"
  elif code == "58000":
    return "客户端IP非法 检查个人资料里填写的IP地址是否正确，可前往开发者信息-基本信息修改"
  elif code == "58001":
    return "译文语言方向不支持 检查译文语言是否在语言列表里"
  elif code == "58002":
    return "服务当前已关闭 请前往管理控制台开启服务"
  elif code == "90107":
    return "认证未通过或未生效 请前往我的认证查看认证进度"

def translate(untrans):
  if untrans == "":
    return untrans
  else:
    global api_url, app_id, secret, detrans, transfrom, transto
    salt = str(random.randint(1000000000,9999999999))
    repcode = random.randint((len(detrans) + 20) ** 3,(len(detrans) + 20) ** 4)
    _repcode = repcode
    print("[↑]原文：" + untrans)
    _u_untrans = untrans
    for i in detrans:
      untrans = untrans.replace(i,str(_repcode))
      _repcode = _repcode + 1
    final_sign = app_id + untrans + salt + secret
    final_sign = hashlib.md5(final_sign.encode(encoding='UTF-8')).hexdigest()
    my_url = api_url + '?appid=' + app_id + '&q=' + untrans + '&from=' + transfrom + '&to=' + transto + '&salt=' + salt + '&sign=' + final_sign
    result = requests.get(my_url,params={},headers={},)
    # print(result.text)
    if "error_code" not in json.loads(result.text).keys():
      output = json.loads(result.text)["trans_result"][0]["dst"]
      _repcode = repcode
      for i in detrans:
        output = output.replace(str(_repcode), i)
        _repcode = _repcode + 1
    else:
      error_msg = error_code_parse(str(json.loads(result.text)["error_code"]))
      print("[*]错误 ==> 翻译 " + _u_untrans + " 时出现了错误\n\t|| 错误信息：" + str(error_msg))
      output = untrans
    print("[↓]译文：" + output)
    time.sleep(1)
    return output.encode('unicode_escape').decode('unicode_escape')

def saveFile (input):
  saveFile = open("output.json", "w", encoding='utf-8')
  saveFile.write(json.dumps(input,indent=4,ensure_ascii=False))
  saveFile.close()

# def list_parse(input):
#   if isinstance(input, list):
#     _elementnum = 0
#     for element in list:
#       if listinput[_elementnum]
#       _elementnum = _elementnum +1

def json_txt(dic_json):
  # print(type(dic_json))
  if isinstance(dic_json,dict):
    # print(type(dic_json))
    for key in dic_json:
      # print(key)
      if (key in whitelist and listmode == "whitelist") or (key not in blacklist and listmode == "blacklist"):
      # if isinstance(dic_json[key],dict):
        # print("*"*30)
        if isinstance(dic_json[key],list):
          _elementnum = 0
          for element in dic_json[key]:
            dic_json[key][_elementnum] = translate(str(element))
            _elementnum = _elementnum + 1
        else:
          dic_json[key] = translate(str(dic_json[key]))
      elif isinstance(dic_json[key],dict) or isinstance(dic_json[key],list):
        json_txt(dic_json[key])
      # elif isinstance(dic_json[key],list):
      #   json_txt(dic_json[key])
  elif isinstance(dic_json,list):
    # print("\n************\n")
    _elementnum = 0
    for element in dic_json:
      # print(str(type(dic_json[_elementnum])) + "\n")
      # for i in dic_json[key][_elementnum]:
      #   print(i)
      json_txt(dic_json[_elementnum])
      _elementnum = _elementnum + 1



if len(sys.argv) == 2:
  jsonpath = sys.argv[1]

elif len(sys.argv) == 1:
  print("[*]错误 ==> 你需要提供需要翻译的文件地址\n\t||usage: *.py/*.exe 'test.json'")
  sys.exit()
else:
  print("[*]错误 ==> 请检查文件地址是否正确\n\t||usage: *.py/*.exe 'test.json'\n\t||文件地址带空格的请使用英文引号括起来")
  sys.exit()

f = open(jsonpath,'r',encoding='utf-8')

# print(f.read())
jsons = json.loads(f.read())
# print(jsons)

json_txt(jsons)

# print(jsons)

saveFile(jsons)

print("|-> 机翻完毕 请检查output.json的内容\n| =: Translate completed. Please Check 'output.json'")