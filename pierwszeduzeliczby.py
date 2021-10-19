import collections
from time import perf_counter
import math
from typing import List, Tuple

def main():
    
    found_primes = 0

    def solve(my_nums: List[Tuple[int, int]], actual_sum: int) -> None:

        if not is_prime_miller(actual_sum):
            return

        sum_counts = collections.Counter(str(actual_sum))
        for orig_dig, amount_to_use in my_nums:
            if amount_to_use != sum_counts[str(orig_dig)]:
                return

        nonlocal found_primes
        found_primes += 1
        print(f"Found ans number {found_primes}: {actual_sum}")


    def dfs(curr_digit: int, remaining: int, curr_sum: int, orig_num_digs: int, biggest: int,
            used_dig_list: List[Tuple[int, int]]) -> None:

        my_pow = POWS[curr_digit]

        if curr_sum >= biggest or 10 * (remaining * my_pow + curr_sum) < biggest - 10:
            return
        if remaining == 0:
            if len(str(curr_sum)) == orig_num_digs:
                solve(used_dig_list, curr_sum)
            return
        assert remaining > 0
        if curr_digit == 0:
            # curr_sum += remaining*pow(9, orig_num_digs)
            if len(str(curr_sum)) == orig_num_digs:
                solve(used_dig_list + [(0, remaining)], curr_sum)
            return

        new_sum = curr_sum
        for amount_to_use in range(remaining + 1):
            dfs(curr_digit=curr_digit - 1, remaining=remaining - amount_to_use, curr_sum=new_sum,
                orig_num_digs=orig_num_digs, biggest=biggest,
                used_dig_list=used_dig_list + [(curr_digit, amount_to_use)])
            new_sum += my_pow
            if new_sum >= biggest:
                return

    for digits_to_use in range(1, 34):
        print(f"Starting {digits_to_use}, {perf_counter() - start_time :.4f} sec. since start")
        POWS = [pow(x, digits_to_use) for x in range(10)]
        dfs(curr_digit=9, remaining=digits_to_use, curr_sum=0, orig_num_digs=digits_to_use,
            biggest=pow(10, digits_to_use), used_dig_list=[])

def is_prime_miller(n: int) -> bool:
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    if n < 2:
        return False
    for p in small_primes:
        if n < p * p:
            return True
        if n % p == 0:
            return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for a in small_primes:

        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


start_time = perf_counter()
main()