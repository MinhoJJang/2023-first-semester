#include <stdio.h>
int string_length(char in[100]);
int find_keyword(char in[100], char key[50]);

#define TRUE 0
#define FALSE 1

void main()
{
    char in_string[100];
    char in_key[50];
    int len; // length of in_string
    int cnt; // count of in_key
    // read input
    printf("Type a sentence: ");
    gets(in_string);
    printf("Enter the keyword: ");
    gets(in_key);
    // function call
    len = string_length(in_string);
    cnt = find_keyword(in_string, in_key);
    // result
    printf("Length of the input string: %d\n", len);
    printf("Keyword \"%s\" found %d times.\n", in_key, cnt);
}
int string_length(char in[100])
{
    int len = 0;
    while (in[len] != '\0')
    {
        len++;
    }
    return len;
}
int find_keyword(char in[100], char key[50])
{

    int cnt = 0;
    int in_length = string_length(in);
    int key_length = string_length(key);
    int flag = FALSE;
    for (int i = 0; i < in_length; i++)
    {
        if (in[i] == key[0])
        {
            for (int j = 1; j < key_length; j++)
            {
                if (in[i + j] == key[j])
                {
                    flag = TRUE;
                }
                else
                {
                    flag = FALSE;
                    break;
                }
            }

            if (flag == TRUE)
            {
                cnt++;
                flag = FALSE;
            }
        }
    }
    return cnt;
}