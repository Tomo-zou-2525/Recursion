# r = 10
# otherSolution = 3.14


# def circleArea(radius):
#     total = r * r * 3.14
#     comparison = total % otherSolution
#     return comparison


# print(circleArea(r))

# r = 100
# otherSolution = 3.14


# def circleArea(radius):
#     return r * r


# print(circleArea(r))

# -*- coding: utf-8 -*-
import subprocess


class Ping(object):
    def __init__(self, hosts):
        for host in hosts:
            # pingコマンド
            ping = subprocess.Popen(["ping", "-c", "1", host],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE
                                    )

            # ping試験
            out, error = ping.communicate()

            # 接続できなかったら
            if error:
                print('[NG]: ' + host + ', Msg->\'' + error.rstrip() + '\'')

            # 接続できたら
            else:
                print('[OK]: ' + host)


# ping試験するホスト
hosts = ['www.google.com', 'algorithm.joho.info', ]

# ping試験
Ping(hosts)
