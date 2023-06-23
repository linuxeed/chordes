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

notes = "abcdefgh"

####################################################

if len(sys.argv) <= 2:
	print('usage: song.txt song.html')
	exit()

fin  = open(sys.argv[1], 'r')
fout = open(sys.argv[2], 'w')

print('<meta charset="utf-8">', file=fout) # fix charset
print('<font face="sans-serif" size="3">', file=fout) # sans font

for line in fin:
	for word in line.split():
		brackets = word[0] == '(' and word[-1] == ')'
		if brackets:
			word = word[1:-2]
			print('(', file=fout)
		
		if word[0].lower() in notes:
			print(f'<img src="{getChordURL(word)}" height="40">', file=fout)
		else:
			print(word, file=fout)
		
		if brackets:
			print(')', file=fout)
	
	print('<br>', file=fout)

print('</font>', file=fout) # end sans font

fin.close()
fout.close()

print(f'Check result: {sys.argv[2]}!')
