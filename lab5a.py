#!/usr/bin/env python3
# Author ID: jshopkins

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name,'r')
    read_data = f.read()
    f.close()
    return(read_data)

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    f = open(file_name,'r')
    read_data = f.readlines()
    f.close()
    for i in range(len(read_data)):
        read_data[i] = read_data[i].rstrip('\n')
    return(read_data)

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))