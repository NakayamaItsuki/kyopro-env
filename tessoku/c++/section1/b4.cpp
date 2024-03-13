#include <bits/stdc++.h>

using namespace std;

int main() {

    string input;
    cin >> input;

    int decimal = 0;
    int length = input.length();

    // 1の位から順に2進数を10進数に変換
    for (int i = length-1; i >= 0; i--) {
        if (input[i] == '1') {
            decimal += pow(2, length-1-i);
        }
    }

    cout << decimal << std::endl;

}
