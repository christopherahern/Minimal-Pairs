# Introduction

This repository contains code for generating minimal pairs from a pronunciation
dictionary. 

# Instructions

## Data

To get the data in the desired format enter the following at the command line:

    ./data.sh

This will do several things:

* Download a version of the Subtlex corpus with part-of-speech tags
* Download a version of the Cmudict pronunciation dictionary
* Get the frequency and dominant part-of-speech for content words from Subtlex
* Remove punctuation, stress, and variant information from Cmudict
* Create a list of words found in both Cmudict and Subtlex	

The output files are the following: 

* cmudict is a revised pronunciation dictionary containing only words that have
 frequency info in subtlex
* subtlex is a list of words with the frequency of the most dominant 
part-of-speech

Note that the number of words that have pronunciations may be smaller than the
number of words that have frequencies. For example, compare:

    wc -l cmudict
    wc -l subtlex 

## Items 
	
To get minimal pairs do the following from the command line:

    from min_pairs import *
    subtlex = get_corpus('subtlex')
    cmudict = get_dictionary('cmudict', subtlex.keys())

We can get the minimal pairs relevant to particular mergers:

    # Get minimal pairs for the COT-CAUGHT distinction
    get_minimal_pairs('AO', 'AA', cmudict, subtlex, post_exclude=['R']) 
    # Get minimal pairs for the PIN-PEN merger
    get_minimal_pairs('IH', 'EH', cmudict, subtlex, post_include=['N', 'M', 'NG']) 

The output files will be stored in a file based on the names of the sounds 
(e.g. AO_AA.prs). The file will contain a list of minimal pairs along with 
frequencies and dominant pos
