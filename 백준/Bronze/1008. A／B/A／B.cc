#include <iostream>
using namespace std;

int main() {
	double A, B, C;
	cin >> A >> B;
	C = A / B;
	cout.precision(9); //소수점 9자리까지 출력
	cout << fixed; //고정된 소수점 설정. 항상 9자리 출력하도록 고정
	cout << C;
	return 0;
}