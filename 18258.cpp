#include <iostream>
#include <queue>
#include <string>
using namespace std;

int main() {

	unsigned int n = 0;
	cin >> n;

	queue <int> queue;
	string cmd;

	for (int i = 0; i < n; i++) {

		cin >> cmd;

		if (cmd == "push") {
			int num;
			cin >> num;
			queue.push(num);
		}
		else if (cmd == "pop") {
			if (!queue.empty()) {
				cout << queue.front() << endl;
				queue.pop();
			}
			else
				printf("%d", -1);
		}
		else if (cmd == "size") {
			cout << queue.size() << endl;
		}
		else if (cmd == "empty") {
			if (!queue.empty()) {
				cout << "0" << endl;
			}
			else
				cout << "1" << endl;
		}
		else if (cmd == "front") {
			if (!queue.empty()) {
				cout << queue.front() << endl;
			}
			else
				printf("%d", -1);
		}
		else if (cmd == "back") {
			if (!queue.empty()) {
				cout << queue.back() << endl;
			}
			else
				cout << "-1" << endl;
		}

	}

	return 0;
}
