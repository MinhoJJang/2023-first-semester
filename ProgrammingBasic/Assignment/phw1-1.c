#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    float u = 0; // initial velocity
    float a = 0; // accleration of an object
    float t = 0; // the time has elapsed
    float v = 0; // the final velocity
    float s = 0; // the distance traversed

    printf("enter the initial velocity 'u': \n");
    scanf("%f", &u);

    printf("enter the accleration 'a': \n");
    scanf("%f", &a);

    printf("enter the time has elasped 't': \n");
    scanf("%f", &t);

    v = u + a * t;
    s = u * t + a * t * t / 2;

    printf("the final velocity 'v' = %.2f\n", v);
    printf("the distance traversed 's' = %.2f", s);

    return 0;
}