#include <iostream>
#include <queue>
using namespace std;

int main() {

	cin.tie(0);
	cin.sync_with_stdio(false);

	int N;
	cin >> N;

	priority_queue <int>  MaxQueue;
	priority_queue <int, vector <int>, greater<int>> MinQueue;

	int x;
	for (int i = 0; i < N; i++) {
		cin >> x;
		
		if (MaxQueue.size() == 0)
			MaxQueue.push(x);
		else {
			if (MinQueue.size() < MaxQueue.size()) {
				MinQueue.push(x);
			}
			else
				MaxQueue.push(x);
			
			if (MaxQueue.top() > MinQueue.top()) {
				int maxtop = MaxQueue.top();
				int mintop = MinQueue.top();
				MaxQueue.pop();
				MinQueue.pop();
				MaxQueue.push(mintop);
				MinQueue.push(maxtop);

			}

		}

		cout << MaxQueue.top() <<'\n';
	}
	return 0;
}