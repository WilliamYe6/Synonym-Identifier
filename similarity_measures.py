#WILLIAM YE
#260982747
from vectors_utils import *
import doctest

def get_semantic_descriptor(word, sentence):
    """
    (string, list) --> dict
    This function takes in a string and list
    and returns a dictionnary representing
    the semantic descriptor vector of the
    word w computed from the sentence (in the form as a list)
    
    >>> s1 = ['all', 'the', 'habits', 'of', 'man', 'are', 'evil']
    >>> desc1 = get_semantic_descriptor('evil', s1)
    >>> desc1['all']
    1
    >>> len(desc1)
    6
    >>> 'animal' in desc1
    False
    
    >>> s2 = ['hello', 'hello', 'i', 'am', 'very', 'excited', 'for', 'winter', 'break']
    >>> get_semantic_descriptor ('winter', s2)
    {'hello': 2, 'i': 1, 'am': 1, 'very': 1, 'excited': 1, 'for': 1, 'break': 1}
    
    >>> s3 = ['hello', 'guys', 'i', 'am', 'not', 'excited', 'for', 'final', 'exams']
    >>> get_semantic_descriptor ('summer', s3)
    {}
    
    """

    #creates a default empty dictionnary
    semantic_descriptor = {}
    
    #returns an empty dictionnary if the word not in sentence
    if word not in sentence:
        return semantic_descriptor
    
    
    for words in sentence:
        #skips the update of the dictionnary when at the word in the sentence
        if words == word:
            continue
        #if not creates a new key in the dictionnary with a default value of 0
        elif words not in semantic_descriptor:
            semantic_descriptor[words] = 1
        
        #updates the occurence of the word in the sentence
        elif (words in semantic_descriptor) and  (words != word):
            semantic_descriptor[words] += 1
    
    return semantic_descriptor

    
def get_all_semantic_descriptors(text):
    
    """
    (list) --> dict
    This function takes as input a list
    of lists representing the words in a
    text, where each sentence in a text is
    represented by a sublist of the input list.
    The function then returns a dictionary with
    dictionaries inside that represent the semantic
    description of each word in those sentences.
    
    >>> s = [['all', 'the', 'habits', 'of', 'man', 'are', 'evil'], \
    ['and', 'above', 'all', 'no', 'animal', 'must', 'ever', 'tyrannise', 'over', 'his', 'own', 'kind'], \
    ['weak', 'or', 'strong', 'clever', 'or', 'simple', 'we', 'are', 'all', 'brothers'], \
    ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal'], \
    ['all', 'animals', 'are', 'equal']]
    >>> d = get_all_semantic_descriptors(s)
    >>> d['animal']['must']
    3
    >>> d['evil'] == {'all': 1, 'the': 1, 'habits': 1, 'of': 1, 'man': 1, 'are': 1}
    True
    
    >>> s2 = [['heavy', 'is', 'the', 'head', 'that', 'wears', 'the', 'crown'],\
    ['this', 'is', 'a', 'pretty', 'cool', 'quote']]
    >>> x = get_all_semantic_descriptors(s2)
    >>> x['heavy']
    {'is': 1, 'the': 2, 'head': 1, 'that': 1, 'wears': 1, 'crown': 1}
    
    >>> s3 = [['you', 'shall', 'not', 'pass', 'only', 'the', 'chosen', 'one', 'can', 'pass'],['this', 'quote', 'comes', 'from', 'lord', 'of', 'the', 'rings']]
    >>> y = get_all_semantic_descriptors(s3)
    >>> y['shall']
    {'you': 1, 'not': 1, 'pass': 2, 'only': 1, 'the': 1, 'chosen': 1, 'one': 1, 'can': 1}
    >>> y['shall']['pass']
    2
    
    """
    
    #creates empty dictionnary that will hold all semantic descriptors
    semantic_descriptor = {}
    
    #iterates through every sentence
    for sentence in text:
        #iterates through every word
        for word in sentence:
            
            #if the semantic descriptor for a word is not added in the empty dictionnary
            if word not in semantic_descriptor:
                #adds a new semantic descriptor in empty dictionnary
                semantic_descriptor[word] = get_semantic_descriptor(word, sentence)
            
             #if the semantic descriptor for a word is already added in the empty dictionnary
            elif word in semantic_descriptor:
                
                #creates a temp dictionnary
                temp_dict = {}
                #gets the semantic descriptor and holds in a temperary variable
                hold = get_semantic_descriptor(word, sentence)
                #puts the temperary variable "hold" inside a dictionnary so that the input is valid
                #for the function merge_dicts_of_vectors(d1,d2)
                temp_dict["temp_key"] = hold
                
                #creates a temp dictionnary
                temp_dict2 = {}
                #gets the semantic descriptor and puts the temperary variable "hold" inside a dictionnary
                #so that the input is valid for the function merge_dicts_of_vectors(d1,d2)
                temp_dict2["temp_key"] = semantic_descriptor[word]
                #merge both of the temporary dictionaries
                merge_dicts_of_vectors(temp_dict2, temp_dict)
                #access the value of the temperary dictionnary and add it inside the final dictionary 
                semantic_descriptor[word]  = temp_dict2["temp_key"]
    
    return semantic_descriptor


def get_cos_sim(u,v):
    """
    (dict, dict) --> float
    
    >>> s = [['all', 'the', 'habits', 'of', 'man', 'are', 'evil'], \
    ['and', 'above', 'all', 'no', 'animal', 'must', 'ever', 'tyrannise', 'over', 'his', 'own', 'kind'], \
    ['weak', 'or', 'strong', 'clever', 'or', 'simple', 'we', 'are', 'all', 'brothers'], \
    ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal'], \
    ['all', 'animals', 'are', 'equal']]
    >>> d = get_all_semantic_descriptors(s)
    >>> v1 = d['evil']
    >>> v2 = d['animal']
    >>> round(get_cos_sim(v1, v2), 4)
    0.0595
    
    >>> round(get_cos_sim({"a": 3, "b": -2,"d": 8, "e": -4}, {"a": 4, "c": -4, "d": 2}), 2)
    0.48
    
    >>> round(get_cos_sim({"a": 7, "b": 4,"c": 5, "f": -4}, {"a": 7, "c": 12, "e": 8}), 2)
    0.66
    
    """
    #this gets the dot product for the 2 vectors 
    dot = get_dot_product(u,v)
    
    #calculates the length of the first vector
    u_norm = get_vector_norm(u)
    
    #calculates the length of the second vector
    v_norm = get_vector_norm(v)
    
    #calculates the denominator of the formula used
    denominator = (u_norm)* (v_norm)
    
    #returns the cosine similarity between the two vectors 
    return (dot/ denominator)
    

def get_euc_sim(v1,v2):
    """
    (dict, dict) --> float
    This function takes 2 vectors as input(dictionary)
    and returns the negative euclidean distance between
    the two vectors
    
    >>> s = [['all', 'the', 'habits', 'of', 'man', 'are', 'evil'], \
    ['and', 'above', 'all', 'no', 'animal', 'must', 'ever', 'tyrannise', 'over', 'his', 'own', 'kind'], \
    ['weak', 'or', 'strong', 'clever', 'or', 'simple', 'we', 'are', 'all', 'brothers'], \
    ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal'], \
    ['all', 'animals', 'are', 'equal']]
    >>> d = get_all_semantic_descriptors(s)
    >>> v1 = d['evil']
    >>> v2 = d['animal']
    >>> round(get_euc_sim(v1, v2), 4)
    -7.1414
    
    >>> round(get_euc_sim({"a": 5, "b": 4, "c": 3,"e":-2}, {"b": -5, "c": 3, "d": 2}), 2)
    -10.68
    
    >>> round(get_euc_sim({"a": -4, "b": 3 ,"e":5}, {"b": 2, "c": -3, "d": 1}), 2)
    -7.21
    
    """
    #find difference between the two vectors 
    vector_diff = sub_vectors(v1,v2)
    # calculates the negative euclidean distance between the two vectors
    euclidean_distance = get_vector_norm(vector_diff)*(-1)
    
    return euclidean_distance


    
def get_norm_euc_sim(v1,v2):
    """
    (dict, dict) --> float
    
    This function takes two vectors in the form of dictionnaries as input
    and returns the negative euclidean distance between
    the two normalized vectors.
    
    >>> v1 = {'a': 10, 'b' : -12, 'c': 4}
    >>> v2 = {'a':2, 'c':-2, 'b': 4}
    >>> round(get_norm_euc_sim(v1,v2),4)
    -1.7063
    
    >>> s = [['all', 'the', 'habits', 'of', 'man', 'are', 'evil'], \
    ['and', 'above', 'all', 'no', 'animal', 'must', 'ever', 'tyrannise', 'over', 'his', 'own', 'kind'], \
    ['weak', 'or', 'strong', 'clever', 'or', 'simple', 'we', 'are', 'all', 'brothers'], \
    ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal'], \
    ['all', 'animals', 'are', 'equal']]
    >>> d = get_all_semantic_descriptors(s)
    >>> v3 = d['evil']
    >>> v4 = d['animal']
    >>> round(get_norm_euc_sim(v3, v4), 4)
    -1.3715
    
    >>> v5 = {"a": 12, "b":3, "c": 6}
    >>> v6 = {"a":2, "b":-5, "d" : 1, "e": 8}
    >>> round(get_norm_euc_sim(v5,v6),4)
    -1.3656
    
    """
    #this normalizes the first vector
    normalize_vector(v1)
    #this normalizes the second vector
    normalize_vector(v2)
    
    #returns the negative euclidean distance between the 2 normalized vectors
    return get_euc_sim(v1,v2)
    
doctest.testmod() 
