#include <iostream>
using namespace std;

int main() {
	int N;
	string S;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> S;
		cout << S[0] << S[S.size() - 1] << endl;
	}


	return 0;
}