#WILLIAM YE
#260982747
import math
import doctest

def add_vectors(v1,v2):
    
    """
    (dict, dict) --> void
    This function takes two vectors in the form of
    dictionnaries and adds them together.
    It only modifies the input of v1.
    
    >>> v1 = {'a' : 1, 'b' : 3}
    >>> v2 = {'a' : 1, 'c' : 1}
    >>> add_vectors(v1,v2)
    >>> v1
    {'a': 2, 'b': 3, 'c': 1}
    >>> v1 == {'a' : 2, 'b' : 3, 'c' : 1}
    True
    >>> v1['a']
    2
    
    >>> v3 = {"a": 2, "b" : 3, "d" : 5}
    >>> v4 = {"c" : 4, "e": 4 }
    >>> add_vectors(v3,v4)
    >>> v3
    {'a': 2, 'b': 3, 'd': 5, 'c': 4, 'e': 4}
    >>> v3 == {'a': 2, 'b': 3, 'd': 5, 'c': 4, 'e': 4}
    True
    >>> v3["c"]
    4
    
    >>> v5 = {"a": -2, "b": -5}
    >>> v6 = {"a" : -4, "b": -2}
    >>> add_vectors(v5,v6)
    >>> v5
    {'a': -6, 'b': -7}
    >>> v5 == {'a': -6, 'b': -7}
    True
    
    """
    
    #iterates through second dictionnary
    for key in v2:
        #if key is in v1 and v2 then we would add the values
        if key in v1:
            v1[key] = v1[key] +v2[key]
            #checks if the value at current key is 0
            if v1[key] == 0:
                # if value is 0 then we delete the key 
                del v1[key]
        #if the key is not in v1 then we create a new key with the same value in v2
        elif key not in v1:
            v1[key] = v2[key]
            #checks if the value at current key is 0
            if v1[key] == 0:
                # if value is 0 then we delete the key 
                del v1[key]
    

def sub_vectors(d1,d2):
    """
    (dict,dict) --> dict
    This function takes 2 vectors in the form
    of 2 dictionnaries and the first vector
    substracts the second vector without
    modifying any of the inputs. It returns
    a new dictionnary instead.
    
    >>> d1 = {'a' : 3, 'b': 2}
    >>> d2 = {'a': 2, 'c': 1, 'b': 2}
    >>> d = sub_vectors(d1, d2)
    >>> d == {'a': 1, 'c': -1}
    True
    >>> d1 == {'a': 3, 'b': 2}
    True
    >>> d2 == {'a': 2, 'c': 1, 'b': 2}
    True
    
    >>> d3 = {"a":-2, "b" : -3, "d": 12}
    >>> d4 = {"a": 5, "d": 10, "b": -3}
    >>> d = sub_vectors(d3,d4)
    >>> d == {'a': -7, 'd': 2}
    True
    >>> d3 == {"a":-2, "b" : -3, "d": 12}
    True
    >>> d4 == {"a": 5, "d": 10, "b": -3}
    True
    
    >>> d5 = {"a": 0, "b": 20, "c":-3}
    >>> d6 = {"a":0 , "b": 0, "c" : 0}
    >>> d = sub_vectors(d5, d6)
    >>> d == {'b': 20, 'c': -3}
    True
    >>> d5 == {"a": 0, "b": 20, "c":-3}
    True
    >>> d6 == {"a":0 , "b": 0, "c" : 0}
    True

    """
    #creates a new dictionnary to deep copy the inputs
    empty_dict = {}
    
    #creates a deep copy of d1 into an empty dictionnary
    for key in d1:
        empty_dict[key] = d1[key]
        #checks if any keys if a value of 0
        if empty_dict[key] == 0:
            #if so we would delete that key
            del empty_dict[key]
    
    #iterates through the second vector
    for key in d2:
        #checks if the current key in d2 is in d1
         if key in d1:
             #if so we would substract the value of d1 by d2
             empty_dict[key] = d1[key] - d2[key]
             #checks if the current key has the value of 0
             if empty_dict[key] == 0:
                 #if so we would delete that key 
                del empty_dict[key]
             
         elif key not in d1:
             #creates a new key in the new dictionnary if current key not found in d1
            empty_dict[key] = -d2[key]
            #checks if the current key has a value of 0
            if empty_dict[key] == 0:
                #deletes the current key has a value of 0
                del empty_dict[key]
                
    #returns new substracted dictionnary       
    return empty_dict

def merge_dicts_of_vectors(d1,d2):
    
    
    """
    (dict,dict) --> void
    This function takes 2 dictionnaries as input
    and 
    
    >>> d1 = {'a' : {'apple': 2}, 'p' : {'pear': 1, 'plum': 3}}
    >>> d2 = {'p' : {'papaya' : 6}}
    >>> merge_dicts_of_vectors(d1, d2)
    >>> d1
    {'a': {'apple': 2}, 'p': {'pear': 1, 'plum': 3, 'papaya': 6}}
    
    >>> d4 = {'l' : {'lamborghini': 41}, 'm' : {'masserati': 5, 'mercedes': 3}, "t" : {'toyota' :2}}
    >>> d3 = {'a' : {'aston martin': 12}, 'm' : {'masserati': 21, 'mercedes': 4}}
    >>> merge_dicts_of_vectors(d3, d4)
    >>> d3
    {'a': {'aston martin': 12}, 'm': {'masserati': 26, 'mercedes': 7}, 'l': {'lamborghini': 41}, 't': {'toyota': 2}}
    
    >>> d5 = {'g': {'goat':32, 'geese': 21}, 'c': {'cows': 10},'r': {'rabbits':21}}
    >>> d6 = {'w': {'wolf': 41 }}
    >>> merge_dicts_of_vectors(d5, d6)
    >>> d6
    {'w': {'wolf': 41}}
    >>> d5
    {'g': {'goat': 32, 'geese': 21}, 'c': {'cows': 10}, 'r': {'rabbits': 21}, 'w': {'wolf': 41}}
    
    """
    
    
    for key in d2:
        
        #adds a key from d2 in d1 if the key doesnt exist in d1 
        if key not in d1:
            
            d1[key] = d2[key] 
        
        
        #if key in d2    
        elif key in d1:
            
            #iterates through every key value in the inner dictionnaries of d2
            for key2 in d2[key]:
                
                #if inner key are also found in d1
                if key2 in d1[key]:
                    #updates the key inner keys of d1 by adding the values of d2
                    d1[key][key2]+= d2[key][key2]
                
                #if inner key are not found in d1
                elif key2 not in d1[key]:
                    #creates a new inner key in d1 and assigns the value of the inner key in d2
                    d1[key][key2] = d2[key][key2]
                                 

def get_dot_product(v1,v2):
    """
    (dict,dict) ---> int
    This function takes 2 vectors in the form as
    dictionnaries for both inputs. It then returns
    the dot product the 2 vectors as input.
    
    >>> v1 = {'a' : 3, 'b': 2}
    >>> v2 = {'a': 2, 'c': 1, 'b': 2}
    >>> get_dot_product(v1, v2)
    10
    
    >>> v3 = {'a' : 7, 'b': -21}
    >>> v4 = {'c': -3}
    >>> get_dot_product(v3, v4)
    0
    
    >>> v5 = {"a" : -2, "b": 3, "c" : -2}
    >>> v6 = {"a": -3, "b": 5, "c": 3}
    >>> get_dot_product(v5, v6)
    15
    
    """
    #sets default dot product
    dot_product = 0
    
    for key in v2:
        if key in v1:
            # updates the dot product if key is present in both vectors
            dot_product += v1[key]*v2[key]
    #returns final dot product
    return dot_product



def get_vector_norm(v1):
    
    """
    (dict)--> int
    This function takes in a vector in
    the form of a dictionnary and returns
    the vector length
    
    >>> v1 = {'a' : 3, 'b': 4}
    >>> get_vector_norm(v1)
    5.0
    
    >>> v2 = {'a': 3, 'c': -5, 'b': 1}
    >>> round(get_vector_norm(v2), 3)
    5.916
    
    >>> v3= {'a': 6, 'b': 10, 'c': -2}
    >>> round(get_vector_norm(v3), 3)
    11.832
    
    """
    #sets the sum of all coordinates of vectors to 0
    sum = 0
    
    #updates the sum by multiplying the coordinate by itself and adding it into the variable sum
    for key in v1:
        sum += (v1[key])**2
    #find the square root of the sum    
    vector_length = math.sqrt(sum)
        
    return vector_length
        
    

    
    
def normalize_vector(v1):
    """
    (dict) --> void
    This function takes in a vector in the
    form of a dictionnary and divides each value
    by the norm of the vector.
    
    >>> v1 = {'a' : 3, 'b': 4}
    >>> normalize_vector(v1)
    >>> v1['a']
    0.6
    >>> v1['b']
    0.8
    
    >>> v2 = {'a': 3, 'c': -5, 'b': 1}
    >>> normalize_vector(v2)
    >>> round(v2['a'],3)
    0.507
    
    >>> v3= {'a': 6, 'b': 10, 'c': -2}
    >>> normalize_vector(v3)
    >>> round(v3['c'],3)
    -0.169
    
    """
    #this gets the vector length
    vector_length = get_vector_norm(v1)
    
    #divides each coordinate of the vector by its norm
    for key in v1:
        v1[key] = v1[key]/ vector_length

doctest.testmod() 
       
    
    

            

             
        
        
        
    
    