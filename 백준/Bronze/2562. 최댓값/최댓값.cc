#include <iostream>
using namespace std;

int main() {
	int n[10];
	int max = 0;
	int maxNth;
	for (int i = 1; i <= 9; i++) {
		cin >> n[i];
		if (n[i] > max) {
			max = n[i];
			maxNth = i;
		}
	}
	cout << max << "\n" << maxNth;
	return 0;
}