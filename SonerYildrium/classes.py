# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 22:16:58 2021

@author: Diego
"""

class Book():
    
    def __init__(self, name, writer, word_length):
        
        self.name = name
        self.writer = writer
        self.word_length = word_length
        
    def number_of_pages(self, fontsize):
        
        word_length = self.word_length
        
        if fontsize == 12:
            words_in_page = 300
            
        else:
            words_in_page = 300 - (fontsize - 12) * 10
            
        return round(word_length / words_in_page)

#setting the variables of the class              
b1 = Book("Pandas", "John Doe", 1000000)
print(b1.name)

#now we want to change the class variable name 
b1.name = "NumPy"
print(b1.name)

print(b1.number_of_pages())

#if we change the font size then we will get a different amount of pages
b1.number_of_pages(fontsize = 16)
print(b1.number_of_pages())