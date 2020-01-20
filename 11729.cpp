#include <iostream>

using namespace std;

void Towers(int num, int from, int spare, int to) {
	if (num == 1)
		printf("%d %d\n",from, to);
	else {
		Towers(num - 1, from, to, spare);
		Towers(1, from, spare, to);
		Towers(num - 1, spare, from, to);
	}
}
int main()
{
	int num;
	scanf("%d", &num);
	printf("%d\n", (1 << num) - 1);

	Towers(num, 1, 2, 3);
	
	return 0;
}