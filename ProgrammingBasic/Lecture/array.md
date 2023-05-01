# Array

## Why we are using array?

Compare following two codes, which one is better?

```c
int v1, v2, v3, ... , v100;

printf("type a value : ");
scanf("%d", &v1);

printf("type a value : ");
scanf("%d", &v2);

printf("type a value : ");
scanf("%d", &v3);

...

printf("type a value : ");
scanf("%d", &v100);
```

vs

```c
int v[100];

for(int i=0; i<100; i++){
    printf("type a value : ");
    scanf("%d", &v[i]);
}
```

Without a doubt, the latter one is much better than the former one.
It is more usable, comfortable and short. That's why we are using array.

## What is array?

Array is a collection of variables of the same data type. And it is announced and initialized by following code:

```c
int array[5] = {0,1,2,3,4};
```

it is not the only way to initialize the array, just one example. Let's check the array details.

1. the first element index of array is `0`
2. the last element index of array is `N-1`, N is the size of array.

   It is very important features of array, because we usually met overflow by misusing the array index.

   -> So, when we want to find 'k'th index, (while k is constant, 0<=k<=N-1)
   arr[k-1] is the exact value which we want to find.

3. the size of array must be delcared.

   Let's think about array which has a size of N, take it from user input using scanf().
   It seems to be able to make it.

   ```c
       int N;
       scanf("%d", &N);
       // int arr[N]; // Error
   ```

   But nope, it can't. The size of array must be a constant. This means that the computer must know the size of the array before creating it.

4. all array elements are stored in contiguous memory loactions.

   As we learned before, the size of int is 4byte. Let's assume that we make a array like this: `int arr[100]`. it takes up the contiguous memory locations, total 400 byte.

## Major use of an array

array is usually combined with loop, like the example as I aforementioned.
let's exercise with solving a problem below.

```text
Write a C program, using a for loop, that
reads in all values of an integer array
grade[50], and then, in a separate for loop,
finds and prints the lowest grade and
average grade.
```

solution:

```c
#include <stdio.h>
#define MAX 50
void main()
{
    int i, grades[MAX], min_idx, min, total = 0;
    float avg;
    for (i = 0; i < MAX; i++)
    {
        printf("type a grade\n");
        scanf("%d", &grades[i]);
    }
    min = grades[0];
    for (i = 1; i < MAX; i++)
    {
        if (grades[i] < min)
        {
            min_idx = i;
            min = grades[i];
        }
        total = total + grades[i];
    }
    avg = (float)total / MAX;
    printf(" lowest grade = %d, and average grade = %f", grades[min_idx], avg);
}
```

We should address array carefully since it may cause underflow and overflow. So we should check array range not to make OutOfBoundsException. Here's a nice tip how to make a good array by my experience, if the array have number of N value, just make a array with size of N+10. It may causes not initiallized value after N th element, but it can prevent overflow. I use it very frequently when I using the array. The number 10 is just an example.

## Advanced curriculum with using array and loop

when we use array and loop together, the size of array is frequently used, since it is used for initializing array and setting the maximum number of loop.

```c
#include <stdio.h>
void main()
{
    int num[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int total = 0;
    for (int a = 0; a < 10; a++)
        total += num[a];
    printf("total number is %d \n", total);
}
```

But if we want to change the array size, we should also change the loop function. So it is better to set the size of array by using `#define SIZE 10` keyword, like following code:

```c
#include <stdio.h>
#define SIZE 10
void main()
{
    int num[SIZE] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int total = 0;
    for (int a = 0; a < SIZE; a++)
        total += num[a];
    printf("total number is %d \n", total);
}
```

It has good software maintainablity.

# Copying an array

if we want to copy an array, just copying one by one using loop is a basic way.

```c
int main()
{
    int i, num1[5], num2[5];
    for (i = 0; i < 5; i++)
    {
        printf("\n type a number");
        scanf("% d", &num2[i]);
    }
    for (i = 0; i < 5; i++)
        num1[i] = num2[i];
    for (i = 0; i < 5; i++)
        printf("\n % d num2 = % d and num1 = % d", i, num2[i], num1[i]);
}
```

## 2-dimensional array

2-dimensional array is just an array that has row and column. So, it may use with nested loop.

```c
#include <stdio.h>

int main()
{
    int value[1000][100];
    int rnum = 1000, cnum = 100;
    int rx, cx;
    int min;
    min = value[0][0];
    for (rx = 0; rx < rnum; rx = rx + 1)
        for (cx = 0; cx < cnum; cx = cx + 1)
        {
            if (min > value[rx][cx])
                min = value[rx][cx];
        }
}
```

as 2-dimensional array can be a matrix, so we can make matrix multiplication function by using loop.
