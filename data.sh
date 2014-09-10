#!/bin/bash
# This script will:
# 1. Download a version of the Subtlex corpus with part-of-speech tags
# 2. Download a version of the Cmudict pronunciation dictionary
# 3. Get the frequency and dominant part-of-speech for content words from Subtlex
# 4. Remove punctuation, stress, and variant information from Cmudict
# 5. Create a list of words found in both Cmudict and Subtlex
clear
date
echo "Downloading Files"
# Download and unzip subtlex file
curl -s http://crr.ugent.be/papers/SUBTLEX-US_frequency_list_with_PoS_information_final_text_version.zip > subtlex.zip
unzip subtlex.zip 
mv SUBTLEX-US\ frequency\ list\ with\ PoS\ information\ text\ version.txt subtlex
rm subtlex.zip
# Download CMUdict and phoneme set
curl -s http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict.0.7a > cmudict
curl -s http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict.0.7a.phones | cut -f1 > cmuphones
echo "Downloaded Files"

# Get word, dominant POS, and frequency of dominant POS
# Only get words that are adjectives, adverbs, nouns, or verbs
# Exclude words that are letters (e.g. 'ae')
cp subtlex subtlex-original
cut -f1,10,11 subtlex | grep -iw 'adjective\|adverb\|noun\|verb' | fgrep -iwvf cmuphones > subtlex-pos
mv subtlex-pos subtlex
echo "Cleaned Subtlex"

# Remove lines that start with symbols
# Remove words with apostrophes or periods
cp cmudict cmudict-original
grep -v "^[;\"\!'\#\%\&(),:.?\/{}]\|'\|\.\|-" cmudict > cmudict-nopunct
mv cmudict-nopunct cmudict
# Remove stress and variant information: ABSOLVE  AH0 B Z AA1 L V vs. ABSOLVE(1)  AE0 B Z AA1 L V
sed -i -e 's/[0-9]*//g' cmudict
sed -i -e 's/(//g' cmudict
sed -i -e 's/)//g' cmudict

echo "Cleaned CMUdict"

echo "Get words common to Subtlex and CMUdict."
cut -f1 subtlex | tr [:lower:] [:upper:] > wordlist
fgrep -wf wordlist cmudict > cmudict-shared
mv cmudict-shared cmudict
rm wordlist
date

