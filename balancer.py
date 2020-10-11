from funs import bisect_right, string_generator, print_result, find_gcd


class Balancer:
    def __init__(self, weights_list=[1]):
        self.reset_weights(weights_list)

    def reset_weights(self, weights_list=[1]):
        self.weights_list = weights_list

    def get_instance_index(self, query):
        pass


class SimpleHashing(Balancer):
    def reset_weights(self, weights_list=[1]):
        self.weights_list = [x // find_gcd(weights_list) for x in weights_list]
        self.inst_indexes = []
        for inst_ind in range(len(self.weights_list)):
            for n in range(self.weights_list[inst_ind]):
                self.inst_indexes.append(inst_ind)

    def get_instance_index(self, query):
        sub_instance_index = hash(query) % sum(self.weights_list)
        return self.inst_indexes[sub_instance_index]


class RendezVousHashing(Balancer):
    def get_instance_index(self, query):
        max_hash = None
        for inst_index in range(len(self.weights_list)):
            for sub_inst_index in range(self.weights_list[inst_index]):
                hash_with_index = (hash((inst_index, sub_inst_index, query)), inst_index)
                if max_hash is None or hash_with_index[0] > max_hash[0]:
                    max_hash = hash_with_index
        return max_hash[1]


class ConsistentHashing(Balancer):
    def reset_weights(self, weights_list=[1]):
        self.weights_list = weights_list
        self.sub_instances = []
        for inst_index in range(len(self.weights_list)):
            for sub_inst_index in range(self.weights_list[inst_index]):
                self.sub_instances.append((hash((inst_index, sub_inst_index)), inst_index))
        self.sorted_sub_instances = sorted(self.sub_instances)

    def get_instance_index(self, query):
        near_right_index = bisect_right(self.sorted_sub_instances, (hash(query), 0))
        return self.sub_instances[near_right_index % len(self.sub_instances)][1]


class Instance:
    def __init__(self):
        self.cache = set()
        self.queries_count = 0
        self.cache_hit_number = 0

    def process_query(self, query):
        self.queries_count += 1
        if query in self.cache:
            self.cache_hit_number += 1
        else:
            self.cache.add(query)

    def cache_hit(self):
        return self.cache_hit_number / self.queries_count if self.queries_count != 0 else 0

    def clear(self):
        self.cache = set()
        self.queries_count = 0
        self.cache_hit_number = 0


def test_balancer(queries, weights_lists, instances, balancer):
    for weights in weights_lists:
        balancer.reset_weights(weights)
        for query in queries:
            choice = balancer.get_instance_index(query)
            instances[choice].process_query(query)


def test(queries, weights_lists):
    max_len = len(max(weights_lists, key=len))

    all_instances = [[Instance() for y in range(max_len)] for x in range(3)]

    relative_weights = [[y / sum(x) * len(queries) for y in x] for x in weights_lists]

    ideal_queries_count = [int(sum([(i[n] if n < len(i) else 0) for i in relative_weights])) for n in range(max_len)]

    simple_balancer = SimpleHashing()
    consistent_balancer = ConsistentHashing()
    rendezvous_balancer = RendezVousHashing()

    test_balancer(queries, weights_lists, all_instances[0], simple_balancer)
    test_balancer(queries, weights_lists, all_instances[1], consistent_balancer)
    test_balancer(queries, weights_lists, all_instances[2], rendezvous_balancer)

    print_result(all_instances, ideal_queries_count)


queries = [string_generator(5) for n in range(10000)]

test(queries, [[100, 200, 300, 400], [100, 200, 300]])
# this test get queryset size and list of lists of weights
# 1) distributes queries across instances
# 2) reset weights
# again Till the end
# shows instances cache hit, distribution of queries across instances
