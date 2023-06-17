#include <iostream>
#include <sstream>

using namespace std;

string getChordURL(string chord) {
	string res = "https://tuneronline.ru/images/chords/guitar/max/";
	for (int i = 0; i < chord.size(); i++) {
		chord[i] = tolower(chord[i]);
		if (chord[i] == '#') res += "diez";
		else res.push_back(chord[i]);
	}
	res += ".jpg";
	return res;
}
const int IMG_SIZE = 50;

int main() {
	string word;
	while (getline(cin, word)) {
		stringstream ss;
		ss << word;
		
		while (ss >> word) {
			if (true) { // chord
				bool brackets = (word.front() == '(' && word.back() == ')');
				if (brackets) word = word.substr(1, word.size() - 2);
				
				if (brackets) cout << '(';
				cout << "<img src=\"" << getChordURL(word) << "\" height=\"" << IMG_SIZE << "\">" << endl;
				
				if (brackets) cout << ')';
			}
		}
		
		cout << "<br>" << endl;
	}
	
	return 0;
}
