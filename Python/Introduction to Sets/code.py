def average(array):
    distinct_heights = set(array)
    total_distinct_heights = len(distinct_heights)
    distinct_heights = sum(distinct_heights)
    return round(distinct_heights/total_distinct_heights, 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)