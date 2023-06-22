import sys

def getChordURL(chord):
	res = 'https://tuneronline.ru/images/chords/guitar/max/'
	
	for char in chord:
		char = char.lower()
		if char == '#':
			res += 'diez'
		else:
			res += char
	
	res += '.jpg'
	return res

####################################################

if len(sys.argv) <= 2:
	print('usage: song.txt song.html')
	exit()

fin  = open(sys.argv[1], 'r')
fout = open(sys.argv[2], 'w')

for line in fin:
	for word in line.split():
		if True: # chord
			brackets = word[0] == '(' and word[-1] == ')'
			if brackets:
				word = word[1:-2]
				print('(', file=fout)
			
			print('<img src="{}" height="{}">'.format(getChordURL(word), 50), file=fout)
			
			if brackets:
				print(')', file=fout)
	print('<br>', file=fout)

fin.close()
fout.close()

print('Check result: {}!'.format(sys.argv[2]))
