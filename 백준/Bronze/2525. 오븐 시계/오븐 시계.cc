#include <iostream>
using namespace std;

int main() {
	int A, B, time, calA, calB;
	cin >> A >> B;
	cin >> time;
	if (B + time < 60) {
		cout << A << " " << B + time;
	}
	else {
		calA = A + (B + time) / 60;
		calB = (B + time) % 60;
		if (calA >= 24) {
			calA = calA - 24;
			cout << calA << " " << calB;
		}
		else cout << calA << " " << calB;
	}
	return 0;
}