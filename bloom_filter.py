import array
import mmh3
import math


def _get_optimal_size(capacity, error_rate):
    bit_array_size = math.ceil(-capacity * math.log(error_rate) / ((math.log(2)) ** 2))
    number_of_hash_functions = math.ceil(-math.log(error_rate, 2))
    return int(bit_array_size), int(number_of_hash_functions)


class BloomFilter:
    def __init__(self, capacity, error_rate):
        self._bit_array_size, self._number_of_hash_functions = _get_optimal_size(capacity, error_rate)

        self._bit_array = array.array('B', [0]) * self._bit_array_size

    def _calculate_hashes(self, val):
        hashes = []
        for seed in range(self._number_of_hash_functions):
            hash_val = mmh3.hash(val, seed=seed, signed=False) % self._bit_array_size
            hashes.append(hash_val)
        return hashes

    def add(self, elem):
        hashes = self._calculate_hashes(elem)
        for hash_val in hashes:
            self._bit_array[hash_val] = 1

    def exist(self, elem):
        hashes = self._calculate_hashes(elem)
        for hash_val in hashes:
            if self._bit_array[hash_val] == 0:
                return False
        return True
