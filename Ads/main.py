def test_case():
    tokens = input().split(" ")
    n = int(tokens[0])
    k = int(tokens[1])
    lengths = [int(x) for x in input().split(" ")]
    smaller = []
    bigger = []
    for x in lengths:
        if x >= k:
            bigger.append(x)
        else:
            smaller.append(x)
    smaller.sort()
    pairs = []
    start_idx = 0
    end_idx = len(smaller) - 1
    while start_idx <= end_idx:
        if start_idx == end_idx:
            pairs.append([smaller[start_idx]])
            break
        if smaller[start_idx] + smaller[end_idx] < k:
            pairs.append([smaller[start_idx], smaller[end_idx]])
            start_idx += 1
        else:
            pairs.append([smaller[end_idx]])
        end_idx -= 1
    print(pairs)
    result = len(bigger)
    if len(bigger) < len(pairs):
        result = (len(pairs) - len(bigger)) // 2 + 1
    result -= 1
    print(result)

t = int(input())
for i in range(t):
    test_case()