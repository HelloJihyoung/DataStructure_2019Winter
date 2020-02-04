#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main() {

	int n;
	cin >> n;
	
	stack <int> stack;
	string cmd;

	for (int i = 0; i < n; i++) {
		
		cin >> cmd;
		if (cmd == "push") {
			int num;
			cin >> num;
			stack.push(num);
		}
		else if (cmd == "pop") {
			if (!stack.empty()) {
				cout << stack.top() << endl;
				stack.pop();
			}
			else
				cout << "-1" << endl;
		}
		else if (cmd == "size") {
			cout << stack.size() << endl;
		}
		else if (cmd == "empty") {
			if (!stack.empty()) {
				cout << "0" << endl;
			}
			else
				cout << "1" << endl;
		}
		else if (cmd == "top") {
			if (!stack.empty()) {
				cout << stack.top() << endl;
			}
			else
				cout << "-1" << endl;
		}
	}

	return 0;
}