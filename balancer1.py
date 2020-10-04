import string
import random
from collections import Counter
from rich.console import Console
from rich.table import Column, Table


def print_result1():
    console = Console()

    table = Table(show_header=True)
    table.add_column('test1', justify="left")
    table.add_column('simple', justify="left")
    table.add_column('consistent', justify="left")
    table.add_column('rendezvous', justify="left")
    table.add_row('1st inst c/h', f'{A1.cash_hit():03f}', f'{A2.cash_hit():03f}', f'{A3.cash_hit():03f}')
    table.add_row('2nd inst c/h', f'{B1.cash_hit():03f}', f'{B2.cash_hit():03f}', f'{B3.cash_hit():03f}')
    table.add_row('3rd inst c/h', f'{C1.cash_hit():03f}', f'{C2.cash_hit():03f}', f'{C3.cash_hit():03f}')
    table.add_row('c/h average',
                  f'{(A1.cash_hit() + B1.cash_hit() + C1.cash_hit())/3:03f}',
                  f'{(A2.cash_hit() + B2.cash_hit() + C2.cash_hit())/3:03f}',
                  f'{(A3.cash_hit() + B3.cash_hit() + C3.cash_hit())/3:03f}')
    table.add_row('1st inst query number', f'{A1.query_number()}', f'{A2.query_number()}', f'{A3.query_number()}')
    table.add_row('    ideal', f'{2000 * 10000 // (2000 + 100 + 3000)}', f'{2000 * 10000 // (2000 + 100 + 3000)}',
                  f'{2000 * 10000 // (2000 + 100 + 3000)}')
    table.add_row('2nd inst query number', f'{B1.query_number()}', f'{B2.query_number()}', f'{B3.query_number()}')
    table.add_row('    ideal',
                  f'{100 * 10000 // (2000 + 100 + 3000)}',
                  f'{100 * 10000 // (2000 + 100 + 3000)}',
                  f'{100 * 10000 // (2000 + 100 + 3000)}')
    table.add_row('    ideal', f'{C1.query_number()}', f'{C2.query_number()}', f'{C3.query_number()}')
    table.add_row('3rd inst query number',
                  f'{3000 * 10000 // (2000 + 100 + 3000)}',
                  f'{3000 * 10000 // (2000 + 100 + 3000)}',
                  f'{3000 * 10000 // (2000 + 100 + 3000)}')

    console.print(table)


def print_result2():
    console = Console()

    table = Table(show_header=True)
    table.add_column('test2', justify="left")
    table.add_column('simple', justify="left")
    table.add_column('consistent', justify="left")
    table.add_column('rendezvous', justify="left")
    table.add_row('1st inst c/h', f'{A1.cash_hit():03f}', f'{A2.cash_hit():03f}', f'{A3.cash_hit():03f}')
    table.add_row('2nd inst c/h', f'{B1.cash_hit():03f}', f'{B2.cash_hit():03f}', f'{B3.cash_hit():03f}')
    table.add_row('3rd inst c/h', f'{C1.cash_hit():03f}', f'{C2.cash_hit():03f}', f'{C3.cash_hit():03f}')
    table.add_row('c/h average',
                  f'{(A1.cash_hit() + B1.cash_hit() + C1.cash_hit())/3:03f}',
                  f'{(A2.cash_hit() + B2.cash_hit() + C2.cash_hit())/3:03f}',
                  f'{(A3.cash_hit() + B3.cash_hit() + C3.cash_hit())/3:03f}')
    table.add_row('1st inst query number', f'{A1.query_number()}', f'{A2.query_number()}', f'{A3.query_number()}')
    table.add_row('2nd inst query number', f'{B1.query_number()}', f'{B2.query_number()}', f'{B3.query_number()}')
    table.add_row('3rd inst query number', f'{C1.query_number()}', f'{C2.query_number()}', f'{C3.query_number()}')

    console.print(table)


def print_result3():
    console = Console()

    table = Table(show_header=True)
    table.add_column('test2', justify="left")
    table.add_column('simple', justify="left")
    table.add_column('consistent', justify="left")
    table.add_column('rendezvous', justify="left")
    table.add_row('1st inst c/h', f'{A1.cash_hit():03f}', f'{A2.cash_hit():03f}', f'{A3.cash_hit():03f}')
    table.add_row('2nd inst c/h', f'{B1.cash_hit():03f}', f'{B2.cash_hit():03f}', f'{B3.cash_hit():03f}')
    table.add_row('3rd inst c/h', f'{C1.cash_hit():03f}', f'{C2.cash_hit():03f}', f'{C3.cash_hit():03f}')
    table.add_row('c/h average',
                  f'{(A1.cash_hit() + B1.cash_hit() + C1.cash_hit())/3:03f}',
                  f'{(A2.cash_hit() + B2.cash_hit() + C2.cash_hit())/3:03f}',
                  f'{(A3.cash_hit() + B3.cash_hit() + C3.cash_hit())/3:03f}')
    table.add_row('1st inst query number', f'{A1.query_number()}', f'{A2.query_number()}', f'{A3.query_number()}')
    table.add_row('2nd inst query number', f'{B1.query_number()}', f'{B2.query_number()}', f'{B3.query_number()}')
    table.add_row('3rd inst query number', f'{C1.query_number()}', f'{C2.query_number()}', f'{C3.query_number()}')

    console.print(table)


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


class SimpleHashing:
    def __init__(self, weights_list=[1]):
        self.weights_list = weights_list

    def set_weights(self, weights_list=[1]):
        self.weights_list = weights_list

    def get_instance_index(self, query):
        sub_instance_index = hash(query) % sum(self.weights_list)
        for instance_index in range(len(self.weights_list)):
            sub_instance_index -= self.weights_list[instance_index]
            if sub_instance_index < 0:
                return instance_index


class RendezVousHashing:
    def __init__(self, weights_list=[1]):
        self.weights_list = weights_list

    def set_weights(self, weights_list=[1]):
        self.weights_list = weights_list

    def get_instance_index(self, query):
        sub_instances = []
        for inst_index in range(len(self.weights_list)):
            for sub_inst_index in range(self.weights_list[inst_index]):
                sub_instances.append(f'{inst_index}_{sub_inst_index}_{query}')
        instances_hashes = [hash(sub_instance) for sub_instance in sub_instances]
        sub_instance_index = instances_hashes.index(max(instances_hashes))
        for instance_index in range(len(self.weights_list)):
            sub_instance_index -= self.weights_list[instance_index]
            if sub_instance_index < 0:
                return instance_index


class ConsistentHashing:
    def __init__(self, weights_list=[1]):
        self.weights_list = weights_list

    def set_weights(self, weights_list=[1]):
        self.weights_list = weights_list

    def get_instance_index(self, query):
        sub_instances = []
        for inst_index in range(len(self.weights_list)):
            for sub_inst_index in range(self.weights_list[inst_index]):
                    sub_instances.append(f'{inst_index}_{sub_inst_index}')
        instances_hashes = [hash(sub_instance) for sub_instance in sub_instances]
        sub_instance_index = instances_hashes.index(instances_hashes[bisect_right(sorted(instances_hashes), hash(query)) % len(instances_hashes)])
        for instance_index in range(len(self.weights_list)):
            sub_instance_index -= self.weights_list[instance_index]
            if sub_instance_index < 0:
                return instance_index


class Instance:
    def __init__(self):
        self.query_list = []

    def get_query(self, query):
        self.query_list.append(query)

    def cash_hit(self):
        repetitions_number = 0
        for query_freq in (list(Counter(self.query_list).values())):
            if query_freq > 1:
                repetitions_number += 1
        if len(self.query_list) > 0:
            return repetitions_number/len(Counter(self.query_list).values())
        else:
            return 'empty'

    def query_number(self):
        return len(self.query_list)

    def clear(self):
        self.query_list = []


query_list = []
for n in range(10000):
    query_list.append(string_generator(10))

simple_balancer = SimpleHashing([2000, 100, 3000])
consistent_balancer = ConsistentHashing([2000, 100, 3000])
rendezvous_balancer = RendezVousHashing([2000, 100, 3000])

A1, B1, C1 = Instance(), Instance(), Instance()
A2, B2, C2 = Instance(), Instance(), Instance()
A3, B3, C3 = Instance(), Instance(), Instance()
instances_list1 = [A1, B1, C1]
instances_list2 = [A2, B2, C2]
instances_list3 = [A3, B3, C3]

for query1 in query_list:
    num1 = simple_balancer.get_instance_index(query1)
    num2 = consistent_balancer.get_instance_index(query1)
    num3 = rendezvous_balancer.get_instance_index(query1)
    instances_list1[num1].get_query(query1)
    instances_list2[num2].get_query(query1)
    instances_list3[num3].get_query(query1)

print_result1()

A1.clear()
B1.clear()
C1.clear()
A2.clear()
B2.clear()
C2.clear()
A3.clear()
B3.clear()
C3.clear()

for query1 in query_list:
    num1 = simple_balancer.get_instance_index(query1)
    num2 = consistent_balancer.get_instance_index(query1)
    num3 = rendezvous_balancer.get_instance_index(query1)
    instances_list1[num1].get_query(query1)
    instances_list2[num2].get_query(query1)
    instances_list3[num3].get_query(query1)

for i, query1 in enumerate(query_list):
    if not i % 1000:
        simple_balancer.set_weights([2000, 100 + i//10, 3000])
        consistent_balancer.set_weights([2000, 100 + i//10, 3000])
        rendezvous_balancer.set_weights([2000, 100 + i//10, 3000])
    num1 = simple_balancer.get_instance_index(query1)
    num2 = consistent_balancer.get_instance_index(query1)
    num3 = rendezvous_balancer.get_instance_index(query1)
    instances_list1[num1].get_query(query1)
    instances_list2[num2].get_query(query1)
    instances_list3[num3].get_query(query1)

print_result2()

A1.clear()
B1.clear()
C1.clear()
A2.clear()
B2.clear()
C2.clear()
A3.clear()
B3.clear()
C3.clear()

simple_balancer.set_weights([2000, 100, 3000])
consistent_balancer.set_weights([2000, 100, 3000])
rendezvous_balancer.set_weights([2000, 100, 3000])

for query1 in query_list:
    num1 = simple_balancer.get_instance_index(query1)
    num2 = consistent_balancer.get_instance_index(query1)
    num3 = rendezvous_balancer.get_instance_index(query1)
    instances_list1[num1].get_query(query1)
    instances_list2[num2].get_query(query1)
    instances_list3[num3].get_query(query1)

simple_balancer.set_weights([2000, 100])
consistent_balancer.set_weights([2000, 100])
rendezvous_balancer.set_weights([2000, 100])

for query1 in query_list:
    num1 = simple_balancer.get_instance_index(query1)
    num2 = consistent_balancer.get_instance_index(query1)
    num3 = rendezvous_balancer.get_instance_index(query1)
    instances_list1[num1].get_query(query1)
    instances_list2[num2].get_query(query1)
    instances_list3[num3].get_query(query1)

print_result3()