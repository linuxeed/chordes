import sys

NOTES = "abcdefgh"


def get_chord_url(chord):
	res = ''
	for char in chord.lower():
		if char in ('#', '♯'):
			res += 'diez'
		elif char in ('b', '♭'):
			res += 'b'
		else:
			res += char
	return f'https://tuneronline.ru/images/chords/guitar/max/{res}.jpg'


def big_font(x):
	return f'<font face="sans-serif" size="5">{x}</font>'


if len(sys.argv) <= 2:
	print('usage: song.txt song.html')
	exit(0)

fin = open(sys.argv[1], 'r')
fout = open(sys.argv[2], 'w')

print('<meta charset="utf-8">', file=fout)

print('<table>', file=fout)
for line in fin:
	print('<tr>\n<td>', file=fout)
	
	for word in line.split():
		brackets = word[0] == '(' and word[-1] == ')'
		if (brackets and word[1].lower() not in NOTES) or (not brackets and word[0].lower() not in NOTES):
			print(big_font(word), file=fout)
	
	print('</td>\n<td>', file=fout)
	
	for word in line.split():
		brackets = word[0] == '(' and word[-1] == ')'
		if brackets:
			word = word[1:-1]
			print(big_font('('), file=fout)
		
		if word[0].lower() in NOTES:
			print(f'<img src="{get_chord_url(word)}" height="90">', file=fout)
		
		if brackets:
			print(big_font(')'), file=fout)
	
	print('</td>\n</tr>', file=fout)
print('</table>', file=fout)

print('</font>', file=fout)

fin.close()
fout.close()

print(f'Check result: {sys.argv[2]}!')
