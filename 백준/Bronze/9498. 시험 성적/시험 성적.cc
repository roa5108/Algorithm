#include <iostream>
using namespace std;

int main() {
	int score;
	cin >> score;
	if (90 <= score && score <= 100) cout << "A";
	else if (80 <= score && score <= 89) cout << "B";
	else if (70 <= score && score <= 79) cout << "C";
	else if (60 <= score && score <= 69) cout << "D";
	else if (score < 0 || score>100) return 0;
	else cout << "F";
	return 0;
}