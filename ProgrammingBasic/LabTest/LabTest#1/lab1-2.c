#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define a 25.5
#define b 10

int main()
{
    double x, z;
    printf("please enter one floating point number x: \n");
    scanf("%lf", &x);

    if (0 < x && x <= 1)
    {
        z = (a * x * x + b * x * x * x) / 3;
    }
    else
    {
        z = a * x * x * x;
    }

    printf("the result z is: %.2lf", z);
    return 0;
}