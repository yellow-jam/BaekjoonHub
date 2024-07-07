#include <iostream>

using namespace std;

int visit(int N, int r, int c) {
	
	if (N==0) return 0;
	
	int n1 = 1<<(N-1);
	int n2 = 1<<N;
	int small = n1*n1;
	
	if (r<n1 && c<n1) {  // 2분면 
		return visit(N-1, r, c);
		
	} else if (r<n1 && n1<c<n2) {  // 1분면 
		return small + visit(N-1, r, c-n1);
		
	} else if (n1<r<n2 && c<n1) {  // 3분면
		return small*2 + visit(N-1, r-n1, c);

	} else {  // 4분면
		return small*3 + visit(N-1, r-n1, c-n1);
	}
}

int main(void) {
	int N, r, c;
	cin >> N >> r >> c;
	
	cout << visit(N, r, c) << endl;
	
	return 0;
}