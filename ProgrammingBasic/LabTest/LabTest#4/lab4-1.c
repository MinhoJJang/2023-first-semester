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
    int in_idx = 0;
    int word_idx = 0;

    if (in[in_idx] == word[word_idx])
    {
    }
}

void str_rev(char *in, int start_pos, int end_pos)
{
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

    print(len);

    // pos = str_find(string_in, word);
    // str_rev(string_in, pos, pos+len-1);

    // printf("(Results)\n");
    // printf("Word length: %d\n", len);
    // printf("The found place: %d\n", pos);
    // printf("Output: %d\n", string_in);

    return 0;
}
}
#include <stdio.h>

#include <stdio.h>

return 0;
}
#include <stdio.h>

#include <stdio.h>

