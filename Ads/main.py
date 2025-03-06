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

t = int(input())
for i in range(t):
    test_case()