
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