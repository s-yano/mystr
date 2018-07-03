#include <string.h>

void to_upper(char *s)
{
    int i;
    for (i = 0; i < (int)strlen(s); i++)
        if ('a' <= s[i] && s[i] <= 'z')
            s[i] -= 32;
}
