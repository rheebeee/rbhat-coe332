#!/usr/bin/env python3
import json
import random
import sys

def breed(parent1, parent2):

    parents=[]
    numbers=[]
    parents.append(parent1)
    parents.append(parent2)
    
    for i in range(5):
        value= random.randint(0,1)
        numbers.append(value)

    child= {}
    child['head']= parents[numbers[0]]['head']
    child['body']= parents[numbers[1]]['body']
    child['arms']= parents[numbers[2]]['arms']
    child['legs']= parents[numbers[3]]['legs']
    child['tail']= parents[numbers[4]]['tail']

    return child

def main():

    with open(sys.argv[1], 'r') as f:
        animal_dict = json.load(f)
    
    parentOne= random.choice(animal_dict['animals'])
    parentTwo= random.choice(animal_dict['animals'])

    print('The parents are: ')
    print(parentOne)
    print(parentTwo)
    print('The child is: ')
    print(breed(parentOne, parentTwo))
    
    
    
if __name__ == '__main__':
    main()
