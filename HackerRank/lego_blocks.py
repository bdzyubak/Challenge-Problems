def first_row(m): 
    num = build_row_rec(m+1)
    return num

def build_row_rec(m_new):
    if m_new <=0: 
        return 0
    if m_new == 1: 
        return m_new
    num = 0
    for width in [1,2,3,4]: 
        num += build_row_rec(m_new-width)
    return num

def test_count_ways(): 
    correct_counts = {1:1,2:2,3:4,4:8,5:15,6:29,7:56,8:108,9:208,10:401}
    
    for i in range(1,11): 
        answer = first_row(i)
        correct_answer = correct_counts[i]
        assert answer == correct_answer, 'Test failed for ' + str(i) + ' width. \
            Was ' + str(answer) + ' should be ' + str(correct_answer)

if __name__ == '__main__': 
    print('Testing building of single row.')
    test_count_ways()

    print('Tests Passed.')