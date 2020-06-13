# Baekjoon Online Judge Study - 2884
# Author : ㄱㄱㅊ
# Title : alarm clock
# Date : 20-06-13

from sys import stdin

H, M = map(int, stdin.readline().split())
alarm_time = (H * 60 + M) - 45
alarm_H, alarm_M = alarm_time // 60 % 24, alarm_time % 60
print(alarm_H, alarm_M)
