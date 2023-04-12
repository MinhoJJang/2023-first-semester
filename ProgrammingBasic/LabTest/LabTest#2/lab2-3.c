#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

int main()
{
    int decimal_number;
    printf("Input the decimal number: ");
    scanf("%d", &decimal_number);

    // 2로 decimal number을 나누고 남은 숫자
    printf("Binary number: ");

    int k = 0;

    while (pow(2, k) <= decimal_number)
    {
        k++;
    }

    while (k >= 1)
    {
        double n = pow(2, k - 1);
        if (decimal_number - n >= 0)
        {
            printf("1");
            decimal_number -= n;
        }
        else
        {
            printf("0");
        }

        k--;
    }

    return 0;
}