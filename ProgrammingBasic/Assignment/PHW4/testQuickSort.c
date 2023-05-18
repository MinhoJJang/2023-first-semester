#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <assert.h>

void swap(int *a, int *b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

int partition(int array[], int low, int high)
{
    int pivot = array[(low + high) / 2]; // pivot is middle element
    int i = low - 1;
    int j = high + 1;

    while (1)
    {
        do
        {
            i++;
        } while (array[i] < pivot);

        do
        {
            j--;
        } while (array[j] > pivot);

        if (i >= j)
            return j;

        swap(&array[i], &array[j]);
    }
}

void quickSort(int array[], int low, int high)
{
    if (low < high)
    {
        int pi = partition(array, low, high);

        quickSort(array, low, pi);
        quickSort(array, pi + 1, high);
    }
}

void printArray(int array[], int size)
{
    for (int i = 0; i < size; i++)
        printf("%d ", array[i]);
    printf("\n");
}

// Function to check if an array is sorted in ascending order or not
int isSorted(int arr[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        if (arr[i] > arr[i + 1])
        {
            return 0; // Not sorted
        }
    }
    return 1; // Sorted
}

// Test function for quickSort
void testQuickSort()
{
    // Seed for random values
    srand(time(0));

    // Test for multiple sizes
    for (int n = 1; n <= 10; n++)
    {
        int *arr = malloc(sizeof(int) * n);

        // Generate random values
        for (int i = 0; i < n; i++)
        {
            arr[i] = rand() % 1000; // Random values between 0 and 999
        }

        // Print the array before sorted
        printArray(arr, n);

        // Sort using quickSort
        quickSort(arr, 0, n - 1);

        // Print the array after sorted
        printArray(arr, n);

        // Verify if sorted correctly
        assert(isSorted(arr, n));

        // Free the allocated memory
        free(arr);
    }

    printf("All test cases passed!\n");
}

int main()
{
    testQuickSort();
    return 0;
}
