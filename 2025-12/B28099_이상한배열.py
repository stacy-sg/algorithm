import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    first = {}
    last = {}
    for i, x in enumerate(A):
        if x not in first:
            first[x] = i
        last[x] = i

    LOG = (N).bit_length()
    st = [A[:]]
    for k in range(1, LOG):
        prev = st[k - 1]
        curr = []
        for i in range(N - (1 << k) + 1):
            curr.append(max(prev[i], prev[i + (1 << (k - 1))]))
        st.append(curr)

    def range_max(l, r):
        if l > r:
            return -1
        length = r - l + 1
        k = length.bit_length() - 1
        return max(st[k][l], st[k][r - (1 << k) + 1])

    ok = True
    for x in first:
        l, r = first[x], last[x]
        if l + 1 <= r - 1:
            if range_max(l + 1, r - 1) > x:
                ok = False
                break

    print("Yes" if ok else "No")