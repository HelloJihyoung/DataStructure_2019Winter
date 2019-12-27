#include <iostream>
#include <string>
using namespace std;

int cnt = 0;

void check(string group) {
	
	for (int i = 0; i < group.length() - 1; i++) {
		if (group[i] != group[i + 1]) {
			for (int j = i + 1; j < group.length(); j++) {
				if (group[j] == group[i])
					return;
			}
		}
	}
	cnt++;
}
int main()
{
	int num;
	cin >> num;
	string group;

	for (int i = 0; i < num; i++) {
		cin >> group;
		check(group);
	}
	cout << cnt;
	return 0;
}