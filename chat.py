import os

# read file
def read_file(filename):
	words = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			words.append(line)
	return words

# write file
def write_file(filename, words):
	sb = 'NB'
	with open(filename, 'w') as f:
		for word in words: 
			if 'Allen' in word:
				sb = 'Allen'
				# f.write(word.strip() + ': ')
			elif 'Tom' in word:
				sb = 'Tom'
				# f.write(word.strip() + ': ')
			else:
				f.write(sb + ': ' + word)			 

def main():
	filename = 'input.txt'
	if os.path.isfile(filename):
		words =	read_file(filename)
	else:
		print('file not found...')

	write_file('output.txt', words)


main()
# read_file('input.txt')