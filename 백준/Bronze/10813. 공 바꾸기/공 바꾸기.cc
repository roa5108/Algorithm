#include <iostream>
#include <vector>
using namespace std;

int main() {
	int N, M;
	int i, j;
	cin >> N >> M;
	vector<int> bag(N + 1); //중요! 공이 1부터 시작이기 때문에 N+1 (0은 사용안함)
	for (int b = 1; b <= N; b++) {
		bag[b] = b;
	}

	int temp;
	for (int a = 0; a < M; a++) {
		cin >> i >> j;
		temp = bag[i];
		bag[i] = bag[j];
		bag[j] = temp;
	}
	for (int c = 1; c <= N; c++) 
		cout << bag[c] << " ";
	return 0;
}