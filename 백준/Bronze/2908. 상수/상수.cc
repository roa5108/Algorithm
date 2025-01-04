#include <iostream>
using namespace std;

int main() {
	string n1, n2, new_n1, new_n2;
	cin >> n1 >> n2;
	for (int i = 2; i >= 0; i--) {
		new_n1 += n1[i];
		new_n2 += n2[i];
	}
	cout << max(new_n1, new_n2);

	return 0;
}