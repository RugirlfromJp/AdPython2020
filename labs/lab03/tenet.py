# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 09:29:15 2020

@author: masha
"""

if __name__ == '__main__':

    def tenet(input_file_path: str, output_file_path: str):
        with open (input_file_path, 'r') as inp:
            inplist = []
            for line in inp:
                #line.strip('\n') -- почему не работает так?
                inplist.append(line)
                
        outlist = []
        for phrase in inplist:
            phrase = phrase.strip('\n')
            outlist.append(phrase[::-1])
        print(outlist)
        finallist = []
        for i in range (len(outlist)):
            finallist.append(outlist[-i-1])
        print(finallist)
        with open (output_file_path, 'w') as otp:
            for phrase in finallist:
                otp.write(phrase)
                #пока не придумала, как сделать с переводом строки
    tenet('D:/MIPT/Python_prac_2020/fortenet.txt', 'D:/MIPT/Python_prac_2020/fortenet2.txt')
    
