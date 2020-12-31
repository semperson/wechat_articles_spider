# coding: utf-8
import os
from pprint import pprint
from wechatarticles import ArticlesAPI
from wechatarticles import tools

if __name__ == '__main__':

    official_cookie = "official_cookie"
    token = "token"
    appmsg_token = "appmsg_token"
    wechat_cookie = "wechat_cookie"

    nickname = "nickname"

    # 手动输入所有参数
    test = ArticlesAPI(official_cookie=official_cookie,
                       token=token,
                       appmsg_token=appmsg_token,
                       wechat_cookie=wechat_cookie)


    # 自定义爬取，每次爬取5篇以上
    data = test.complete_info(nickname=nickname, begin="0")
    print(len(data))
    pprint(data)

    # 自定义从某部分开始爬取，持续爬取，直至爬取失败为止，一次性最多爬取40篇（功能未测试，欢迎尝试）
    datas = test.continue_info(nickname=nickname, begin="0")

    tools.save_json("test.json", data)