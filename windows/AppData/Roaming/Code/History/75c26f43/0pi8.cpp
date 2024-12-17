#include <bits/stdc++.h>
using namespace std;

int noi(int n)
{
    if (n == 1)
        return 0;
    if (n % 2 == 0)
        return (1 + noi(n / 2));
    else
        return 1 + noi(3 * n + 1);
}

int main()
{
    int maxi = 0;
    for (int i = 1; i <= 1000000; i++)
        maxi = max(maxi, noi(i));
}