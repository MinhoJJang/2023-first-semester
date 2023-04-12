#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    int row;
    printf("Input the number of row: ");
    scanf("%d", &row);

    for (int i = 1; i <= row; i++)
    {
        for (int j = 0; j < row - i; j++)
        {
            printf(" ");
        }

        for (int n = 1; n < i; n++)
        {
            printf("%d", n);
        }

        printf("%d", i);

        for (int n = i - 1; n >= 1; n--)
        {
            printf("%d", n);
        }

        printf("\n");
    }

    return 0;
}