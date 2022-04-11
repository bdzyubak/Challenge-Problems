
from pair_in_seq_add_to_target_sum import find_pair_in_seq_naive, find_pair_in_seq_complement, find_pair_in_seq_complement, find_pair_in_seq_complement
import pytest

# This is a unit test file for pair_in_seq_add_to_target_sum 
def test_find_pair_in_seq_naive(): 
    assert_common(find_pair_in_seq_naive)


def test_find_pair_in_seq_complement(): 
    assert_common(find_pair_in_seq_complement)


def test_find_pair_in_seq_complement_sorted(): 
    assert_common(find_pair_in_seq_complement)


def test_find_pair_in_seq_iterative(): 
    assert_common(find_pair_in_seq_complement)


def assert_common(func): 
    assert len(func([1,2,3,9],8)) == 0, 'No matching values'
    assert len(func([1,2,4,4],8)) == 2


if __name__ == '__main__': 
    retcode = pytest.main()
    print('Everything passed.')