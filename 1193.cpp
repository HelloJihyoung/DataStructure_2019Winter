#include <iostream>
#include <string>
using namespace std;

int main()
{
	int x;
	cin >> x;
	int num = 1;
	int line = 0;
	while (true) {
		if (x - num <= 0)
			break;
		x -= num; 
		num++; 
		line++;
	}

		if (line % 2 == 0) {
			cout << line + 2 - x << '/' << x;
		}
		else {
			cout << x << '/' << line + 2 - x;
		}
	return 0;
}

