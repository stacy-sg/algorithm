import sys
input = sys.stdin.readline

s = input().strip()
n = len(s)

class State:
    def __init__(self):
        self.next = {}
        self.link = -1
        self.len = 0
        self.cnt = 0


sam = [State()]
last = 0

def sa_extend(c):
    global last
    cur = len(sam)
    sam.append(State())
    sam[cur].len = sam[last].len + 1
    sam[cur].cnt = 1

    p = last
    while p != -1 and c not in sam[p].next:
        sam[p].next[c] = cur
        p = sam[p].link

    if p == -1:
        sam[cur].link = 0
    else:
        q = sam[p].next[c]
        if sam[p].len + 1 == sam[q].len:
            sam[cur].link = q
        else:
            clone = len(sam)
            sam.append(State())
            sam[clone].len = sam[p].len + 1
            sam[clone].next = sam[q].next.copy()
            sam[clone].link = sam[q].link
            sam[clone].cnt = 0

            while p != -1 and sam[p].next.get(c, -1) == q:
                sam[p].next[c] = clone
                p = sam[p].link

            sam[q].link = clone
            sam[cur].link = clone
    last = cur


for ch in s:
    sa_extend(ch)

order = sorted(range(len(sam)), key=lambda i: sam[i].len, reverse=True)
for v in order:
    if sam[v].link != -1:
        sam[sam[v].link].cnt += sam[v].cnt

answer = 0
for st in sam:
    if st.cnt >= 2:
        answer = max(answer, st.len)

print(answer)