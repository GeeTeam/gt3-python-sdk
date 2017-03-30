# coding:utf-8
import tornado.ioloop
import tornado.web
import tornado.gen
from torndsession.sessionhandler import SessionBaseHandler
from torndsession.session import SessionManager
from sdk import GeetestLib

import json

pc_geetest_id = "48a6ebac4ebc6642d68c217fca33eb4d"
pc_geetest_key = "4f1c085290bec5afdc54df73535fc361"

product = "embed"


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/login.html",)


class PcGetCaptchaHandler(SessionBaseHandler):
    def get(self):
        user_id = 'test'
        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        status = gt.pre_process(user_id,JSON_FORMAT=0,ip_address="127.0.0.1")
        if not status:
            status=2
        self.session[gt.GT_STATUS_SESSION_KEY] = status
        self.session["user_id"] = user_id
        response_str = gt.get_response_str()
        self.write(response_str)


class PcValidateHandler(SessionBaseHandler):
    def post(self):
        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        challenge = self.get_argument(gt.FN_CHALLENGE, "")
        validate = self.get_argument(gt.FN_VALIDATE, "")
        seccode = self.get_argument(gt.FN_SECCODE, "")
        status = self.session[gt.GT_STATUS_SESSION_KEY]
        user_id = self.session["user_id"]
        if status==1:
            result = gt.success_validate(challenge, validate, seccode, user_id,JSON_FORMAT=0)
        else:
            result = gt.failback_validate(challenge, validate, seccode)
            self.session["user_id"] = user_id
        result = "<html><body><h1>登录成功</h1></body></html>" if result else "<html><body><h1>登录失败</h1></body></html>"
        self.write(result)

if __name__ == "__main__":
    app = tornado.web.Application([
                                      (r"/", MainHandler),
                                      (r"/pc-geetest/register", PcGetCaptchaHandler),
                                      (r"/pc-geetest/validate", PcValidateHandler),
                                  ], debug=True)

    app.listen(8088)
    tornado.ioloop.IOLoop.instance().start()
