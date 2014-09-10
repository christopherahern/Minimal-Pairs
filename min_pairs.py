# Find minimal pairs from a pronunciation dictionary

def get_corpus(corpus_file):
	"""Get corpus file with orthography, part-of-speech, frequency"""
	corpus = {}
	for line in [item.strip() for item in open(corpus_file).readlines()]: # Loop through the lines of the file, skipping header
		parts = line.split('\t') # Split lines by delimiter in input file
		# Get orthography
 		orthography = parts[0].lower()
		# Add orthography, part-of-speech, and frequency to the corpus dictionary
		corpus[orthography.replace('\"','')] = [parts[1].replace('\"',''),parts[2].replace('\"','')]
	return corpus


def get_dictionary(dict_file, wordlist):
	"""Read in a pronunciation dictionary: key will be the pronunciation, value will be 
	orthography"""
	# Dictionary to store pronunciations and orthography
	pr_dict = {}
	# For each line in the pronunciation dictionary file 
	for line in [item.strip() for item in open(dict_file).readlines()]:
		# Split the line by the spaces
		parts = line.partition(' ')
		# The orthography is the first part
		# Variants are tagged: word(1)
 		orthography = parts[0].lower()
		# The pronunciation is everything else
		pronunciation = parts[-1][1:]
		# Store pronunciation and orthography in dictionary
		pr_dict[pronunciation] = orthography 
	# return dictionary
	return pr_dict 	

def get_seg_words(seg, dictionary, pre_include=None, pre_exclude=None, post_include=None, post_exclude=None):
	"""Get all the words in the dictionary that contain a segment"""
	seg_words = []
	# Loop through the pronunciations
	for pronunciation in dictionary.keys():
		parts = pronunciation.split(' ')
		reqs = 0
		# Loop through all occurences of the segment in the pronunciation
		for i in [i for i, x in enumerate(parts) if x == seg]:
			reqs = 1
			# Check to see if pronunciation violates any of the constraint
			#print pronunciation
			#print dictionary[pronunciation]
			if pre_include:
				if i - 1 > 0:
					if parts[i-1] not in pre_include:
						reqs = 0
			if pre_exclude:
				if i - 1 > 0:
					if parts[i-1] in pre-exclude:
						reqs = 0
			if post_include:
				if i < len(parts)-1:
					if parts[i + 1] not in post_include:
						reqs = 0
			if post_exclude:
				if i < len(parts)-1:
					if parts[i + 1] in post_exclude:
						reqs = 0
		# If pronunciation met all requirements add it to list
		if reqs:
			seg_words.append(pronunciation)
	return seg_words
	
def get_minimal_pairs(seg1, seg2, dictionary, corpus, pre_include=[],pre_exclude=[], post_include=[], post_exclude=[]):
	"""Find all minimal pairs for two segments based on a pronunciation dictionary"""
	# Output to a file: seg1_seg2.prs

	f = open(seg1 +'_'+ seg2 + '.prs', 'w')
	# columns: word, segment, pair number
	f.write('Word' + '\t' + 'Segment' + '\t' + 'Pair' + '\t' + 'POS' + '\t' + 'Freq' + '\t' + 'Min' + '\n')
	# Get all the words that have the two segments
	seg1_words = get_seg_words(seg1, dictionary, pre_include, pre_exclude, post_include, post_exclude)
	seg2_words = get_seg_words(seg2, dictionary, pre_include, pre_exclude, post_include, post_exclude)
	# Keep track of the number of pairs
	counter = 0
	# For each of the words with seg1, see if it has a minimal pair
	for i, word in enumerate(seg1_words):
		word2 = word.replace(seg1, seg2)
		# Does the word appear in the seg2 words
		if word2 in seg2_words:
			# Get orthography for both words
			orth1 = dictionary[word]
			orth2 = dictionary[word2]
			# Make sure the two are not variants of the same word
			if orth1 != orth2:
				if orth1 in corpus.keys() and orth2 in corpus.keys():
					print orth1, orth2
					pair_min = str(min(int(corpus[orth1][1]), int(corpus[orth2][1])))
					counter += 1
					# write first member of pair
					f.write(orth1 + '\t'+ seg1 + '\t' + str(counter) + '\t' +  corpus[orth1][0] + '\t' + corpus[orth1][1] +  '\t' + str(pair_min) + '\n')
					# write second member of pair
					f.write(orth2 + '\t'+ seg2 + '\t' + str(counter) + '\t' +  corpus[orth2][0] + '\t' + corpus[orth2][1] +  '\t' + str(pair_min) + '\n')
