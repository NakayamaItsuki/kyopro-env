


#include <bits/stdc++.h>

using namespace std;


int dp[209][209]; // dp[i][j] := マス[i][j]におけるエネルギーの最大値

int main() {

    int H, W;
    // string A[209][209];
    char A[209][209];

    int N;

    int R[309], C[309], E[309];

    cin >> H >> W;

    int S_x=0, S_y=0, T_x=0, T_y=0;


    for(int i = 1; i <= H; i++){
        for(int j = 1; j <= W; j++){
            cin >> A[i][j];

            if (A[i][j] == 'S'){
                S_x = i;
                S_y = j;
            }
            else if (A[i][j] == 'T'){
                T_x = i;
                T_y = j;
            }
        }
    }


    // cout << S_x << S_y << T_x << T_y << endl;


    cin >> N;

    for(int i = 1; i <= N; i++){
        cin >> R[i] >> C[i] >> E[i];
        // dp[R][C] = max(dp[R][C], E);
    }

    int medicine[209][209];

    for (int i=1; i<=N; i++){
        medicine[R[i]][C[i]] = E[i];
    }

    // 初期化
    for(int i = 0; i <= H; i++){
        for(int j = 0; j <= W; j++){
            dp[i][j] = -1;
        }
    }

    // // スタート地点のエネルギーは0
    // dp[S_x][S_y] = 0;

    // スタート地点に薬があるか
    // if (medicine[S_x][S_y] > 0){
    //     dp[S_x][S_y] = max(dp[S_x][S_y], medicine[S_x][S_y]);
    // }
    // else{
    //     cout << "No" << endl;
    //     return 0;
    // }

    // cout << dp[S_x][S_y] << endl;


    // for(int i = 1; i <= H; i++){
    //     for(int j = 1; j <= W; j++){
    //         // cout << dp[i][j] << " ";
    //         if (dp[i][j] == -1){
    //             continue;
    //         }

    //         // 4方向を探索
    //         for(int k = -1; k <= 1; k++){
    //             for(int l = -1; l <= 1; l++){
    //                 if (k == 0 && l == 0){
    //                     continue;
    //                 }
    //                 if (k==1 && l==1){
    //                     continue;
    //                 }
    //                 if (k==1 && l==-1){
    //                     continue;
    //                 }
    //                 if (k==-1 && l==1){
    //                     continue;
    //                 }
    //                 if (k==-1 && l==-1){
    //                     continue;
    //                 }

    //                 int nx = i + k;
    //                 int ny = j + l;

    //                 // 範囲外
    //                 if (nx < 1 || nx > H || ny < 1 || ny > W){
    //                     continue;
    //                 }

    //                 // 壁
    //                 if (A[nx][ny] == '#'){
    //                     continue;
    //                 }

    //                 // 薬があるか
    //                 if (medicine[nx][ny] > 0){
    //                     dp[nx][ny] = max({dp[nx][ny], dp[i][j]-1, medicine[nx][ny]});
    //                 }
    //                 else{
    //                     dp[nx][ny] = max(dp[nx][ny], dp[i][j]-1);
    //                 }
    //             }
    //         }
    //     }
    //     // cout << endl;
    // }

    // Sからスタート，前後左右に幅優先探索を行い，dpを更新していく
    queue<pair<int, int>> que;
    que.push(make_pair(S_x, S_y));
    dp[S_x][S_y] = 0;

    // スタート地点に薬があるか
    if (medicine[S_x][S_y] > 0){
        dp[S_x][S_y] = max(dp[S_x][S_y], medicine[S_x][S_y]);
    }
    else{
        cout << "No" << endl;
        return 0;
    }

    static const int dx[] = {1, 0, -1, 0};
    static const int dy[] = {0, 1, 0, -1};

    while (!que.empty()){
        int x = que.front().first;
        int y = que.front().second;
        que.pop();

        for (int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 1 || nx > H || ny < 1 || ny > W){
                continue;
            }

            if (A[nx][ny] == '#'){
                continue;
            }

            if (dp[nx][ny] == -1){
                dp[nx][ny] = dp[x][y] - 1;
                if (medicine[nx][ny] > 0){
                    dp[nx][ny] = max(dp[nx][ny], medicine[nx][ny]);
                }
                que.push(make_pair(nx, ny));
            }

            else{
                dp[nx][ny] = max(dp[nx][ny], dp[x][y] - 1);
                if (medicine[nx][ny] > 0){
                    dp[nx][ny] = max(dp[nx][ny], medicine[nx][ny]);
                }
                que.push(make_pair(nx, ny));
            }

            // if (dp[nx][ny] == -1){
            //     dp[nx][ny] = dp[x][y] - 1;
            //     if (medicine[nx][ny] > 0){
            //         dp[nx][ny] = max(dp[nx][ny], medicine[nx][ny]);
            //     }
            //     que.push(make_pair(nx, ny));
            // }
        }
    }


    // ゴール地点に到達できるか
    if (dp[T_x][T_y] == -1){
        cout << "No" << endl;
    }
    else{
        cout << "Yes" << endl;
        // cout << dp[T_x][T_y] << endl;
    }




    return 0;
}
