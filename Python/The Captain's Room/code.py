from collections import Counter

group_size = int(input())
rooms_list = list(map(int, input().split()))

rooms_count = Counter(rooms_list)

for room, count in rooms_count.items():
    if count == 1:
        print(room)
        break