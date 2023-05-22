#include <stdio.h>

int main()
{
    float *fptr;
    int *iptr;
    float fvalue;
    int ivalue;

    ivalue = 200;
    fvalue = 100.55;

    iptr = &ivalue;
    fptr = &fvalue;

    printf("iptr=%p, &iptr=%p, *iptr=%d, &ivalue=%p", iptr, &iptr, *iptr, &ivalue);
    return 0;
}