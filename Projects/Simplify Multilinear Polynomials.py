# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 21:55:16 2019

@author: Gary Tablet
"""
poly = "+n-5hn+7tjhn-4nh-3n-6hnjt+2jhn+9hn"

"""Solution transforms subtraction to addition. This allows for the communitive 
property of addition. It uses a pandas dataframe to aggregate the coefficients,
converts it to a list, and joins the list in a polynomial.

"""
import re
import pandas as pd

reg_nums = re.compile(r'[\+\-]?[0-9]+')

def simplify(poly):
    poly_parts = [char for char in poly]
    mon_list = []
    nums = []
    chars = []
    mon_parts = []
    polynom = []

    if poly_parts[0] == "-" and poly_parts[1].isdigit() == False:
        poly_parts[0] = -1
    elif poly_parts[0].isalpha() == True:
        poly_parts.insert((0), 1)
    
    for i in range(len(poly_parts)):
        if poly_parts[i] == "-" and poly_parts[i+1].isdigit() == True:
            poly_parts[i] = "+"
            poly_parts[i + 1] = int(poly_parts[i+1]) * -1
        elif poly_parts[i] == "-" and poly_parts[i+1].isdigit() == False:
            poly_parts[i] = "+"
            poly_parts.insert((i+1), -1)
        elif poly_parts[i] == "+" and poly_parts[i+1].isdigit() == True:
            poly_parts[i] = "+"
            poly_parts[i + 1] = int(poly_parts[i+1])
        elif poly_parts[i] == "+" and poly_parts[i+1].isdigit() == False:
            poly_parts[i] = "+"
            poly_parts.insert((i+1), 1)   
            
    poly = "".join(map(str, poly_parts))
    
    nums = [int(k) for k in reg_nums.findall(poly)]

    mon_list = poly.split('+')
    
    while("" in mon_list) : 
        mon_list.remove("") 
    
    for i in range(len(mon_list)):
        mon_parts.append([nums[i], ''.join(filter(str.isalpha, mon_list[i]))])
        chars.append(''.join(filter(str.isalpha, sorted(mon_list[i]))))
              
    chars = list(set(chars))
    
    for item in mon_parts:
        #item.sort(key=len)
        item[1] = ''.join(sorted(item[1])) 
        
    #mon_parts = mon_parts.sort(key=lambda x: x[1])
  
    df = pd.DataFrame(mon_parts, columns = ['coeff', 'vari'])
    
    df = df.groupby(['vari'], as_index=False).sum()
    
    df = df[df.coeff != 0]
    
    polynom = df.values.tolist()

    polynom = [li[::-1] for li in polynom]
    
    polynom.sort(key=lambda x: len(x[1]))
         
    polynom = [["" if j == 1 else "-" if j == -1 else "" if j == 0 else str(j) for j in i] for i in polynom]
    
    polynom = ["".join(li) for li in polynom]
    
    polynom = '+'.join(polynom)
    
    polynom = polynom.replace("+-", "-")

    return polynom

 

polys = [
    "-xyz+3zxy",
    "2xy+yx",
    "ax+bc-df+gg",
    "2xy-yx",
    "3xy+4bc-5yx-3cb+3bc",
    "-a+5ab+3a-c-2a"
]

for p in polys:
    simplify(p)


tests = {
    "dc+dcba": "cd+abcd",
    "2xy-yx": "xy",
    "-a+5ab+3a-c-2a": "-c+5ab",
    "a+ca-ab": "a-ab+ac",
    "-8fk+5kv-4yk+7kf-qk+yqv-3vqy+4ky+4kf+yvqkf": "3fk-kq+5kv-2qvy+fkqvy"
}

for inp, corr in tests.items():
    out = simplify(inp)
    print("INPUT: {0}, RESULT: {1} [{2}] " . format(inp, out, out == corr))