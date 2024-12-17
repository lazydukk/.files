#include <bits/stdc++.h>
#define int long long
using namespace std;

void rec(int n)
{
    cout << n << ' ';
    if (n == 1)
        return;
    if (n % 2 == 0)
        return rec(n / 2);
    return rec(3 * n + 1);
}

int32_t main()
{
#define judge
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int n;
    cin >> n;
    rec(n);
    return 0;
}