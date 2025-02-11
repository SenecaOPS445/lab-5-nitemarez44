#!/usr/bin/env python3
# Author ID: [seneca_id]

def add(number1, number2):
    # Add two numbers together, return the result, if error return string 'error: could not add numbers'
    try:
        number1 = int(number1)
        number2 = int(number2)
        number1+number2
    except:
        return "error: could not add numbers"
    else:
        number1 = int(number1)
        number2 = int(number2)
        return number1+number2

def read_file(filename):
    # Read a file, return a list of all lines, if error return string 'error: could not read file'
    try:
        f = open(filename, 'r')
    except(FileNotFoundError,PermissionError):
        return "error: could not read file"

    else:
        f = open(filename,'r')
        read_data = f.readlines()
        f.close()
        
        return(read_data)


if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception