#include <stdio.h>
#include <limits.h>

int main()
{
    int value = INT_MAX;
    printf("Original value: %d\n", value);
    value += 1; // This will cause an overflow
    printf("Value after overflow: %d\n", value);
    return 0;
}