#include <iostream>
#include <string>
using namespace std;

int main()
{
	string alpha;
	cin >> alpha;
	int cnt = 0;
	for (int i = 0; i < alpha.length(); i++) {
		switch (alpha[i])
		{
		case 'c':
			if (alpha[i + 1] == '=' || alpha[i + 1] == '-')
				i++;
			break;
		case 'd':
			if (alpha[i + 1] == 'z' && alpha[i + 2] == '=')
				i+=2;
			else if (alpha[i + 1] == '-')
				i++;
			break;
		case 'l':
			if (alpha[i + 1] == 'j')
				i++;
			break;
		case 'n':
			if (alpha[i + 1] == 'j')
				i++;
			break;
		case 's':
			if (alpha[i + 1] == '=')
				i++;
			break;
		case 'z':
			if (alpha[i + 1] == '=')
				i++;
			break;
		}
		cnt++;
	}
	cout << cnt;
	return 0;
}