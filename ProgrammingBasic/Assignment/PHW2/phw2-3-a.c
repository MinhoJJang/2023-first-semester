#include <stdio.h>

int main()
{
    int num, i;
    long long fact = 1; // initialize fact to 1, since 0! = 1

    printf("Enter a non-negative integer: ");
    scanf("%d", &num);

    // check if the input is negative
    if (num < 0)
    {
        printf("Error: negative integers do not have factorials.\n");
    }
    else
    {
        // compute the factorial using a loop
        for (i = 1; i <= num; i++)
        {
            fact *= i; // multiply fact by i on each iteration
        }

        printf("%d! = %lld\n", num, fact); // print the result
    }

    return 0;
}
