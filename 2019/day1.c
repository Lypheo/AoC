#include <stdio.h>
#include <stdlib.h>
#define MAX(a, b) (a > b ? a : b)

int get_fuel(int mass) {
    int fuel = MAX(mass / 3 - 2, 0);
    return fuel < 1 ? 0 : fuel + get_fuel(fuel);
}

int main(int argc, char const *argv[])
{
    FILE *inp = fopen("C:\\testing\\input", "r");
    int total= 0, add = 0;
    while (fscanf(inp, "%d", &add) > 0) {
        total += add/3 - 2;
    };
    printf("Part1: %d\n", total);
    rewind(inp);

    total = 0; add = 0;
    int mass = 0;
    while (fscanf(inp, "%d", &add) > 0) {
        mass = add/3 - 2;
        total += mass + get_fuel(mass);
    };
    printf("Part2: %d\n", total);
    return 0;
}