#include <stdio.h>

int main()
{
    float input[10];
    float sum = 0;
    for (int i = 0; i < 10; i++)
    {
        scanf("%f", &input[i]);
        sum += input[i];
    }

    int idx = 0;
    while (2)
    {
        printf("2\n");
        idx++;
        if (idx > 5)
        {
            break;
        }
    }

    printf("sum = %.2f, avg = %.2f \n", sum, sum / 10);
    return 0;
}