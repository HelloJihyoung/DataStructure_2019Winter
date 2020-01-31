#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int num;
	cin >> num;
	
	vector<pair<int, int>> loc(num); 

	for (int i = 0; i < num; i++)
	{
		cin >> loc[i].first >> loc[i].second;
	}

	sort(loc.begin(), loc.end());

	for (int i = 0; i < num; i++) {
		cout << loc[i].first << ' ' << loc[i].second << endl;
	}
	
	return 0;

}