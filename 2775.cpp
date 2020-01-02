#include <iostream>
using namespace std;

int apt[15][15];
int main()
{
	
	int size, k, n;
	cin >> size;

	for (int i = 1; i < 15; i++) {
		apt[0][i] = i;
	}
	for (int i = 1; i < 15; i++) {
		for (int j = 1; j < 15; j++) {
			apt[i][j] = apt[i][j - 1] + apt[i - 1][j];
		}
	}

	for (int i = 0; i < size; i++) {
		cin >> k >> n;
		cout << apt[k][n] << endl;
	}
}