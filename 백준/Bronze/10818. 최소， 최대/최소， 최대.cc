#include <iostream>
using namespace std;

int  main() {
	int N;
	cin >> N;
	int array[N];
	int max = -1000000;
	int min = 1000000;

	for (int i = 0; i < N; i++) {
		cin >> array[i];
		if (array[i] > max) {
			max = array[i];
		}
		if (array[i] < min) {
			min = array[i];
		}
	}
	
	cout << min<< " " << max;

}