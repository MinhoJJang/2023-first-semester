#include <stdio.h>
#define MAX_SIZE 50

int findMax(int *arr, int size)
{
    int max = arr[0];
    for (int i = 1; i < size; i++)
    {
        if (max < arr[i])
        {
            max = arr[i];
        }
    }
    return max;
}

void normalizeArray(int *arr, int size, double *arr_out)
{
    int max = findMax(arr, size);

    for (int i = 0; i < size; i++)
    {
        arr_out[i] = arr[i] / (double)max;
    }
}

int main()
{
    int size;
    int arr[MAX_SIZE];
    int max;
    double arr_double[MAX_SIZE];

    printf("Enter the size of the array: ");
    scanf("%d", &size);

    printf("Enter the elements of the array: ");
    for (int i = 0; i < size; i++)
    {
        scanf("%d", &arr[i]);
    }

    max = findMax(arr, size);
    normalizeArray(arr, size, arr_double);

    printf("(Results)\n");
    printf("Max: %d\n", max);
    printf("Normalized array: ");
    for (int i = 0; i < size; i++)
    {
        printf("%.2lf ", arr_double[i]);
    }

    return 0;
}