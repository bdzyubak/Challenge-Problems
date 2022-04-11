
import pair_in_seq_add_to_target_sum as find_sum

# This is a unit test file for pair_in_seq_add_to_target_sum 
def test_find_pair_in_seq_naive(): 
    assert len(find_sum.find_pair_in_seq_naive([1,2,3,9],8)) == 0, 'No matching values'
    assert len(find_sum.find_pair_in_seq_naive([1,2,4,4],8)) == 2


def test_find_pair_in_seq_complement(): 
    assert len(find_sum.find_pair_in_seq_complement([1,2,3,9],8)) == 0, 'No matching values'
    assert len(find_sum.find_pair_in_seq_complement([1,2,4,4],8)) == 2


if __name__ == '__main__': 
    test_find_pair_in_seq_naive()
    test_find_pair_in_seq_complement()
    print('Everything passed.')