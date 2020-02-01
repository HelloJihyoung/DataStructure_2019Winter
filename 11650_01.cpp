#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int num;
	scanf("%d", &num);

	vector<pair<int, int>> loc(num);

	for (int i = 0; i < num; i++)
	{
		scanf("%d, %d\n", loc[i].first >> loc[i].second);
	}

	sort(loc.begin(), loc.end());

	for (int i = 0; i < num; i++) {
		printf("%d, %d\n", loc[i].first >> loc[i].second);

	}

	return 0;

}