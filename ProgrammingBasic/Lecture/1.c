#include <stdio.h>
#define MAX 50
void main()
{
    int i, grades[MAX], minx, min, total = 0;
    float avg;
    for (i = 0; i < MAX; i++)
    {
        printf("type a grade\n");
        scanf("%d", &grades[i]);
    }
    for (i = 0; i < MAX; i++)
    {
        if (i == 0)
        {
            minx = 0;
            min = grades[0];
        }
        else if (grades[i] < min)
        {
            minx = i;
            min = grades[i];
        }
        total = total + grades[i];
    }
    avg = (float)total / MAX;
    printf(" lowest grade = %d, and average grade = %f", grades[minx], avg);
}