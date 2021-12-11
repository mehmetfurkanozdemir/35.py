# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 08:51:04 2021

@author: Pc
"""

v = float(input("Enter your mid-term exam result: "))
f = float(input("Enter your final exam result: "))
yn = 0.4 * v + 0.6 * f

if yn >=85 and yn <100:
  
  print("AA ile geçtin, weelll:", yn)
  
elif yn>=70 and yn< 85:

   print("BB ile geçtin, fena değil:" yn)
  
else :

  print("FF ile kaldın, you have to work more:" yn)
  
# burdaki hata nedir ?????????????