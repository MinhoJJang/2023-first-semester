#include <stdio.h>

int main()
{
    const int a = 10;
    int value[1000][100];
    int rnum = 1000, cnum = 100;
    int rx, cx;
    int min;
    min = value[0][0];
    for (rx = 0; rx < rnum; rx = rx + 1)
        for (cx = 0; cx < cnum; cx = cx + 1)
        {
            if (min > value[rx][cx])
                min = value[rx][cx];
        }
}