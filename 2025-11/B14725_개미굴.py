import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.children = {}

def insert(root, foods):
    node = root
    for f in foods:
        if f not in node.children:
            node.children[f] = Node()
        node = node.children[f]

def dfs(node, depth):
    for key in sorted(node.children.keys()):
        print("--" * depth + key)
        dfs(node.children[key], depth + 1)

N = int(input().strip())
root = Node()

for _ in range(N):
    data = input().strip().split()
    K = int(data[0])
    foods = data[1:]
    insert(root, foods)

dfs(root, 0)