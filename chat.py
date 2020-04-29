import os

# read file
def read_file(filename):
	words = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			words.append(line)
	return words

#convert file
def convert(words):
	new = []
	for word in words:
		if 'Allen' in word:
			sb = 'Allen'
			continue
		elif 'Tom' in word:
			sb = 'Tom'
			continue
		new.append(sb + ': '+ word)
	return new	

# write file
def write_file(filename, words):
	with open(filename, 'w') as f:
		for word in words:
			f.write(word + '\n')			 

def main():
	filename = 'input.txt'
	if os.path.isfile(filename):
		words =	read_file(filename)
	else:
		print('file not found...')
	words = convert(words)
	write_file('output.txt', words)


main()
# read_file('input.txt')