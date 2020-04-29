
# read file
def read_file(filename):
	words = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			words.append(line.strip())
	return words

# write file
def convert(words):
	new = []
	sb = None #預設值設成無
	for word in words: 
		if word == 'Allen':
			sb = 'Allen'
			continue
		elif word == 'Tom':
			sb = 'Tom'
			continue
		if sb: #如果sb有值
			new.append(sb + ": " + word)
	return new

def write_file(filename, words):
	with open(filename, 'w') as f:
		for word in words:
			f.write(word + '\n')


def main():
	words =	read_file('input.txt')
	words = convert(words) #取代、覆蓋
	write_file('output.txt', words)

main()
# read_file('input.txt')