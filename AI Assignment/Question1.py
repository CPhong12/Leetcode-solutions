def soep(n, k, mod=1000000007):
    result = 0
    for i in range(1, n + 1):
        result = (result + pow(i, k, mod)) % mod
    return result

def main():
    n, k = map(int, input().split())
    print(soep(n, k))

if __name__ == "__main__":
    main()