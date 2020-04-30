
# read file
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

# write file
def convert(lines):
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_image_count = 0
	viki_image_count = 0

	for line in lines:
		s = line.split(' ') #字串切割完，變成一個清單-存成s
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for msg in s[2:]:
					allen_word_count += len(msg)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for msg in s[2:]:
					viki_word_count += len(msg)
				
	print('allen_word: ', allen_word_count, '/ allen_sticker: ', allen_sticker_count, '/allen_image: ', allen_image_count)
	print('viki_word: ', viki_word_count, '/ viki_sticker: ', viki_sticker_count,'/viki_image: ', viki_image_count)


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	words =	read_file('LINE-Viki.txt')
	words = convert(words) #取代、覆蓋
	# write_file('output.txt', words)

main()
