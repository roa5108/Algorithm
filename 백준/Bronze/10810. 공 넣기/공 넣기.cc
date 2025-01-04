#include <iostream>
#include <vector>
using namespace std;

int main() {
	int N, M;
	int i, j, k;
	cin >> N >> M;
	vector<int> bag(N);
	for (int a = 0; a < M; a++) {
		cin >> i >> j >> k;
		for (i; i <= j; i++) {
			bag[i-1] = k;
		}
	}
	for (int i = 0; i < bag.size(); i++) {
		cout << bag[i] << " ";
	}
	return 0;
}