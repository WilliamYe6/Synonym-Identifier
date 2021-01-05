#WILLIAM YE
#260982747

from file_processing import *
import doctest

def most_sim_word(word, choices, sem_descs, similarity_fn):
    
    """
    (str, list, dict, function) ---> str
    
    This function takes 4 arguments as input
    and returns the most similiar word in the
    list choices to the argument "word"
    
    >>> choices = ['dog', 'cat', 'horse']
    >>> c = {'furry' : 3, 'grumpy' : 5, 'nimble' : 4}
    >>> f = {'furry' : 2, 'nimble' : 5}
    >>> d = {'furry' : 3, 'bark' : 5, 'loyal' : 8}
    >>> h = {'race' : 4, 'queen' : 2}
    >>> sem_descs = {'cat' : c, 'feline' : f, 'dog' : d, 'horse' : h}
    >>> most_sim_word('feline', choices, sem_descs, get_cos_sim)
    'cat'
    
    >>> choices = ['cow', 'feline', 'horse', 'eagle']
    >>> c = {'sturdy' : 3, 'heavy' : 5, 'herbivor' : 4}
    >>> f = {'furry' : 2, 'nimble' : 5}
    >>> h = {'race' : 4, 'queen' : 2}
    >>> e = {'speed':3, 'vigilant':2, 'feather':4}
    >>> t = {'aggresive':3, 'heavy':4, 'sturdy':2}
    >>> sem_descs = {'cow' : c, 'feline' : f, 'horse': h, 'eagle': e, "taureau": t  }
    >>> most_sim_word('taureau', choices, sem_descs, get_cos_sim)
    'cow'
    
    >>> choices = ['cow', 'feline', 'horse', 'eagle']
    >>> c = {'sturdy' : 3, 'heavy' : 5, 'herbivor' : 4}
    >>> f = {'furry' : 2, 'nimble' : 5}
    >>> h = {'race' : 4, 'queen' : 2}
    >>> e = {'speed':3, 'vigilant':2, 'feather':4}
    >>> p = {'stupid':3, 'light':4, 'feather':2}
    >>> sem_descs = {'cow' : c, 'feline' : f, 'horse': h, 'eagle': e, "pigeon": p  }
    >>> most_sim_word('pigeon', choices, sem_descs, get_cos_sim)
    'eagle'
    
    """
    
    #default empty lists used to later in the function
    list = []
    
    #calls similarity function
    for i in choices:
        try:
            value = similarity_fn(sem_descs[i], sem_descs[word])
        
        #Raises ZeroDivisionError
        except ZeroDivisionError:
            
            #Set value to float('-inf')
            value = float('-inf')
        
        #updates the list by adding the key and value into the list
        list.append([i,value])
    
    #empty list to store the values 
    all_values = []
    
    #checks if the semanctic similarity is valid 
    for index in list:
        if (index[1] != None) and (index[1] != float('-inf')):
            all_values.append(index[1])
    
    #edge case that checks if there is no valid semantic similarity
    if all_values == [] :
        return ""
    
    #gets the max value inside the list all_values
    maximum_value = max(all_values)
    
    #empty list that stores the keys
    all_keys = []
    
    #updates the max values in a list
    for index in list:
        if index[1] == maximum_value:
            all_keys.append(index[0])
            
    #returns the smallest index in the list 
    return all_keys[0]


def run_sim_test(filename, descriptors , similarity_fn):
    
    """
    (str,dict, function) ---> float
    
    This function takes 4 arguments as input
    and will return the pourcentage of corrrect
    answer answered by the function most_sim_word.
    
    >>> descriptors = build_semantic_descriptors_from_files(['test.txt'])
    >>> run_sim_test('test.txt', descriptors, get_cos_sim)
    15.0
    
    (only 1 example possible)
    """
    
    #****************** find all semantic descriptions ************************
    
    #This will rewrite the orignal test.txt file in one line 
    obj_file = open(filename, "r", encoding="utf-8")
    text = obj_file.read()
    no_lines_text = text.replace("\n", " ")
    obj_file.close()
    
    #this will add the rewritten test.txt file into a new file called temp.txt
    new_file = "temp.txt"
    latest_file = open(new_file, "w", encoding="utf-8")
    latest_file.write(no_lines_text)
    latest_file.close()
    
    #we will then get all_semantic_descriptors by calling the temp.txt files 
    all_semantic_descriptors = build_semantic_descriptors_from_files([new_file])
    
    #used later when calling the function most_sim_word
    #**************************************************************************************
    
    
    #open filename
    file = open(filename, "r", encoding="utf-8")
    
    #creates an temporary list 
    all_lines = []
    
    #this will put every eachline into a subslist
    for i in file:
        all_lines.append([i.strip("\n")])
    
    file.close()
    #creates another temporary list
    updated_lines = []
    
    #this will transform every sublist from the list all_lines into string
    for element in all_lines:
        subList_str =(''.join(element))
        updated_lines.append(subList_str)

    #this will transfrom the list updated_lines into a string used for get_word_breakdown
    new_string = ('.'.join(updated_lines)) 
    last_list = get_word_breakdown(new_string)    
    
    #creates a new list that will help check if the answers are correct
    helper_list =[]
    
    
    #iterates through the last list and gets the answer with the most_sim_word function
    for i in range(len(last_list)):
        
        #sets the word questioned as a variable 
        word = last_list[i][0]
        
        #sets the possible choices to chose from
        choices = last_list[i][2:]
        
        #sets the answer as a variable 
        answer = last_list[i][1]
        
        #calls most_sim_word function to get answer
        get_answer = most_sim_word(word,choices, all_semantic_descriptors,similarity_fn)
        
        #updates the helper function by adding each answer
        helper_list.append(get_answer)
        
    x = 0   
    for j in range(len(helper_list)):
        
        # checks if the answer is correct and keeps count of the number of correct answers 
        if helper_list[j] == last_list[j][1] :
            x += 1
    
    #finds the success pourcentage rate      
    pourcentage = round(((x / (len(helper_list))) * 100), 0)
    
    return pourcentage
    
    
doctest.testmod()
