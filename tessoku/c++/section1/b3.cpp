#include <bits/stdc++.h>

using namespace std;

bool flag = false;

int main() {
    int N;
    int As[100];

    cin >> N;

    for (int i=0; i<N; i++) {
        cin >> As[i];
    }
    
    int sum;

    for (int i=0; i<N; i++) {
        for (int j=i+1; j<N; j++) {
            for (int k=j+1; k<N; k++) {
                sum = As[i] + As[j] + As[k];
                if (sum == 1000){
                    flag = true;
                    break;
                }
            }
        }
    }

    if (flag) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}

