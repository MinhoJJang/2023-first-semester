#include <stdio.h>

void foo(int *first, int *second)
{
    int temp;
    // swapping if first > second
    if (*first > *second)
    {
        temp = *first;
        *first = *second;
        *second = temp;
    }
    // squared if first = second
    else if (*first == *second)
    {
        *first *= *first;
        *second *= *second;
    }
}

int main()
{
    int a, b;
    // read inputs
    printf("First number: ");
    scanf_s("%d", &a);
    printf("Second number: ");
    scanf_s("%d", &b);
    // function call
    foo(&a, &b);
    // print the results
    printf("(Results)\n");
    printf("%d %d\n", a, b);

    return 0;
}
