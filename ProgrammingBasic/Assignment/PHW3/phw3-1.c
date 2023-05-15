#include <stdio.h>
#include <stdbool.h>

int main()
{
    int first_set[10], second_set[10], union_set[20];
    int union_size = 0;

    printf("Enter first set: ");
    for (int i = 0; i < 10; i++)
    {
        scanf("%d", &first_set[i]);
        union_set[union_size++] = first_set[i];
    }

    printf("Enter second set: ");
    for (int i = 0; i < 10; i++)
    {
        scanf("%d", &second_set[i]);

        bool is_unique = true;
        for (int j = 0; j < union_size; j++)
        {
            if (second_set[i] == union_set[j])
            {
                is_unique = false;
                break;
            }
        }
        if (is_unique)
        {
            union_set[union_size++] = second_set[i];
        }
    }

    // Sort the union_set array
    for (int i = 0; i < union_size - 1; i++)
    {
        for (int j = i + 1; j < union_size; j++)
        {
            if (union_set[i] > union_set[j])
            {
                int temp = union_set[i];
                union_set[i] = union_set[j];
                union_set[j] = temp;
            }
        }
    }

    printf("The Union set: ");
    for (int i = 0; i < union_size; i++)
    {
        printf("%d ", union_set[i]);
    }
    printf("\n");

    return 0;
}
