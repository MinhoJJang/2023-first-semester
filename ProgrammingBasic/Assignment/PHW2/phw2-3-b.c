#include <stdio.h>
#include <math.h>

int fac(int num)
{
    int fact = 1;
    for (int i = 1; i <= num; i++)
    {
        fact *= i; // multiply fact by i on each iteration
    }
    return fact;
}

int main()
{
    double e = 1;    // initialize e to 1
    double term = 1; // initialize the first term to 1
    int n = 1;       // initialize the number of terms to 1

    // keep adding terms until the difference between the current estimate of e and the previous estimate is less than the smallest representable value of double
    do
    {
        e += term;           // add the current term to e
        n++;                 // increment the number of terms
        term /= fac(n);      // calculate the next term
    } while (e != e + term); // this condition is true when term is smaller than the smallest representable value of double
    // it means that double type cannot represent the value of term. so term is 0, then e != e+term is false, so it can go out loop

    printf("The value of e is: %.10lf\n", e);      // print the value of e with 10 decimal places
    printf("Number of terms calculated: %d\n", n); // print the number of terms calculated

    return 0;
}
