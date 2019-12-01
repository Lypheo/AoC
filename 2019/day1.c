#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>

#define MAX(a, b) (a > b ? a : b)

int64_t get_fuel(int64_t mass) {
    int64_t fuel = MAX(mass / 3 - 2, 0);
    return fuel < 1 ? 0 : fuel + get_fuel(fuel);
}

int64_t main(int argc, char const *argv[])
{
    FILE *inp = fopen("C:\\testing\\bigboyinput", "r");
    int64_t total1 = 0, total2= 0, add = 0, mass = 0;
    while (fscanf(inp, "%d", &add) > 0) {
        mass = add/3 - 2;
        total1 += mass;
        total2 += get_fuel(mass);
    };
    printf("Part1: %" PRId64 "\n""Part2: %" PRId64 "\n", total1, total2+total1);
    return 0;
}