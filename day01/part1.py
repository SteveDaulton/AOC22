"""Day 1, part 1"""


with open('./input', encoding="utf-8") as fp:
    maxcal = 0
    supplies = fp.read().split('\n\n')
    for elfcals in supplies:
        elfcal = sum(map(int, elfcals.split()))
        if elfcal > maxcal:
            maxcal = elfcal
    print(f'Best Elf is carrying {maxcal} calories')


with open('./test') as fp:
    # As a one liner;
    print(max([sum(map(int, elfcals.split()))
               for elfcals in fp.read().split('\n\n')]))
