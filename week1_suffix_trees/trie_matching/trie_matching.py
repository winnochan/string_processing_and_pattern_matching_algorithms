# python3
import sys


def build_trie(patterns):
    root = 0
    trie = {}

    nid = 1
    for p in patterns:
        node = root
        for c in p:
            if node not in trie:
                trie[node] = {}
            if c in trie[node]:
                node = trie[node][c]
            else:
                trie[node][c] = nid
                node = nid
                nid += 1

    return trie


def match_trie(trie, text, begin):
    node = 0
    for i in range(begin, len(text) + 1):
        if node not in trie:
            return True
        if i == len(text):
            break
        if text[i] in trie[node]:
            node = trie[node][text[i]]
            continue
        return False
    return False


def solve(text, n, patterns):
    result = []

    trie = build_trie(patterns)
    # print(trie)

    for i in range(len(text)):
        if match_trie(trie, text, i):
            result.append(i)

    return result


text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]

ans = solve(text, n, patterns)

sys.stdout.write(' '.join(map(str, ans)) + '\n')
