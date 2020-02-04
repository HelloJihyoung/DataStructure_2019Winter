#include <iostream>
#include <string>
#define MAX 100000
using namespace std;

int stack[MAX];

int main() {

	int n;
	cin >> n;

	int top = 0;
	string cmd;

	for (int i = 0; i < n; i++) {
		
		cin >> cmd;

		if (cmd == "push") {
			int num;
			cin >> num;
			stack[++top] = num;
		}
		else if (cmd == "pop") {
			if (top != 0) {
				cout << stack[top--] << endl;
			}
			else
				cout << "-1" << endl;
		}
		else if (cmd == "size") {
			cout << top << endl;
		}
		else if (cmd == "empty") {
			if (top != 0) {
				cout << "0" << endl;
			}
			else
				cout << "1" << endl;
		}
		else if (cmd == "top") {
			if (top != 0) {
				cout << stack[top] << endl;
			}
			else
				cout << "-1" << endl;
		}
	}

	return 0;
}