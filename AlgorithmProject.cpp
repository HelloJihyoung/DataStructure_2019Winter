#include <fstream>
#include <sstream>
#include <cstring>
#include <string>
#include <algorithm>
#include <iostream>
#include <vector>
#include <time.h>
using namespace std;

int bruteCount = 0;
int KMPCount = 0;
int bubbleCount = 0;
int quickCount = 0;

int maxvalue(int a, int b, int c) { // 할인 금액 비교
	int k[3] = { a, b, c };
	int max = 0;
	for (int i = 0; i < 3; i++) {
		if (max < k[i]) max = k[i];
	}
	if (max == a) cout << "할인액이 가장 큰 카드는 국민 노리카드 입니다." << endl;
	else if (max == b) cout << "할인액이 가장 큰 카드는 카카오 뱅크 프렌즈 체크카드 입니다." << endl;
	else if (max == c) cout << "할인액이 가장 큰 카드는 신한 HeyYoung카드 입니다." << endl;

	return max;
}

inline void swap(vector<pair<string, int>> &a, int i, int j) { // 데이터 이동 위한 swap 함수
	pair<string, int> t = a[i]; a[i] = a[j]; a[j] = t;
}

void bubblesort(vector<pair<string, int>> &a) { //bubble sort
	for (int i = 0; i < a.size(); i++) { 
		bubbleCount++;
		for (int j = 1; j < a.size() - i; j++) {
			bubbleCount++;
			if (a[j - 1].second > a[j].second) {
				swap(a[j - 1], a[j]);
				bubbleCount ++;
			}
		}
	}
}

int partition(vector<pair<string, int>> &a, int l, int r) { // bubble sort - partition
	int i, j; pair<string, int> v;
	if (r > l) {
		v = a[l]; i = l; j = r + 1;
		for (;;) {
			while (a[++i].second < v.second)
				quickCount++;
			while (a[--j].second > v.second)
				quickCount++;
			if (i >= j) break;
			swap(a, i, j);

		}
		swap(a, j, l);
	}
	return j;
}

void quicksort(vector<pair<string, int>> &a, int l, int r) { //quicksort
	int j;
	if (r > l) {
		j = partition(a, l, r);
		quicksort(a, l, j - 1);
		quicksort(a, j + 1, r);
	}
}

void makegraph(int k) { // 그래프 생성
	for (int i = 0; i < k; i++) {
		cout << "■";
	}
}

int findString(string parent, string pattern) { // bruteforce 로 string 찾기
	int cnt = 0; // 출현 횟수를 세기 위한 변수
	int parentSize = parent.size() - pattern.size();
	int patternSize = pattern.size();

	for (int i = 0; i < parentSize - patternSize; i++) {
		bool finded = true;
		for (int j = 0; j < patternSize; j++) {
			bruteCount++;
			if (parent[i + j] != pattern[j]) {
				finded = false;
			}
		}
		if (finded) {
			cnt++;
		}
	}
	return cnt;
}

void checkBrute(string all, string arr[]) { //항목 분류 위해 문자열 검색
	int food = findString(all, arr[0]) + findString(all, arr[1]) + findString(all, arr[2]);
	int convien = findString(all, arr[3]);
	int coffee = findString(all, arr[4]);
	int internet = findString(all, arr[5]);
	int culture = findString(all, arr[6]) + findString(all, arr[13]);
	int deliver = findString(all, arr[7]);
	int bakery = findString(all, arr[8]);
	int phone = findString(all, arr[9]);
	int traffic = findString(all, arr[10]);
	int cosme = findString(all, arr[11]);
	int etc = findString(all, arr[12])+ findString(all, arr[14]);

	vector<pair<string, int>> sortB;
	sortB.push_back(make_pair("외식", food));
	sortB.push_back(make_pair("편의점", convien));
	sortB.push_back(make_pair("카페", coffee));
	sortB.push_back(make_pair("전자상거래", internet));
	sortB.push_back(make_pair("문화", culture));
	sortB.push_back(make_pair("배달", deliver));
	sortB.push_back(make_pair("베이커리", bakery));
	sortB.push_back(make_pair("통신", phone));
	sortB.push_back(make_pair("교통", traffic));
	sortB.push_back(make_pair("화장품", cosme));
	sortB.push_back(make_pair("기타", etc));

	//quicksort(sortB, 0, sortB.size()-1);
	bubblesort(sortB);
	for (int i = sortB.size() - 1; i >= 0; i--) {
		makegraph(sortB[i].second);
		cout << sortB[i].first << " : " << sortB[i].second + 1 ;
		cout << "\n";
	}

	cout << "당신은 " << sortB[sortB.size() - 1].first << "에 가장많은 소비를 했습니다!" << endl;
	cout << "\n" << endl;
}

vector<int> makeTable(string pattern) {
	int patternSize = pattern.size();
	vector<int> table(patternSize, 0);
	int j = 0;
	for (int i = 1; i < patternSize; i++) {
		while (j > 0 && pattern[i] != pattern[j]) {
			j = table[j - 1];
		}
		if (pattern[i] == pattern[j]) {
			table[i] = ++j;
		}
	}
	return table;
}

int KMP(string parent, string pattern) {
	vector<int> table = makeTable(pattern);
	int parentSize = parent.size();
	int patternSize = pattern.size();
	int j = 0;
	int cnt = 0;
	for (int i = 0; i < parentSize; i++) {
		while (j > 0 && parent[i] != pattern[j]) {
			j = table[j - 1];
			KMPCount++;
		}
		if (parent[i] == pattern[j]) j++;
		if (j == patternSize - 1) {
			j = table[j];
			KMPCount++;
			cnt++;
		}
	}
	return cnt;
}

int checkKMP(string all, string arr[]) { //항목 분류 위해 문자열 검색
	
	int food = KMP(all, arr[0]) + KMP(all, arr[1]) + KMP(all, arr[2]);
	int convien = KMP(all, arr[3]);
	int coffee = KMP(all, arr[4]);
	int internet = KMP(all, arr[5]);
	int culture = KMP(all, arr[6]) + KMP(all, arr[13]);
	int deliver = KMP(all, arr[7]);
	int bakery = KMP(all, arr[8]);
	int phone = KMP(all, arr[9]);
	int traffic = KMP(all, arr[10]);
	int cosme = KMP(all, arr[11]);
	int etc = KMP(all, arr[12]) + KMP(all, arr[14]);

	vector<pair<string, int>> sortB;
	sortB.push_back(make_pair("외식", food));
	sortB.push_back(make_pair("편의점", convien));
	sortB.push_back(make_pair("카페", coffee));
	sortB.push_back(make_pair("전자상거래", internet));
	sortB.push_back(make_pair("문화", culture));
	sortB.push_back(make_pair("배달", deliver));
	sortB.push_back(make_pair("베이커리", bakery));
	sortB.push_back(make_pair("통신", phone));
	sortB.push_back(make_pair("교통", traffic));
	sortB.push_back(make_pair("화장품", cosme));
	sortB.push_back(make_pair("기타", etc));

	quicksort(sortB, 0, sortB.size() - 1);
	//bubblesort(sortB);
	for (int i = sortB.size() - 1; i >= 0; i--) {
		makegraph(sortB[i].second);
		cout << sortB[i].first << " : " << sortB[i].second + 1;
		cout << "\n";
	}
	cout << "당신은 " << sortB[sortB.size()-1].first << "에 가장많은 소비를 했습니다!" << endl;
	cout << "\n" << endl;
	return 0;

}
//카드별 혜택 분석
int noricard(vector<pair<string, int>> &a) {
	int nori_discount = 0;
	for (int i = 0; i < a.size(); i++) {
		if (a[i].first == "CGV") {
			if ((a[i].second) >= 10000) {
				if (((a[i].second)*0.35) > 7000) nori_discount += 7000;
				else nori_discount += ((a[i].second)*0.35);
			}
		}
		else if (a[i].first == "휴대폰요금") {
			if ((a[i].second) < 50000) 	nori_discount += ((a[i].second)*0.05);
			else nori_discount += 2500;
		}
		else if (a[i].first == "지하철" || a[i].first == "티머니 개인택시") {
			if (((a[i].second) * 0.1) > 2000) 	nori_discount += 2000;
			else nori_discount += ((a[i].second) * 0.1);
		}
		else if (a[i].first == "스타벅스") {
			if ((a[i].second) >= 10000) {
				if (((a[i].second)*0.2) > 4000) nori_discount += 4000;
				else nori_discount += ((a[i].second)*0.2);
			}
		}
		else if (a[i].first == "GS25") {
			if ((a[i].second) >= 10000) {
				if (((a[i].second)*0.05) > 1000) nori_discount += 1000;
				else nori_discount += ((a[i].second)*0.05);
			}
		}
	}

	
	return nori_discount;
}
int kakaocard(vector<pair<string, int>> &a) {
	int kakao_discount = 0;
	for (int i = 0; i < a.size(); i++) {
		if (a[i].first == "CGV") {
			if ((a[i].second) >= 15000) {
				kakao_discount += 4000;
			}
		}
		else if (a[i].first == "휴대폰요금") {
			if ((a[i].second) >= 50000) 	kakao_discount += 3000;
		}
		else if (a[i].first == "스타벅스") {
			if ((a[i].second) >= 10000) kakao_discount += 1000;
		}
		else if (a[i].first == "씨유") {
			if ((a[i].second) >= 10000)	kakao_discount += 1000;
		}
		else if (a[i].first == "요기요") {
			if ((a[i].second) >= 20000)	kakao_discount += 2000;
		}
	}

	return kakao_discount;
}
int youngcard(vector<pair<string, int>> &a) {
	int young_discount = 0;

	for (int i = 0; i < a.size(); i++) {
		if (a[i].first == "CGV") {
			if ((a[i].second) >= 20000)	young_discount += 5000;
		}
		else if (a[i].first == "휴대폰요금") {
			if ((a[i].second) >= 50000) young_discount += 2000;
		}
		else if (a[i].first == "지하철") {
			young_discount += ((a[i].second) * 0.05);
		}
		else if (a[i].first == "스타벅스") {
			if ((a[i].second) >= 10000) young_discount += 1000;
		}
		else if (a[i].first == "GS25") {
			if ((a[i].second) >= 10000) young_discount += 1000;
		}
	}
	
	return young_discount;
}

int main() {
	vector <string> name; // 사용 장소명, 금액
	vector <int> money;
	vector <string> sort; // 가맹점 정보
	ifstream file("re.csv"); // 파일 불러오기
	string all; //불러온 전체 내용을 저장하는 all string
	string line; // txt파일을 한줄씩 받아옴
	string arr[15] = { "한식", "일반대중음식", "일식", "편의점", "커피전문점", "전자상거래","PC 게임방","배달", "제과점", "통신", "교통", "화장품", "기타", "영화관", "약국" };
	string s; // string 값 받아오기
	while (!file.eof()) { // txt파일 종료할때까지 아래 과정 반복
		getline(file, line);//getline함수를 이용하여 한줄씩 읽어옴
		stringstream f(line); // stringstream을 이용하여 문자열을 입력받아 저장
		int flag = 0;
		while (getline(f, s, ',')) { //,를 단위로 하여 단어 받음
			all += s;
			if (flag == 0) { // name
				name.push_back(s);
			}
			else if (flag == 2) { //money
				int n = atoi(s.c_str());
				money.push_back(n);
			}
			flag++;
		}
	}
	vector <pair<string, int>> list;
	int sum = 0;
	for (int i = 0; i < name.size(); i++) {
		list.push_back(pair<string, int>(name[i], money[i]));
		sum += money[i];
	}
	int lastmoney = 0;
	cout << "지난달 카드 사용 금액을 작성해 주세요 : ";
	cin >> lastmoney;
	while (lastmoney < 300000)
	{
		cout << "전월실적이 부족하여 할인 혜택을 받을 수 없습니다 :(" << "\n" << endl;
		cout << "지난달 카드 사용 금액을 작성해 주세요 : ";
		cin >> lastmoney;
	}

	cout << "-----------BruteForce----------" << endl;
	clock_t start_Brute = clock();
	checkBrute(all, arr); // BruteForce + BubbleSort
	clock_t end_Brute = clock();


	cout << "-----------KMP----------" << endl;
	clock_t start_KMP = clock();
	checkKMP(all, arr); // KMP + QuickSort
	clock_t end_KMP = clock();

	cout << "-***********************************" << endl;

	cout << "이번달 총 사용 금액은 " << sum << "원 입니다." << "\n";

	cout << "---------------------" << endl;
	cout << "국민 노리카드 할인 금액 : " << noricard(list) << endl;
	cout << "카카오 뱅크 프렌즈 체크카드 할인 금액 : " << kakaocard(list) << endl;
	cout << "신한 HeyYoung카드 할인 금액 : " << youngcard(list) << endl;
	cout << endl;
	int a = noricard(list);
	int b = kakaocard(list);
	int c = youngcard(list);

	maxvalue(a, b, c);


	cout << "\n************알고리즘 비교 횟수************" << endl;
	cout << "-----------문자열 탐색 알고리즘-----------" << endl;
	cout << "Brute-Force 비교횟수 : " << bruteCount << endl;
	cout << "KMP 비교횟수         : " << KMPCount << endl;
	cout << "--------------정렬 알고리즘--------------" << endl;
	cout << "QuickSort 비교횟수   : " << quickCount << endl;
	cout << "BubbleSort 비교횟수  : " << bubbleCount << endl;

	cout << "\n***************런타임 시간***************" << endl;
	printf("Brute Force + Bubble Sort Run Time : %lf\n", (double)(end_Brute - start_Brute) / CLOCKS_PER_SEC);
	printf("KMP + Quick Sort Run Time          : %lf\n", (double)(end_KMP - start_KMP) / CLOCKS_PER_SEC);
	file.close(); // 파일 닫기
	

	return 0;

}