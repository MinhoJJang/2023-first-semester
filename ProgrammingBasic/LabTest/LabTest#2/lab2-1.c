#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define THREE 3

int main()
{
    int num;
    int sum = 0;
    float average = 0;
    printf("Input the number of multiples: ");
    scanf("%d", &num);

    printf("Multiples: ");
    for (int i = 1; i <= num; i++)
    {
        sum += i * THREE;
        printf("%d", i * THREE);
        if (i < num)
        {
            printf(", ");
        }
        else
        {
            printf("\n");
        }
    }
    average = sum / num;
    printf("Sum: %d\n", sum);
    printf("Average: %.1f\n", average);
    return 0;
}