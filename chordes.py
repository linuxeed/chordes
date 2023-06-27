import sys

NOTES = "abcdefgh"
def getChordURL(chord):
	res = 'https://tuneronline.ru/images/chords/guitar/max/'
	
	for char in chord:
		char = char.lower()
		if char == '#' or char == '♯':
			res += 'diez'
		elif char == 'b' or char == '♭':
			res += 'b'
		else:
			res += char
	
	res += '.jpg'
	return res

if len(sys.argv) <= 2:
	print('usage: song.txt song.html')
	exit(0)

fin  = open(sys.argv[1], 'r')
fout = open(sys.argv[2], 'w')

print('<meta charset="utf-8">', file=fout)
print('<font face="sans-serif" size="3">', file=fout)
print('<table>', file=fout)

for line in fin:
	print('<tr><td>', file=fout)
	
	for word in line.split():
		brackets = word[0] == '(' and word[-1] == ')'
		if brackets:
			if not word[1].lower() in NOTES:
				print(word, file=fout)
		else:
			if not word[0].lower() in NOTES:
				print(word, file=fout)
	
	print('</td><td>', file=fout)
	
	for word in line.split():
		brackets = word[0] == '(' and word[-1] == ')'
		if brackets:
			word = word[1:-2]
			print('(', file=fout)
		
		if word[0].lower() in NOTES:
			print(f'<img src="{getChordURL(word)}" height="40">', file=fout)
		
		if brackets:
			print(')', file=fout)
	
	print('</td></tr>', file=fout)

print('</font>', file=fout)
print('</table>', file=fout)

fin.close()
fout.close()

print(f'Check result: {sys.argv[2]}!')
