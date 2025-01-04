#include <iostream>
#include <vector>
using namespace std;

int main() {
	int N;
	cin >> N;
	vector<double> score(N, 0);

	int max = -1000;
	for (int i = 0; i < N; i++) {
		cin >> score[i];
		if (score[i] > max) max = score[i];
	}

	double sum = 0;
	for (int i = 0; i < N; i++) {
		score[i] = score[i] / max * 100;
		sum += score[i];
	}

	double avg = sum / N;
	cout << avg;
	return 0;
}