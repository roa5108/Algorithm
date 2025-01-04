#include <iostream>
#include <vector>
using namespace std;

int main() {
	string S;
	cin >> S;
	vector<int> arr(26, -1);
	for (int i = 0; i < S.size(); i++) {
		if (arr[S[i] - 97] == -1) {
			arr[S[i] - 97] = i;
		}
	}

	for (int i = 0; i < 26; i++) {
		cout << arr[i] << " ";
	}
	return 0;
}