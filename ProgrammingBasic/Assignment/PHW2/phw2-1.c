#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

int main()
{
    int num; // reads an integer
    printf("Enter an integer: ");
    scanf("%d", &num);
    int root_n = sqrt(num); // square root n

    if (num == 1) // if n == 1, n is not prime
    {
        printf("n = %d is not a prime", num);
    }
    else if (num == 2) // if n == 2, n is prime
    {
        printf("n = %d is a prime", num);
    }
    else
    {
        // if n >= 3, check all the integer from 3 to root_n. root_n is for optimization. Because we don't have to check all the numbers from 3 to n to confirm n is divided by i.

        /*
        Proof:

        n = a * b(a != 1, b != 1, a<=b), let's assume a and b is bigger than sqrt(n) = k. so it can be represented like this:
        a = k + Q, b = k + P (Q,P is positive integer).
        But,

         a*b = k*k
         (k+Q)(k+P) = k*k

         is not true.
        So Q and P can't be a positive integer. It means if we check the integers 1 from k, we must can find a(a<=b).
        */
        for (int i = 2; i <= root_n; i++)
        {
            if (num % i == 0)
            {
                // then it's not a prime
                printf("n = %d is not a prime, divided by %d", num, i);
                return 0;
            }
        }
        // if check it all, then n is a prime
        printf("n = %d is a prime", num);
    }
    return 0;
}