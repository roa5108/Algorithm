#include <iostream>
using namespace std;

int main() {
	string str;
	cin >> str;
	int dif;
	int result = 0;
	int alp[26] = { 3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10 };
	for (int i = 0; i < str.size(); i++) {
		dif = str[i] - 'A';
		result += alp[dif];
	}
	cout << result;
	return 0;
}