#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int a, b, c, result;
	cin >> a >> b >> c;
	if (a == b && b == c) {
		result = 10000 + a * 1000;
		cout << result;
	}
	else if (a == b && b!= c) {
		result = 1000 + a * 100;
		cout << result;
	}
	else if (a == c && c!= b) {
		result = 1000 + a * 100;
		cout << result;
	}
	else if (b == c && c!= a) {
		result = 1000 + b * 100;
		cout << result;
	}
	else {
		result = max({ a, b, c }) * 100;
		cout << result;
	}
	return 0;
}