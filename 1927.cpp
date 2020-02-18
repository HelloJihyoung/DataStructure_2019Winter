#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {

	cin.tie(0);
	cin.sync_with_stdio(false);

	int N;
	cin >> N;

	priority_queue <int,vector <int>, greater<int>> queue;

	int x;
	for (int i = 0; i < N; i++) {
		cin >> x;
		if ((x == 0) && queue.empty())
			cout << "0\n";
		else if (x != 0) {
			queue.push(x);
		}
		else {
			cout << queue.top() << "\n";
			queue.pop();
		}
	}
	return 0;
}