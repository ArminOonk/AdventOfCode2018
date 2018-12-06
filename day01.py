with open('input_day01.txt', 'r') as f:
    data = f.readlines()

res = 0
for d in data:
    res += int(d)

print('Day 01 part1 results: ' + str(res))

res = 0
found_freq = dict()
loop_cnt = 0
searching = True

while searching:
    print('Loop cnt: ' + str(loop_cnt))
    loop_cnt += 1
    for d in data:
        res += int(d)

        if res in found_freq:
            searching = False
            break

        found_freq[res] = True

print('Day 01 part2 results: ' + str(res))
