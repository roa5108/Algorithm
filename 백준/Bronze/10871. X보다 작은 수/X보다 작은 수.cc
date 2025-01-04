#include <iostream>
#include <vector>
using namespace std;

int main() {
	int N, X;
	cin >> N >> X;
	vector<int> A(N, 0);
	vector<int> B;
	for (int i = 0; i < N; i++) {
		cin >> A[i];
		if (A[i] < X) B.push_back(A[i]);
	}
	for (int i = 0; i < B.size(); i++) {
		cout << B[i] << " ";
	}
	return 0;
}