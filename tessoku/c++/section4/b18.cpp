#include <bits/stdc++.h>

using namespace std;


int main() {

    int N, S;
    int As[100009];

    cin >> N >> S;

    for (int i = 1; i <= N; i++) {
        cin >> As[i];
    }

    bool dp[69][10009]; // N * S の配列を格納する

    // メモ：dp[i][j] は、i番目までの整数を使って、総和がjになるような組み合わせが存在するかどうかを表す

    // 初期化，カードが0枚の場合
    dp[0][0] = true;
    for (int j = 1; j <= S; j++) {
        dp[0][j] = false;
    }

    // メイン部分
    for (int i=1; i<=N; i++){
        for (int j=0; j<=S; j++){

            // i-1番目まででjが作れる時
            if (dp[i-1][j] == true){
                dp[i][j] = true;
            }

            // // i-1番目まででj-As[i]が作れる時
            // else if (dp[i-1][j-As[i]]){
            //     dp[i][j] = true;
            // }

            // i-1番目まででj-As[i]が作れる時，j-As[i]が負の時を考慮する
            else if ((j >= As[i]) && (dp[i-1][j-As[i]])){
                dp[i][j] = true;
            }

            else {
                dp[i][j] = false;
            }
        }
    }


    // 先にここでNoの場合を処理しておく
    if (dp[N][S]==false){
        cout << "-1" << endl;
    }

    // 以下，Yesの場合の処理

    // 復元
    int i = N;
    int j = S;

    vector<int> route;
    
    while (i > 0){

        // iを使わなくてもjが作れる時はスキップ
        if (dp[i-1][j] == true){
            i = i-1;
        }

        // iを使う時
        else {
            route.push_back(i);
            j = j - As[i];
            i = i-1;
        }
    }

    // 最短経路の長さを出力
    cout << route.size() << endl;

    // 最短経路を出力
    for (int i = route.size()-1; i>=0; i--){
        cout<< route[i] << ' ';
    }

}

/* 以下，不要 */

// #include <bits/stdc++.h>

// using namespace std;


// int main() {

//     int N, S;
//     int As[100009];

//     cin >> N >> S;

//     for (int i = 1; i <= N; i++) {
//         cin >> As[i];
//     }

//     int dp[69][10009]; // N * S の配列を格納する，ここではboolではなく，どこから来たかを格納する

//     // メモ：dp[i][j] は、i番目までの整数を使って、総和がjになるような組み合わせが存在するかどうかを表す

//     // 初期化，カードが0枚の場合
//     dp[0][0] = 0;
//     for (int j = 1; j <= S; j++) {
//         dp[0][j] = -1;
//     }

//     // メイン部分
//     for (int i=1; i<=N; i++){
//         for (int j=0; j<=S; j++){

//             // i-1番目まででjが作れる時
//             if (dp[i-1][j] >= 0){
//                 dp[i][j] = int(INFINITY); // ここは経路でスキップするところ
//             }

//             // i-1番目まででj-As[i]が作れる時，j-As[i]が負の時を考慮する
//             else if ((j >= As[i]) && (dp[i-1][j-As[i]] >= 0)){
//                 dp[i][j] = i-1;
//             }

//             else {
//                 dp[i][j] = -1;
//             }
//         }
//     }


//     if (dp[N][S] > 0){

//         vector<int> route;

//         // 逆に辿る
//         int i = N;
//         int j = S;
//         int tmp_cost;

//         while (true){

//             // ショートカットすべきところで無ければ
//             if (route.size() == 0 || (i != int(INFINITY))){
//                 route.push_back(i);
//             }

//             tmp_cost = j;
//             j = j - As[i];
//             i = dp[i][tmp_cost];
            
//             if (i==1){
//                 route.push_back(1);
//                 break;
//             }

//         }

//         // 最短経路の長さを出力
//         cout << route.size() << endl;

//         // 最短経路を出力
//         for (int i = route.size()-1; i>=0; i--){
//             cout<< route[i] << ' ';
//         }

//     }

//     else {
//         cout << -1 << endl;
//     }

// }

