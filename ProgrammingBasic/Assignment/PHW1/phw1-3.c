#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    // It seems that the variable name below alone can sufficiently explain the code.
    float weightInPounds = 0;
    float heightInInches = 0;
    float BMI = 0;

    printf("enter your weightInPounds: \n");
    scanf("%f", &weightInPounds);
    printf("enter your heightInInches: \n");
    scanf("%f", &heightInInches);

    BMI = weightInPounds * 703 / (heightInInches * heightInInches);

    printf("your BMI value is: %.2f\n", BMI);

    printf("BMI VALUES\n");
    printf("Underweight: less than 18.5\n");
    printf("Normal:         between 18.5 and 24.9\n");
    printf("Overweight:  between 25 and 29.9\n");
    printf("Obese:          30 or greater\n");

    return 0;
}