# with open('../../Downloads/dataset_3363_4 (3).txt', 'r') as text:
#     s = text.read().lower().split("\n",)
# del s[len(s) - 1]
# out_ = open('output.txt', 'a')
# first, second, third = 0, 0, 0
# for i in s:
#     i = i.split(';')
#     first += int(i[1])
#     second += int(i[2])
#     third += int(i[3])
#     print((int(i[1]) + int(i[2]) + int(i[3])) / 3, file=out_)
#     print((int(i[1]) + int(i[2]) + int(i[3])) / 3)
# print(first / len(s), second / len(s), third / len(s), file=out_)
# print(first / len(s), second / len(s), third / len(s))
# import math
# x = float(input())
# print(2 * math.pi * x)

res = input()
if len(res) == 5:
    for i in range(1, len(res) + 1):
        if res[-i] == "0": continue
        else:
            print(int(res[-i]), end="")
else:
    print(res[0], end="")
    for i in range(1, len(res)):
        if res[-i] == "0": continue
        else:
            print(res[-i], end="")
