# TranslateJson

[博客地址](#) | [视频演示](#)

![](https://img.shields.io/badge/TranslateJson-python-green?style=flat&logo=Python) ![](https://img.shields.io/badge/License-AGPL-3.0_License-yellow?style=flat) ![](https://img.shields.io/badge/Version-0.1.0-blueviolet?style=flat)

## 我能干啥？

**调用[百度翻译API](http://api.fanyi.baidu.com/doc/11)** 自定义翻译你的Json文件中的value

## 下载安装

下载release中对应操作系统的版本即可

或

```bash
$ git clone "https://github.com/0ojixueseno0/TranslateJson.git"
$ cd TranslateJson
$ .\TJson.py "example.json or example.yaml"
#或者编译为程序使用
```

## 我咋用它？

```bash
#Windows
$ Tjson.exe example.json
#or
$ Tjson.exe example.yaml
#linux
$ Tjson example.json
#or
$ Tjson example.yaml
```

翻译完毕后会输出为output.json/y(a)ml文件

## 配置文件

```Config.yml```

```yml
Config:
#百度API帮助地址：http://api.fanyi.baidu.com/doc/21
  #API地址默认为百度翻译的通用翻译API
  api_url: "http://api.fanyi.baidu.com/api/trans/vip/translate"
  app_id: #此处填写你的AppID
  secret: "" #此处填写你的密钥
  transfrom: en #从 from 翻译 为 to
  transto: zh
  #不翻译以下列表的字符
  DetranslateList:
  - "&"
  - "*"
  - ":"
  - "!"
  #过滤模式：whitelist 或 blacklist 分别匹配下方的白名单和黑名单
  listmode: whitelist
  #白/黑名单内填写json的key
  Whitelist:
  - Title
  - Thursday
  Blacklist:
  - lore

```

## 后话

大佬走之前点个star吧quq...