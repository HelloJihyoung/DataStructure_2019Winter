#include <iostream>
#include <string>
using namespace std;

int main()
{
	int house = 0; 
	cin >> house;
	int route = 1; 
	int num = 1; 
	int up = 6; 

	while (1) {
		if (house <= num)
			break;
		route++;
		num += up;
		up += 6;
	}
	cout << route;

	return 0;
}