import sys
N = int(sys.stdin.readline())
temp_n = N
# 666 1 * 1 + 1 * 0 -> 1
# 1666 2666 3666 4666 5666 -> 2
# 6660 6661 6662 6663 6664 6665 6666 6667 6668 6669
# 7666 8666 9666  1 * 10 + 1 * 9
# 10666 11666 1 * 100 + 2 * 90 -> 3
# 100666 1 * 1000 + 3 * 900

i = 0
while temp_n > 0:
    temp_n -= (1 * (10 ** i) + i * (10 ** i - 1))
    i += 1