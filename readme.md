# TranslateJson

[Blog Post](#) | [BilibiliVideo(zh)](#) | [中文readme](https://github.com/0ojixueseno0/TranslateJson/blob/master/readme_zh.md)

![](https://img.shields.io/badge/TranslateJson-python-green?style=flat&logo=Python) ![](https://img.shields.io/badge/License-GNU_Affero_GPL-yellow?style=flat) ![](https://img.shields.io/badge/Version-0.1.0-blueviolet?style=flat)

## How Can i do？

**Use [Baidu Translation API](http://api.fanyi.baidu.com/doc/11)** Customize translate your value in json file

## Download

Download the version that matches your system in the release

Or you can run:

```bash
$ git clone "https://github.com/0ojixueseno0/TranslateJson.git"
$ cd TranslateJson
$ .\TJson.py example.json
#Or compiled as a program to use
```

## How to use？

```bash
#Windows
$ Tjson.exe example.json
#linux
$ Tjson example.json
```

When it completed, you will find a file named ```output.json``` with result

## Configure File

```Config.yml```

```yml
Config:
#Help of Baidu-Trans API：http://api.fanyi.baidu.com/doc/21
  #Default address is Baidu-Trans general API
  api_url: "http://api.fanyi.baidu.com/api/trans/vip/translate"
  app_id: #Fill in your AppID here
  secret: "" #Fill in your key here
  transfrom: en #from "from" trans to "to"
  transto: zh
  #program will not translate the chars in the list
  DetranslateList:
  - "&"
  - "*"
  - ":"
  - "!"
  #Filter mode：whitelist/blacklist will Match the whitelist and blacklist list below
  listmode: whitelist
  #put the key of json in the list
  Whitelist:
  - Title
  - Thursday
  Blacklist:
  - lore

```

## At last

Click the ```star``` button pls !!!
