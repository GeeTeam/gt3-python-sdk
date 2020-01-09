# Gt3 Python SDK

# 概述

> 行为验证 Python SDK目前提供基于`Flask`、`Tornado`、`Django`框架的demo。

## 开发环境

|条目||
|----|------|
|python环境 | python3，建议python3.5|
|依赖库|Web框架库（如`django`、`tornado`）等<br>您可以使用`pip3 install -r requirements.txt` 一键安装所有依赖|

## 资源导航

|条目||
|-------------|--------------|
|产品结构流程|[通讯流程](/install/overview/flowchart/#通讯流程)|
|SDK项目地址|[gt3-python-sdk](http://github.com/GeeTeam/gt3-python-sdk)|

# 安装 Python SDK

## 下载SDK

> 使用命令从Github导入完整项目

```
git clone https://github.com/GeeTeam/gt3-python-sdk.git
```

> 手动下载压缩包文件

从[Github: gt3-python-sdk](https://github.com/GeeTeam/gt3-python-sdk/archive/master.zip)下载`.zip`文件

## 下载pip依赖

> 各框架demo路径中有requirements.txt文件，使用pip3一键安装

```
pip3 install -r requirements.txt
```

## 配置密钥，修改请求参数

> 配置密钥

从[极验管理后台](https://account.geetest.com/login)获取您的公钥（id）和私钥（key）, 并在代码中配置。配置文件路径如下：
- Django：`/demo/django_demo/app/views.py`
- Flask：`/demo/flask_demo/start.py`
- Tornado：`/demo/tornado_demo/start.py`

> 修改请求参数（可选）

名称|说明
----|------
user_id|user_id作为终端用户的唯一标识，确定用户的唯一性；作用于提供进阶数据分析服务，可在api1 或 api2 接口传入，不传入也不影响验证服务的使用；若担心用户信息风险，可作预处理(如哈希处理)再提供到极验 ；
client_type|客户端类型，**web**（pc浏览器），**h5**（手机浏览器，包括webview），**native**（原生app），**unknown**（未知）
ip_address|客户端请求您服务器的ip地址，**unknow**表示未知

# 运行 demo

> 您也许需要使用`sudo`命令才能执行下列命令

### Flask demo 运行

>命令行进入flask_demo文件夹路径，执行命令：

```
$ python3 start.py
```

在浏览器中访问`http://localhost:5000`即可看到demo界面。

### Tornado demo运行

> 命令行进入tornado_demo文件夹路径，执行命令:

```
$ python3 start.py
```

在浏览器中访问`http://localhost:8088`即可看到demo界面

### Django demo运行

> 命令行进入django_demo文件夹路径，执行命令:

```
$ python3 manage.py runserver 0.0.0.0:8000
```

在浏览器中访问`http://localhost:8000`即可看到demo界面


发布日志
-----------------
+ 3.4.0

  - 优化包结构
  - 整理代码失效链接
  - 升级新版failback表现形式

+ 3.3.2
  
  - 去掉代码和文档中的已失效的链接

+ 3.3.1

  - 保持 sdk 包名和导入名保持一致, geetest.

+ 3.3.0

  - 保持 sdk 包名和导入名保持一致, geetest.

+ 3.2.0

  - 添加用户标识(user_id)的接口

+ 3.1.2

  - 支持Python3

+ 3.1.1

  - 统一接口

+ 3.1.0

  - 添加challenge加密特性，使验证更安全， 老版本更新请先联系管理员

+ 3.0.1

  - 修复failback情况下 无法正确解码答案的错误

+ 3.0.0

  - 去除SDK对Session操作， 现在Session部分由开发者自己处理
  - 简易化初始化过程.
  - 修复failback模式BUG