极验验证
========
极验行为验证是一款可以帮助你的网站与 APP 应用识别与拦截机器程序批量自动化操作的SaaS应用。它是由极验开发的
新一代人机验证产品，它不基于传统“问题-答案”的检测模式，而是通过利用深度学习对验证过程中产生的行为数据进行
高维分析，发现人机行为模式与行为特征的差异，更加精准地区分人机行为。


集成流程
--------
行为验证的整个集成流程是顺序进行的，业务层主要涉及到客户端和服务端的部署，在下一个步骤开始前请确保上一个
步骤的检查点都已经正确完成；请开发者严格按照步骤进行。

步骤:  注册极验账户(1) 一 登录极验后台(2) 一 注册验证 ID 和 Key (3) 一 配置ID属性(4) 一 集成服务端代码(5) 一 
	   集成客户端代码(6) 一 服务上线(7) 一 数据上线(8) 一 登录后台查看数据(9)


新手指南
--------
0. 产品概述 - https://docs.geetest.com/install/overview/prodes/
1. 入门指引 - https://docs.geetest.com/install/overview/beginner/


文档导航
--------
* 部署指引 - https://docs.geetest.com/install/overview/guide
* 数据通讯流程 - https://docs.geetest.com/install/overview/flowchart
* 服务的部署 - https://docs.geetest.com/install/deploy/server/python
* 客户端部署 - https://docs.geetest.com/install/deploy/client/web
* 名词解释 - https://docs.geetest.com/install/help/glossary
* 常见问题 - https://docs.geetest.com/install/help/faq


联系我们
--------
* 官网： www.geetest.com        	
* 技术支持邮箱：service@geetest.com        
* 技术支持电话：400-8521-816    
* 联系商务邮箱：cooperation@geetest.com     
* 联系商务电话：13720157161    


Gt Python SDK
===============
使用 3.1 之前版本SDK的用户如果想更新到3.1以及以后版本请先联系极验客服,因为为了兼容老用户,新的特性需要修改验证设置。

极验验证的Python SDK目前提供基于django, flask, tornado框架的DEMO。

本项目是面向服务器端的，具体使用可以参考我们的 `文档 <http://www.geetest.com/install/sections/idx-server-sdk.html>`_ ,客户端相关开发请参考我们的 `前端文档。 <http://www.geetest.com/install/>`_.

**注意事项：部署在生产环境中时，需要将gt.js文件存放到项目中并在页面中引用该文件。该js的作用是充分利用多CDN，使静态文件尽可能加载成功。**

开发环境
----------------

 - Python (推荐2.7.0以上版本）
 - django, flask, tornado框架

快速开始
---------------

下面使用示例代码的均以flask框架为例。

1. 获取代码

从 `Github <https://github.com/GeeTeam/gt-python-sdk/>`__ 上Clone代码:

.. code-block:: bash

    $ git clone https://github.com/GeeTeam/gt-python-sdk.git

2. 安装GeetestSDK

.. code-block:: bash

    $ sudo python setup.py install

3. 初始化验证


在调用GeetestLib前请自行设定公钥和私钥,用户id为可选项，默认为随机数字：

.. code-block :: python

  captach_id = "你的公钥"
  private_key = "你的私钥"
  user_id = random.randint(1,100)

根据自己的私钥初始化验证

.. code-block :: python

  @app.route('/getcaptcha', methods=["GET"])
  def get_captcha():
      user_id = random.randint(1,100)
      gt =  GeetestLib(captcha_id, private_key)
      status = gt.pre_process(user_id)
      session[gt.GT_STATUS_SESSION_KEY] = status
      session["user_id"] = user_id
      response_str = gt.get_response_str()
      return response_str

4. 二次验证

.. code-block :: python

  @app.route('/validate', methods=["POST"])
  def validate_capthca():
      gt = GeetestLib(captcha_id, private_key)
      status = session[gt.GT_STATUS_SESSION_KEY]
      challenge = request.form[gt.FN_CHALLENGE]
      validate = request.form[gt.FN_VALIDATE]
      seccode = request.form[gt.FN_SECCODE]
      user_id = session["user_id"]
      if status:
          result = gt.success_validate(challenge, validate, seccode, user_id)
      else:
          result = gt.fail_validate(challenge, validate, seccode)
      result = "success" if result else "fail"
      return result


运行demo
---------------------

1. django demo运行：进入django_demo文件夹，运行：

.. code-block:: bash

    $ python manage.py runserver 0.0.0.0:8000

在浏览器中访问http://localhost:8000即可看到Demo界面

2. flask demo运行：进入flask_demo文件夹，运行：

.. code-block:: bash

    $ python start.py

在浏览器中访问http://localhost:5000即可看到Demo界面

3. tornado demo运行：进入tornado_demo文件夹，运行:

.. code-block:: bash

    $ python start.py

在浏览器中访问http://localhost:8088即可看到Demo界面


发布日志
-----------------
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
