"""Individual class

This script allows the user to create the chromosome with diffrents ways.

This script requires only `random` library.

This file can also be imported as a module and contains the following
functions:

    * get_spreadsheet_cols - returns the column headers of the file
    * main - the main function of the script
"""

import random
import string


BINARIES_ENCODING = 'binaries'
DIGITS_ENCODING = 'digits'
BOOLEANS_ENCODING = 'booleans'
LETTERS_ENCODING = 'letters'
CUSTOM_ENCODING = 'custom'


def create_binary_individual(long):
    genes = []
    i = 0
    while i<long:
        genes.append(str(random.randint(0,1)))
        i+=1
    return genes


def create_individual_from_values(long, encoding):
    if encoding == BOOLEANS_ENCODING:
        values = ['True', 'False']

    if encoding == DIGITS_ENCODING:
        values = list(string.digits)

    if encoding == LETTERS_ENCODING:
        values = list(string.ascii_uppercase)

    genes = []
    i = 0
    while i<long:
        genes.append(random.choice(values))
        i+=1
    return genes

def create_individual_from_list(long, mylist):
    genes = []
    i = 0
    while i<long:
        genes.append(str(random.choice(mylist)))
        i+=1
    return genes

class Individual(object):
    def __init__(self):
        self.genes = []
        self.fitness = 0

    def get_size(self):
        return self.genes.__len__()
    
    def create_individual(self, long, encoding, extra=[]):
        if encoding not in [BINARIES_ENCODING, DIGITS_ENCODING, BOOLEANS_ENCODING, LETTERS_ENCODING, CUSTOM_ENCODING]:
            encoding = BINARIES_ENCODING

        if encoding == CUSTOM_ENCODING and len(extra)==0:
            encoding = BINARIES_ENCODING
        
        if encoding == BINARIES_ENCODING:
            self.genes = create_binary_individual(long)
        
        if encoding in [BOOLEANS_ENCODING, DIGITS_ENCODING, LETTERS_ENCODING]:
            self.genes = create_individual_from_values(long,encoding)

        if encoding == CUSTOM_ENCODING:
            self.genes = create_individual_from_list(long, extra)
        
    def __repr__(self):
        return repr(
            {
                'Individual' : self.genes,
                'Fitness' : self.fitness
            }
        )


