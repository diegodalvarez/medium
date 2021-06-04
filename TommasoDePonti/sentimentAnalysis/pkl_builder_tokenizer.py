# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 01:37:48 2020

@author: Diego
"""

#this creates a function where you pass through text 
def tokenizer(text):
    
    #this creates a variable called text the re.sub part means go through the string
    text = re.sub('<[^>]*>', '', text)
    
    #this is for the other characters
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text.lower())
    
    #this cleans all the text up together
    text = re.sub('[\W]+', ' ', text.lower()) +\
        ' '.join(emoticons).replace('-', '')