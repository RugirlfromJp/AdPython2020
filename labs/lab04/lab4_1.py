# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 21:34:28 2020

@author: masha
"""

if __name__ == '__main__':
    def author(_author):
        def wrapper(func):
            func.author = _author #присвоили функции параметр
            return func #сделали что-то с функцией и вернули её
        return wrapper
   
    @author("Captain Friedrich Von Schoenvorts")
    def add2(num: int) -> int:
        return num + 2
    
    print(add2.author)