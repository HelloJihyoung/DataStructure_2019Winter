#include <iostream>
#include <deque>
#include <string>
using namespace std;

int main() {

	cin.tie(0);
	cin.sync_with_stdio(false);

	int n = 0;
	cin >> n;

	deque <int> deque;
	string cmd;

	for (int i = 0; i < n; i++) {

		cin >> cmd;

		if (cmd == "push_front") {
			int num;
			cin >> num;
			deque.push_front(num);
		}
		else if (cmd == "push_back") {
			int num;
			cin >> num;
			deque.push_back(num);
		}
		else if (cmd == "pop_front") {
			if (!deque.empty()) {
				cout << deque.front() << "\n";
				deque.pop_front();
			}
			else
				cout << "-1" << "\n";
		}
		else if (cmd == "pop_back") {
			if (!deque.empty()) {
				cout << deque.back() << "\n";
				deque.pop_back();
			}
			else
				cout << "-1" << "\n";
		}
		else if (cmd == "size") {
			cout << deque.size() << "\n";
		}
		else if (cmd == "empty") {
			if (!deque.empty()) {
				cout << "0" << "\n";
			}
			else
				cout << "1" << "\n";
		}
		else if (cmd == "front") {
			if (!deque.empty()) {
				cout << deque.front() << "\n";
			}
			else
				cout << "-1" << "\n";
		}
		else if (cmd == "back") {
			if (!deque.empty()) {
				cout << deque.back() << "\n";
			}
			else
				cout << "-1" << "\n";
		}

	}

	return 0;
}
