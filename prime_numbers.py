def sieve_of_eratosthenes(start, end):
    if end < 2:
        return []
    
    sieve = [True] * (end + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(end ** 0.5) + 1):
        if sieve[i]:
            sieve[i*i : end+1 : i] = [False] * len(sieve[i*i : end+1 : i])
    
    primes = [i for i in range(max(2, start), end + 1) if sieve[i]]
    return primes

def is_prime_simple(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    if end - start > 1000000:
        return sieve_of_eratosthenes(start, end)
    else:
        primes = []
        for num in range(max(2, start), end + 1):
            if is_prime_simple(num):
                primes.append(num)
        return primes

def main():
    print("欢迎使用素数计算器！")
    while True:
        try:
            user_input = input("\n请输入范围（格式：起始值-结束值，如 1-100）：")
            parts = user_input.split('-')
            if len(parts) != 2:
                print("格式错误！请使用 '起始值-结束值' 格式。")
                continue
            start = int(parts[0].strip())
            end = int(parts[1].strip())
            
            if start > end:
                print("起始值不能大于结束值！")
                continue
            
            if start < 1:
                print("请输入正整数！")
                continue
            
            break
        except ValueError:
            print("输入无效！请输入有效的整数。")
    
    primes = find_primes_in_range(start, end)
    
    if primes:
        primes_str = ','.join(map(str, primes))
        print(f"\n{start}-{end} 的素数有：{primes_str}")
        print(f"\n共找到 {len(primes)} 个素数。")
    else:
        print(f"\n{start}-{end} 范围内没有素数。")

if __name__ == "__main__":
    main()
