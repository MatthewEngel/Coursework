#Matthew Engel, Tro Davenport
#PA 4, due 04/02/2024
#This code takes data and represents it in a easy-to-read plot/diagram.

#brushed up on dictionaries here:
#    https://www.w3schools.com/python/python_dictionaries_add.asp
#looked up what function is standard deviation for the statistics library using:
#    https://www.geeksforgeeks.org/python-statistics-stdev/
#enriched our knowledge on histograms and their use in python here:
#    https://www.geeksforgeeks.org/plotting-histogram-in-python-using-matplotlib/

#we decided to offer more options for the txt file part of this PA. during this, however, we
#consulted chat gpt on how to write a dictionary into a txt file.
#These lines of code were *heavily* inspired by chat gpt:
# for key, values in classes_grades.items():
#                 writing_file.write(f"{key} ")
#                 for value in values:
#                     writing_file.write(f"{value} ")
#                 writing_file.write(f"\n")
#We were having trouble writing the dictionaries into the txt file in the *correct format*, and chat gpt assisted us. 
#This code assigns keys and values to their respective variables from the dictionary, then loops through each key value pair.
#it writes the key, adds a space seperator, loops and writes each value (using a space as seperation),
#then when done with all values, prints out a new line for the next key value pair.


import matplotlib.pyplot as plt
import random
import statistics



def grades():
    #randomly generates a dictionary with 6 specific classes with random grades and random number of students.
    number_of_students=random.randrange(15,25)  #random quantity of students range 15-25
    classes_grades={'Math':[], 'Physics':[], 'Recreation':[], 'History':[], 'English':[], 'Chemistry':[] }
    
    for each_class_key in classes_grades:
        #assigns each key random grades. the quantity of grades is equal to the number of students.
        for classes_values in range(number_of_students):
            #randomizes grades and adds them to specific key/class
            x= random.randrange(0,100)
            classes_grades[each_class_key].append(x)
    #returns a dicitonary of 6 classes (keys) with randomized grades.        
    return classes_grades 

def graph_all_classes(classes_dictionary):
    #Graphs all the classes in the randomly generated dicitonary.
    plt.plot(classes_dictionary['Math'], linestyle = '--', marker = 'v', label = 'math')
    plt.plot(classes_dictionary['Physics'], linestyle = '--', marker = '.', label = 'physics')
    plt.plot(classes_dictionary['Recreation'], linestyle = '--', marker = 'o', label = 'recreation')
    plt.plot(classes_dictionary['History'], linestyle = '--', marker = '4', label = 'history')
    plt.plot(classes_dictionary['English'], linestyle = '--', marker = 'p', label = 'english')
    plt.plot(classes_dictionary['Chemistry'], linestyle = '--', marker = 'x', label = 'chemistry')

    plt.legend()
    plt.xlabel('Students')
    plt.ylabel('Grades')
    plt.title('Graph representing every student and their grades in 6 classes')
    plt.show()
    
def math_histogram(classes_dictionary):
    #provides a histogram of the frequency of math grades in this class (key).
    
    plt.hist(classes_dictionary['Math'])
    plt.xlabel('Grades')
    plt.ylabel('Frequency of Grades')
    plt.title('Bar graph represnting frequency of math grades')
    #used these ticks as before the ticks were every 20 numbers, which felt to vague.
    plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
        
    print(classes_dictionary['Math'])
    plt.show()
    

def classes_statistics(classes_dictionary):
    #aquires desired statistics of random grades for random number of students.
    try:
        for a_class in classes_dictionary.keys():
            #loops through keys/ their lists and using the stats library, prints out data.
            print('the maximum grade for', a_class, 'is:', max(classes_dictionary[a_class]))
            print('the minimum grade for', a_class, 'is:', min(classes_dictionary[a_class]))
            print('the average (mean) grade for', a_class, 'is:', statistics.mean(classes_dictionary[a_class]))
            print('the median grade for', a_class, 'is:', statistics.median(classes_dictionary[a_class]))
            print('the standard deviation for the grades in', a_class, 'is:', statistics.stdev(classes_dictionary[a_class]), '\n')
    except ValueError:
        print('not enough values/data provided to satisfy statistics')
        
def read_file_grade(filename):
    # Initialize an empty dictionary to store the grades for each class
    classes_grades = {'Math': [], 'Physics': [], 'Recreation': [], 'History': [], 'English': [], 'Chemistry': []}
    #asks user if they wish to input, use existing, or get random data.
    random_or_input = input('To input data into a txt file, then print this data, type "input". \n'
                            'To use data from an existing txt file, type "existing". \n'
                            'To use random data from a txt file, type "random": ')

    if random_or_input == 'random' or random_or_input == 'input':
        with open(filename, 'w') as writing_file:
            #this would over write existing files if we created the file before looping through what the user input was.
            #opens a file to write. name of file is the one inputed into function.

           if random_or_input == 'input':
                #if user wishes to input data, loops through keys and takes user input for values. updates the dictionary.
               
                for classes_keys in classes_grades:
                    #loops through all keys
                    user_data = input('input a grade number for the the student. when done, type done. the class is: ' + classes_keys + ': ')
                    while user_data != 'done':
                        #appends values to key/class until user is done.
                        classes_grades[classes_keys].append(int(user_data))        #appends dictionary with users input
                        user_data = input('input a grade number for the the student. when done, type done. the class is: ' + classes_keys + ': ')
                    
           elif random_or_input == "random":
               #randomizez the values for they keys
               classes_grades = grades()
               
           for key, values in classes_grades.items():
                #writes updated dictionary into a txt file.
                #.items so we dont get value error. 
                writing_file.write(f"{key} ")
                for value in values:
                    writing_file.write(f"{value} ")
                writing_file.write(f"\n")
               
        writing_file.close() #closes file when done with all. if user didnt want to change/create txt, uses existing file.       

    # Open the file in read mode
    with open(filename, 'r') as read_file:
        # Read each line from the file and extract class grades
        for line in read_file:
            class_name, *grades_str = line.split()
            classes_grades[class_name] = [int(grade) for grade in grades_str]
    read_file.close()
    return classes_grades

    
if __name__ == "__main__":
    #if you wish to take from txt, use this:
    filename = 'input.txt'
    classes_grades = read_file_grade(filename)

    print(graph_all_classes(classes_grades))
    print(classes_statistics(classes_grades))
    print(math_histogram(classes_grades))

    
    #if you want all input to be from the .py file, use this:
    print(graph_all_classes(grades()))
    print(classes_statistics(grades()))
    print(math_histogram(grades()))
