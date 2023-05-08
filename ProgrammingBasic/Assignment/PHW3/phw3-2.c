#include <stdio.h>

int main()
{
    int first_set[10], second_set[10], intersection_set[10];
    int intersection_size = 0;

    printf("Enter first set: ");
    for (int i = 0; i < 10; i++)
    {
        scanf("%d", &first_set[i]);
    }

    printf("Enter second set: ");
    for (int i = 0; i < 10; i++)
    {
        scanf("%d", &second_set[i]);
    }

    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            if (first_set[i] == second_set[j])
            {
                intersection_set[intersection_size++] = first_set[i];
                break;
            }
        }
    }

    printf("The Intersection set: ");
    for (int i = 0; i < intersection_size; i++)
    {
        printf("%d ", intersection_set[i]);
    }
    printf("\n");

    return 0;
}
