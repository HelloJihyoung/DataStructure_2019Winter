#include <iostream>
#include <stack>
#include <string>
using namespace std;

bool vps(string cmd) {
	
	stack <char> stack;
	int length = cmd.length();
	for (int i = 0; i < length; i++) {
		char c = cmd[i];
		if (c == '(') {
			stack.push(cmd[i]);
		}
		else {
			if (!stack.empty())
				stack.pop();
			else
				return false;
		}
	}
	return stack.empty();
}
int main() {

	int n;
	cin >> n;
	
	for (int i = 0; i < n; i++) {
		string cmd;
		cin >> cmd;

		if (vps(cmd)) 
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}

	return 0;
}