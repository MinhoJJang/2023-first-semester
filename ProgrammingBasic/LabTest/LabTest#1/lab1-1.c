#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    double side;
    printf("please input side of a square: \n");
    scanf("%lf", &side);

    printf("the square's area: %.2lf\n", side * side);
    printf("the square's perimeter: %.2lf", 4 * side);
    return 0;
}