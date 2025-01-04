#include <iostream>
#include <vector>
using namespace std;

int main() {
	int N, M;
	int a, b;
	cin >> N >> M;
	vector<int> arr(N + 1, 0);

	for (int i = 1; i <= N; i++) {
		arr[i] = i;
	}
	
	for (int i = 0; i < M; i++) {
		cin >> a >> b;
		while (a < b) {
			swap(arr[a], arr[b]);
			a++;
			b--;
		}
	}

	for (int i = 1; i <= N; i++) cout << arr[i] << " ";
	return 0;
}