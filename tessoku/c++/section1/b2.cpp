#include <bits/stdc++.h>

using namespace std;

bool flag = false;

int main() {
    int A, B;
    cin >> A >> B;
    
    for (int i=A; i<=B; i++) {
        if (100%i==0) {
            flag = true;
            break;
        }
    }

    if (flag) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}

