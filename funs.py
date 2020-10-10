import string
from math import gcd
from functools import reduce
import random
from rich.console import Console
from rich.table import Table


def bisect_right(list__, x, lo=0, hi=None):
    if hi is None:
        hi = len(list__)
    while lo < hi:
        mid = (lo+hi)//2
        if x < list__[mid]:
            hi = mid
        else:
            lo = mid+1
    return lo


def string_generator(size=10, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def find_gcd(lst):
    x = reduce(gcd, lst)
    return x


def print_result(instances, inst_queries_count):
    console = Console()

    table = Table(show_header=True)

    table.add_column(' ', justify="left")
    table.add_column('simple', justify="left")
    table.add_column('consistent', justify="left")
    table.add_column('rendezvous', justify="left")

    chs_sum1, chs_sum2, chs_sum3 = 0, 0, 0
    instances_number = len(instances[0])

    for n in range(instances_number):
        chs_sum1 += instances[0][n].cache_hit()
        chs_sum2 += instances[1][n].cache_hit()
        chs_sum3 += instances[2][n].cache_hit()
        table.add_row(f'{n + 1} inst c/h',
                      f'{instances[0][n].cache_hit():.3f}',
                      f'{instances[1][n].cache_hit():.3f}',
                      f'{instances[2][n].cache_hit():.3f}')
    table.add_row(f'c/h average',
                  f'{chs_sum1 / instances_number:.3f}',
                  f'{chs_sum2 / instances_number:.3f}',
                  f'{chs_sum3 / instances_number:.3f}')

    for n in range(instances_number):
        table.add_row(f'{n + 1} inst queries number',
                      f'{instances[0][n].queries_count}',
                      f'{instances[1][n].queries_count}',
                      f'{instances[2][n].queries_count}')
        table.add_row(f'  accuracy by weights',
                      f'{instances[0][n].queries_count/inst_queries_count[n] * 100:.0f}%',
                      f'{instances[1][n].queries_count/inst_queries_count[n] * 100:.0f}%',
                      f'{instances[2][n].queries_count/inst_queries_count[n] * 100:.0f}%')

    console.print(table)
