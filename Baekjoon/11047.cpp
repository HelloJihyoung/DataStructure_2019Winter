#include <iostream>
using namespace std;

int main() {
	int sort;
	int pay;
	cin >> sort >> pay;

	int cnt = 0;

	int *money = new int[sort];
	for (int i = 0; i < sort; i++) {
		cin >> money[i];
	}

	for (int i = sort - 1; i >= 0; i--) {
		if (pay == 0)
			break;
		else {
			cnt += pay / money[i];
			pay %= money[i];
		}
	}

	cout << cnt;
		
	return 0;

}