M = int(input())
M_seq = list(map(int,input().split()))
N = int(input())
N_seq = list(map(int,input().split()))

if len(M_seq) == M and len(N_seq) == N:
    M_seq = set(M_seq)
    N_seq = set(N_seq)
    diff1 = M_seq.difference(N_seq)
    diff2 = N_seq.difference(M_seq)
    result = [diff1, diff2]

    flattened_result = [item for sublist in result for item in sublist]
    flattened_result.sort()
    for element in flattened_result:
        print(element)

else:
    print("Problem with set lengths.")