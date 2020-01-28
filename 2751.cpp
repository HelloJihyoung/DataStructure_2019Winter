#include <iostream>
#include <vector>
using namespace std;

void merge(vector<int>& v, int start, int mid, int end) {
	
	vector<int> sort;
	int i = start, j = mid + 1, a = 0;
	
	while (i <= mid && j <= end) {
		if (v[i] < v[j]) sort.push_back(v[i++]);
		else sort.push_back(v[j++]);
	}

	while (i <= mid) sort.push_back(v[i++]);
	while (j <= end) sort.push_back(v[j++]);

	for (int k = start; k <= end; k++)
		v[k] = sort[a++];
}

void divide(vector<int>& v, int start, int end) {

	if (start < end) {
		int mid = (start + end) / 2;
		divide(v, start, mid);
		divide(v, mid + 1, end);
		merge(v, start, mid, end);
	}
}

int main() {

	vector<int> v;

	int num;
	scanf("%d", &num);

	for (int i = 0, a = 0; i < num; i++) {
		scanf("%d", &a);
		v.push_back(a);
	}


	divide(v, 0, num - 1);

	for (int i = 0; i < num; i++) {
		printf("%d\n", v[i]);
	}

	return 0;

}
