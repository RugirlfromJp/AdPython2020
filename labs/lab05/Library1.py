# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 22:20:11 2020

@author: masha
"""

class Library:
    def __init__(self, name, booklist, numberlist): #для удобства не только список книг, но и список их номеров
        self.books = booklist
        self.name = name
        self.numbers = numberlist
        self.authorbooks = {}

    
    def addbook(self, book):
        if book.number in numberlist:
            print('the book is already here')
        else:
            numberlist.append(number)
            booklist.append(book)
            if book.author in self.authorbooks:
                authorbooks[book.author].append(book.title)
            else:
                authorbooks[book.author] = []
                authorbooks[book.author].append(book.title)
            
    def searchbook(self, author):
        if author in authorbooks:
            print(authorbooks[author])
        else:
            print('No books of this author')
        
    def bookinfo(self, number):
        if number in self.numberlist:
            print('Yes, it is here, wait a second!')
            n = numberlist.index(number)
            Thebook = booklist[n]
            print(Thebook.title, Thebook.author, Thebook.number)
            
        
    def delbook(self, book)
        if book.number in self.numberlist:
            n = numberlist.index(number)
            booklist.pop([n])
            numberlist.pop([n])
            authorbooks[book.author].remove(book.title)

class Book:
    def __init__(self, number, title, publisher, data, author):
        self.number = number
        self.author = author
        self.title = title
        self.publisher = publisher
        self.data = data

def test_library():
    latte = Book(123, 'Gone with the wind', 'Second Chance', 202020, 'Margaret Mitchell')
    cappuccino = Book(124, 'Anna Karenina', 'No Second Chance', 202021, 'Tolstoy')
    coffeebooks = [latte, cappuсcino]
    CoffeeLibrary = Library(CoffeeLibrary, coffeebooks, coffeenumbers)
    War_and_Peace = Book(125, 'War and Peace', 'Maybe next time', 202022, 'Tolstoy')
    CoffeeLibrary.addbook(War_and_Peace)
    CoffeeLibrary.searchbook('Tolstoy')
    
    del CoffeeLibrary.authorbooks['Tolstoy']

if __name__ == '__main__':
    test_library()
    