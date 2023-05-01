#include <stdio.h>

int main()
{
    int num, count = 0;
    printf("Enter an integer: ");
    scanf("%d", &num);

    // Loop through each digit of the number
    while (num != 0)
    {
        int digit = num % 10; // Get the last digit of the number
        if (digit == 9)
        {
            count++; // Increment the count if the digit is 9
        }
        num /= 10; // Remove the last digit from the number
    }

    printf("The number of 9s in the integer is: %d\n", count);
    return 0;
}
