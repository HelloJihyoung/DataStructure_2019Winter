#include <iostream>
using namespace std;

int main() {
	int num;
	cin >> num;

	int *number = new int[num];
	for (int i = 0; i < num; i++) {
		cin >> number[i];
	}
	for (int i = 0; i < num; i++) {
		for (int j = i; j < num; j++) {
			if (number[i] >= number[j]) {
				int temp = number[i];
				number[i] = number[j];
				number[j] = temp;
			}
		}
	}
	for (int i = 0; i < num; i++) {
		cout << number[i] << endl;
	}


}