from funs import bisect_right, string_generator, print_result, find_gcd


class Balancer:
    def __init__(self, weights_list=[1]):
        self.weights_list = weights_list

    def reset_weights(self, weights_list=[1]):
        self.__init__(weights_list)

    def get_instance_index(self, query):
        pass


class SimpleHashing(Balancer):
    def __init__(self, weights_list=[1]):
        self.weights_list = [x // find_gcd(weights_list) for x in weights_list]

    def get_instance_index(self, query):
        sub_instance_index = hash(query) % sum(self.weights_list)
        for instance_index in range(len(self.weights_list)):
            sub_instance_index -= self.weights_list[instance_index]
            if sub_instance_index < 0:
                return instance_index


class RendezVousHashing(Balancer):
    def get_instance_index(self, query):
        sub_instances = []
        for inst_index in range(len(self.weights_list)):
            for sub_inst_index in range(self.weights_list[inst_index]):
                sub_instances.append((hash((inst_index, sub_inst_index, query)), inst_index))
        return max(sub_instances)[1]


class ConsistentHashing(Balancer):
    def __init__(self, weights_list=[1]):
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


def test(queries_number, weights_lists):
    queries = [string_generator(5) for n in range(queries_number)]

    max_len = len(max(weights_lists, key=len))

    all_instances = [[Instance() for y in range(max_len)] for x in range(3)]

    relative_weights = [[y / sum(x) * queries_number for y in x] for x in weights_lists]

    ideal_queries_count = [int(sum([(i[n] if n < len(i) else 0) for i in relative_weights])) for n in range(max_len)]

    simple_balancer = SimpleHashing()
    consistent_balancer = ConsistentHashing()
    rendezvous_balancer = RendezVousHashing()

    for weights in weights_lists:
        simple_balancer.reset_weights(weights)
        consistent_balancer.reset_weights(weights)
        rendezvous_balancer.reset_weights(weights)

        for query in queries:
            choice1 = simple_balancer.get_instance_index(query)
            choice2 = consistent_balancer.get_instance_index(query)
            choice3 = rendezvous_balancer.get_instance_index(query)

            all_instances[0][choice1].process_query(query)
            all_instances[1][choice2].process_query(query)
            all_instances[2][choice3].process_query(query)

    print_result(all_instances, ideal_queries_count)


test(10000, [[100, 200, 300, 500], [100, 200, 300]])

# this test get queryset size and list of lists of weights
# 1) distributes queries across instances
# 2) reset weights
# again Till the end
# shows instances cache hit, distribution of queries across instances
