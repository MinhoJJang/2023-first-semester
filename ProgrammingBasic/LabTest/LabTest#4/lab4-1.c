#include <stdio.h>

int str_len(char *in)
{
    // 들어온 글자의 길이
    int cnt = 0;
    while (in[cnt] != '\0')
    {
        cnt++;
    }
    return cnt;
}

int str_find(char *in, char *word)
{
    int word_idx = 0;
    int in_len = str_len(in);
    int word_len = str_len(word);

    for (int in_idx = 0; in_idx < in_len; in_idx++)
    {
        if (in[in_idx] == word[word_idx])
        {
            if (in_len - in_idx < word_len)
            {
                return -1;
            }
            else
            {
                int flag = 0;
                for (int i = 0; i < word_len; i++)
                {
                    if (in[in_idx + i] != word[word_idx + i])
                    {
                        flag = -1;
                    }
                }

                if (flag == 0)
                {
                    return in_idx;
                }
            }
        }
    }
}

void str_rev(char *in, int start_pos, int end_pos)
{
    char temp[50];

    for (int i = start_pos; i <= end_pos; i++)
    {
        temp[i] = in[i];
    }

    for (int i = start_pos; i <= end_pos; i++)
    {
        in[i] = temp[end_pos + start_pos - i];
    }
}

int main()
{
    char string_in[100], word[50];
    int len, pos;

    printf("String: ");
    gets(string_in);
    printf("Word: ");
    gets(word);

    len = str_len(word);

    pos = str_find(string_in, word);
    str_rev(string_in, pos, pos + len - 1);

    printf("(Results)\n");
    printf("Word length: %d\n", len);
    printf("The found place: %d\n", pos);
    printf("Output: %s\n", string_in);

    return 0;
}
