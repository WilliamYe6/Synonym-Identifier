#WILLIAM YE
#260982747

import doctest
from vectors_utils import *
from similarity_measures import *

def get_sentences(text):
    """
    (string) --> list
    This function takes in a string as
    input and returns each sentence in
    an element. The sentences are seperated
    by the punctuations ".", "!", "?"
    
    >>> text = "No animal must ever kill any other animal. All animals are equal."
    >>> get_sentences(text)
    ['No animal must ever kill any other animal', 'All animals are equal']
    
    >>> text2 = "Hi! How are you? How was your day?"
    >>> get_sentences(text2)
    ['Hi', 'How are you', 'How was your day']
    
    >>> text3 = "Are you going to move out soon? I heard you found a nice place in the city. Must be nice to have your own place!"
    >>> get_sentences(text3)
    ['Are you going to move out soon', 'I heard you found a nice place in the city', 'Must be nice to have your own place']
    
    """
    
    #creates an empty string
    empty_text = ""
    
    
    #updates the empty string with the text, except that
    #there is no whitespace at the beginning of each sentence
    for i in range (len(text)):
        if (i< len(text)-1) and text[i] == " " and text[i-1] in ['.', '!', '?']:
            
            continue
        
        empty_text += text[i]
            
    
    #edge case
    #this removes the punctuation at the end of the last sentence so there is no extra space in the list
    if empty_text[len(empty_text)-1] in ['.', '!', '?']:
        empty_text  = empty_text[:len(empty_text)-1]

    #creates an empty list where we will start splitting the text into sentences
    sentence = []
    #splits every sentence with a '?'
    sentence = empty_text.split('?')
    
    #this will split all sentences that have a "!"
    #if there is no "!" then we will only be placing the list into
    #a new variable
    new_sentence = []
    for i in sentence:
        updated = i.split('!')
        for j in range (len(updated)):
            new_sentence.append(updated[j])
    
    #This will split all sentences that are seperated by a "."
    #if there is no "." then we will only be placing the list into
    #a new variable
    newest_sentence = []
    for j in new_sentence:
        latest =  j.split('.')
        for z in range (len(latest )):
            newest_sentence.append(latest[z])
           
    return newest_sentence

def get_word_breakdown(text):
    
    """
    (string) ---> list
    
    This function takes in a string as input
    and returns a list of each word in the string.
    All the punctuations are seperated.
    
    
    >>> text = "All the habits of Man are evil. And, above all, no animal must ever tyrannise over his\
    own kind. Weak or strong, clever or simple, we are all brothers. No animal must ever kill\
    any other animal. All animals are equal."
    >>> s = [['all', 'the', 'habits', 'of', 'man', 'are', 'evil'], \
    ['and', 'above', 'all', 'no', 'animal', 'must', 'ever', 'tyrannise', 'over', 'his', 'own', 'kind'], \
    ['weak', 'or', 'strong', 'clever', 'or', 'simple', 'we', 'are', 'all', 'brothers'], \
    ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal'], \
    ['all', 'animals', 'are', 'equal']]
    >>> w = get_word_breakdown(text)
    >>> s == w
    True
    
    >>> text2 = "Sometimes in life, there will be some minor setbacks for major comebacks. Trust yourself and everything will take place"
    >>> get_word_breakdown(text2)
    [['sometimes', 'in', 'life', 'there', 'will', 'be', 'some', 'minor', 'setbacks', 'for', 'major', 'comebacks'], ['trust', 'yourself', 'and', 'everything', 'will', 'take', 'place']]
    
    >>> text3 = "But are you a different animal, but the same beast? What does that mean Kobe Bryant? You are welcome"
    >>> get_word_breakdown(text3)
    [['but', 'are', 'you', 'a', 'different', 'animal', 'but', 'the', 'same', 'beast'], ['what', 'does', 'that', 'mean', 'kobe', 'bryant'], ['you', 'are', 'welcome']]
    
    """
    
    #creates a list with all of the possible punctuations
    PUNCTUATION = [',', '-', '--', ':', ';', '"', "'"]
    
    
    #this variable is to store the original string without any punctuation
    empty_text = ""
    #this adds the original string without the puncuation into an empty string 
    for i in range (len(text)):
        if ((i< len(text)-1) and (text[i] in PUNCTUATION)):
        
            remover = " "
            empty_text += remover
            
            
        else:
            empty_text += text[i]
    
    #this variables is used to store the original string in lower case
    lower_case = ""
    #converts all of the original string into lower case
    for i in empty_text:
        lower = i.lower()
        lower_case += lower
    
    
    
        
    #this function seperates the text into sentences that place are stored in a list
    sentences = get_sentences(lower_case)
    
    #this variable is an empty list that will store all of the words in a new list
    final_list = []
    
    #iterates through the variable sentences 
    for words in sentences:
            
        #splits the sentence for every space
        final_word = words.split(" ")
        #creates a new list just in case for any tabs or newlines
        temp_list = []
        
        #iterates through every element that is split
        #and checks if there is any empty strings as elements
        for elements in final_word:
            #if elements is not an empty string then we add the element to the temp list
            if elements != "":
                elements = elements.strip("\n")
                temp_list.append(elements)
        #we fianlly add every temp list into the final list which will be returned
        final_list.append(temp_list)
    
        
    return final_list
    
   


def build_semantic_descriptors_from_files(filename):
    
    """
    (list) ---> dict
    This function takes in a list of text files and
    reads them and returns the get_all_semantic_descriptor()
    function for every word in the text files.
    
    >>> d = build_semantic_descriptors_from_files(['animal_farm.txt'])
    >>> d['animal']['must']
    3
    >>> d["are"]
    {'all': 3, 'the': 1, 'habits': 1, 'of': 1, 'man': 1, 'evil': 1, 'weak': 1, 'or': 2, 'strong': 1, 'clever': 1, 'simple': 1, 'we': 1, 'brothers': 1, 'animals': 1, 'equal': 1}
    
    
    >>> d = build_semantic_descriptors_from_files(['animal_farm.txt', 'alice.txt'])
    >>> d["animal"]
    {'and': 1, 'above': 1, 'all': 1, 'no': 3, 'must': 3, 'ever': 3, 'tyrannise': 1, 'over': 1, 'his': 1, 'own': 1, 'kind': 1, 'kill': 2, 'any': 2, 'other': 2}
    
    >>> d = build_semantic_descriptors_from_files(['alice.txt'])
    >>> d["t"]
    {'if': 1, 'you': 1, 'didn': 1, 'sign': 1, 'it': 1, 'said': 1, 'the': 2, 'king': 1, 'that': 1, 'only': 1, 'makes': 1, 'matter': 1, 'worse': 1}
    """
   
    #creates a dictionary to be returned 
    final_dict = {}
    #loops through every file in the list
    for i in filename:
        
        #opens and reads every file
        file_obj = open (i, "r", encoding="utf-8")
        file_content = file_obj.read()
        
        
        #breaks down every word in the file 
        words = get_word_breakdown(file_content)
       
    
        #calls every all semantic descriptors for the text file 
        semantic_descriptor  =  get_all_semantic_descriptors(words)
        
        #merges the semantic_descriptor with the current the final dictionnary returned
        merge_dicts_of_vectors(final_dict, semantic_descriptor)    
        file_obj.close()
    
    return final_dict


doctest.testmod()    

    
    
