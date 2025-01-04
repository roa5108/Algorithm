#include <iostream>
#include <vector>
using namespace std;

int main() {
	int N, v;
	cin >> N;
	vector<int> num(N, 0);
	
	for (int i = 0; i < N; i++) {
		cin >> num[i];
	}
	cin >> v;
	int result = 0;
	for (int i = 0; i < num.size(); i++) {
		if (num[i] == v) result++;
	}
	cout << result;
	return 0;
}