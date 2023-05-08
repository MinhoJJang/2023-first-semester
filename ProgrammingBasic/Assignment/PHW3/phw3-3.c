#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>

int main()
{
    char s[100];
    bool to_upper = true;

    printf("Enter a line of text: ");
    fgets(s, sizeof(s), stdin);

    for (int i = 0; s[i] != '\0'; i++)
    {
        if (isalpha(s[i]))
        {
            if (to_upper)
            {
                if (islower(s[i]))
                {
                    s[i] = s[i] - 'a' + 'A';
                }
            }
            else
            {
                if (isupper(s[i]))
                {
                    s[i] = s[i] - 'A' + 'a';
                }
            }
            to_upper = !to_upper;
        }
    }

    printf("Converted text is: %s", s);

    return 0;
}
