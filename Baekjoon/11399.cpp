#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
	int N;
	cin >> N;

	int sum = 0;

	int *time = new int[N];

	for (int i = 0; i < N; i++) {
		cin >> time[i];
	}

	sort(time, time + N);	

	for (int i = 0; i <N; i++) {
		for (int j = 0; j <= i; j++) {
			sum += time[j];
		}
	}

	printf("%d\n", sum);

	return 0;
}