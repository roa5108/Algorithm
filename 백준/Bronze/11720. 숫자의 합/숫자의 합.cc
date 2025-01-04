#include <iostream>
using namespace std;

int main() {
	int N;
	char num;
	cin >> N;
	int result = 0;
	for (int i = 0; i < N; i++) {
		cin >> num;
		result += num - '0';
	}
	cout << result;
	return 0;
}