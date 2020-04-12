
def getPotentialDomains(lines):
    # Write your code here    
    for url in lines:
        url = url.replace("http://",'')
        url = url.replace("https://",'')
        url = url.replace("www.",'')
        url = url.split("/", 1)[0]
        print(url)
    return None

print(getPotentialDomains(['http://hackerrank.com/contest','http://www.hackerrank.com/contest']))



#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getPotentialDomains' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY lines as parameter.
#

def getPotentialDomains(lines):
    # Write your code here    
    ls = []
    for url in lines:
        print(url)
        newUrl = ""
        if "http://" in url or "https://" in url:
            newUrl = url[:url.find("http://")]
            newUrl = url.replace("http://",'')
            newUrl = newUrl.replace("https://",'')
            newUrl = newUrl.replace("www.",'')
            newUrl = newUrl.split("/", 1)[0]
        if newUrl not in ls and newUrl != "":
            ls.append(newUrl)
    sorted(ls)
    domain = ""
    for x in ls:
        domain += x + ";" 
    return domain

    for url in lines:
        newUrl = ""
        if "http://" in url or "https://" in url:
            newUrl = url[:url.find("http://")]
            newUrl = newUrl[:newUrl.find("https://")]
            newUrl = newUrl.replace("http://",'')
            newUrl = newUrl.replace("https://",'')
            newUrl = newUrl.replace("www.",'')
            newUrl = newUrl.split("/", 1)[0]
        if newUrl not in ls and newUrl != "":
            ls.append(newUrl)
    sorted(ls)
    domain = ""
    for x in ls:
        domain += x + ";" 
    return domain

import re
n = int(input())
html = ''
for _ in range(n):
    html += input()

links = set(re.findall(r"https?://(?:www\.|ww2\.|)([\w\-]+(?:\.[\w\-]+)+)+[/\?\"]", html))
print(';'.join(list(sorted(links))))



    regEx = r'''(?:(?:"|'|=)http(?:s?):\/\/)(?:www\.)?([-a-zA-Z0-9\.]*)(?=\/|\?|")'''


"https?://(?:www\.|ww2\.|)([\w\-]+(?:\.[\w\-]+)+)+[/\?\"]"

    "http[s]?:\\/\\/(ww[w2]\\.)?(([a-zA-Z0-9\\-]+\\.)+([a-zA-Z\\-])+)"


import re


regex = r'''(?:(?:"|'|=)http(?:s?):\/\/)(?:www\.)?([-a-zA-Z0-9\.]*)(?=\/|\?|")'''

pattern = re.compile( regex )

if __name__ == '__main__':

    domain_list = []

    n = int( input() )

    for _ in range(n):

        input_str = input()

        result = re.findall( pattern, input_str )

        result = list( dict().fromkeys( result ) )

        domain_list += [ domain for domain in result if domain not in domain_list and domain.count('.') != 0 ]

    
    domain_list.sort()

    output_str = ';'.join( domain_list )

    print( output_str )