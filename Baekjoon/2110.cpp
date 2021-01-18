#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int C, N;
	cin >> N >> C;

	int *home = new int[N];
	for (int i = 0; i < N; i++) {
		cin >> home[i];
	}

	sort(home, home + N);

	int left = 1;
	int right = home[N - 1] - home[0];
	int routeMAX = 0;

	while (left <= right) {
		int mid = (left + right) / 2;
		int cnt = 1;
		int start = home[0];

		for (int i = 1; i < N; i++) {
			if (home[i] - start >= mid) {
				cnt++;
				start = home[i];
			}
		}
		if (cnt >= C) {
			routeMAX = mid;
			left = mid + 1;
		}
		else
			right = mid - 1;
			
	}
	
	cout << routeMAX;

	return 0;
	
}
