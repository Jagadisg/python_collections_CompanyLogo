
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,

 would have it's logo with the letters

#!/bin/python3
import math
import ossd
import random
import re
import sys
if __name__ == '__main__':
    s = input()
    dic = {}
    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    sort_dic = dict(sorted(dic.items(),key=lambda pair:pair[1],reverse=True))
    new = dict(sorted(sort_dic.items(),key=lambda item: (-item[1], item[0])))
    j = 1
    for k,v in new.items():
        if j<=3:
            print(k,v)
        else:
            break
        j += 1 
