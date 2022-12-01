"""Day 1, part 2"""


with open('./input', encoding="utf-8") as fp:
    supplies = fp.read().split('\n\n')
    supplies = [sum(map(int, elfcals.split())) for elfcals in supplies]
    supplies.sort()
    print(sum(supplies[-3::]))


with open('./input', encoding="utf-8") as fp:
    # As one liner:
    print(sum(sorted([sum(map(int, elfcals.split()))
                      for elfcals in fp.read().split('\n\n')])[-3::]))
