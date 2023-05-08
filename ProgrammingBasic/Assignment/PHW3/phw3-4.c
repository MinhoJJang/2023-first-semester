#include <stdio.h>

int main()
{
    char words[6][101];

    for (int i = 0; i < 6; i++)
    {
        printf("Enter the %d-th conversation: ", i);
        fgets(words[i], sizeof(words[i]), stdin);
    }

    printf("The strings ending with \"?\" are:\n");
    for (int i = 0; i < 6; i++)
    {
        int j;
        for (j = 0; words[i][j] != '\0'; j++)
        {
            // do nothing, just find the end of the string
        }
        // check if the last character before '\n' is '?'
        if (words[i][j - 2] == '?')
        {
            printf("%s", words[i]);
        }
    }

    return 0;
}
