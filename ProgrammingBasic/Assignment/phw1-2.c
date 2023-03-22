#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    int five_digit_num = 0; // the user's input, five-digit number
    int n1, n2, n3, n4, n5; // each variables are the individual digit of input digit numbers

    printf("enter the five-digit number: \n");
    scanf("%d", &five_digit_num);

    n5 = five_digit_num % 10;
    n4 = (five_digit_num / 10) % 10;
    n3 = (five_digit_num / 100) % 10;
    n2 = (five_digit_num / 1000) % 10;
    n1 = (five_digit_num / 10000);

    printf("%d   %d   %d   %d   %d", n1, n2, n3, n4, n5);

    return 0;
}