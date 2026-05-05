import sys
input = sys.stdin.readline

def sieve(limit):
    """에라토스테네스 체로 limit 이하 소수 목록 반환"""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(2, limit + 1) if is_prime[i]]

# n ≤ 10^4이므로 최대 9999개의 소수가 필요 → 200,000 이하 소수로 충분
primes = sieve(200_000)

t = int(input())
for _ in range(t):
    n = int(input())

    # n-1개의 소수 사용: p[0], p[1], ..., p[n-2]
    p = primes[:n - 1]

    seq = []
    seq.append(p[0])                      # a1 = p1

    for i in range(1, n - 1):             # a_i = p_{i-1} * p_i  (2 ≤ i ≤ n-1)
        seq.append(p[i - 1] * p[i])

    seq.append(p[n - 2])                  # a_n = p_{n-1}

    print(*seq)