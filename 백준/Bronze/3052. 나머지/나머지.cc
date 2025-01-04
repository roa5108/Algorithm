#include <iostream>
using namespace std;

int main() {
	int a[10] = { 0, };
	int ans[10];
	int cnt = 0;
	for (int i = 0; i < 10; i++) {
		cin >> a[i];
		ans[i] = a[i] % 42;
	}
	
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j <= i; j++) {
			if (ans[i] == ans[j] && i != j) {
				cnt--;
				break;
			}
		}
		cnt++;
	}
	cout << cnt;
	return 0;
}