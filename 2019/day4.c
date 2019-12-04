#include <stdio.h>
#include <math.h>

long int inarray(long int arr[], long int val) {
    for (int i = 0; i < 10; ++i) {
        if (arr[i] == val)
            return 1;
    }
    return 0;
}

long int nonzero(long int arr[]) {
    for (int i = 0; i < 10; ++i) {
        if (arr[i] != 0)
            return 1;
    }
    return 0;
}

unsigned long int isvalid(long int num) {
    long int duplicates[10] = {0,0,0,0,0,0,0,0,0,0};
    long int increasing = 1;
    long int length = 1 + (long int) log10l((long double) num);
    long int div = (long int) pow(10, length-1);
    long int last_digit = num / div;
    long int rest = num % div;
    long int digit;
    for (long int i = 1; i < length; ++i) {
        div /= 10;
        digit = rest / div;
        if (digit == last_digit) {
            duplicates[digit] += 1;
        }
        if (digit < last_digit) {
            increasing = 0;
        }
        last_digit = digit;
        rest = rest % div;
    }
    return increasing ? nonzero(duplicates) + inarray(duplicates, 1) * 2 : 0;
}

int main(int argc, char const *argv[])
{
    long int start = 100000000, end = 1000000000;
    unsigned long int counta = 0, countb = 0, res;
    for (long int i = start; i <= end; ++i) {
        res = isvalid(i);
        counta += (res | 2u) == 3u;
        countb += (res | 1u) == 3u;
    }
    printf("%lu %lu", counta, countb);
    return 0;
}