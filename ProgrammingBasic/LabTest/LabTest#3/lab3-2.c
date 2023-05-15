#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define TRUE 0
#define FALSE 1
void main()
{
    int original_array[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int shuffled_array[10];

    // srand
    // shuffle
    int idx_arr[10] = {0};
    int arrIdx = 0;
    while (arrIdx <= 9)
    {
        int flag = TRUE;
        time_t current_time;
        current_time = time(NULL);
        srand(current_time);
        int idx = rand();
        idx %= 10;

        for (int j = 0; j < arrIdx; j++)
        {
            if (idx_arr[j] == idx)
            {
                flag = FALSE;
                continue;
            }
        }
        if (flag == TRUE)
        {
            idx_arr[arrIdx] = idx;
            arrIdx++;
        }
    }

    for (int i = 0; i < 10; i++)
    {
        shuffled_array[i] = original_array[idx_arr[i]];
    }

    // result
    printf("Original Array: ");
    for (int i = 0; i < 10; i++)
    {
        printf("%02d ", original_array[i]);
        printf("%02d ", idx_arr[i]);
    }
    printf("\nShuffled Array: ");
    for (int i = 0; i < 10; i++)
        printf("%02d ", shuffled_array[i]);
}