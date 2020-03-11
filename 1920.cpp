#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {

	cin.tie(0);
	cin.sync_with_stdio(false);

	int N;
	cin >> N;
	vector<int> num1(N);
	for (int i = 0; i < N; i++){
		cin >> num1[i];
	}

	int M;
	cin >> M;
	vector <int> num2(M);
	for (int i = 0; i < M; i++){
		cin >> num2[i];
	}

	sort(num1.begin(), num1.end());

	int cnt = 0;
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
			if (num1[j] == num2[i]) {
				cout << 1;
				cnt = 1;
				break;
			}
		}
		if (cnt == 0)
			cout << 0;
	}
	return 0;
}

