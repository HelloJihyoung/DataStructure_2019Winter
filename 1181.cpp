#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
	int num;
	cin >> num;

	vector<pair<int, string>> word(num); 

	for (int i = 0; i < num; i++){
		cin >> word[i].second;
		word[i].first = word[i].second.size();
	}

	sort(word.begin(), word.end());

	for (int i = 0; i < num - 1; i++) {
		if (word[i].second == word[i + 1].second) {
			word.erase(word.begin() + i);
			num--;
			i--; // 동일 문자가 3회 이상 나올 경우를 대비
		}
	}

	for (int i = 0; i < num; i++) {
		cout << word[i].second << endl;
	}

	return 0;
}