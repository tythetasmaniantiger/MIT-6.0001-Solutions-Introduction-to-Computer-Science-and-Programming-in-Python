# Problem Set 4A
# Name: G.A.
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    # Long strings take a very long time to compute, best to avoid
    assert type(sequence) == str, "non-string entry"
    assert len(sequence) > 0, "invalid string length"

    if len(sequence) == 1:
        return [sequence]
    else:
        perm_list = []
        for elt in get_permutations(sequence[1:]):
            for k in range(len(sequence)):
                perm_list.append(elt[:k] + sequence[0] + elt[k:])
        perm_list = list(set(perm_list))
        return perm_list
        

if __name__ == '__main__':
    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input),"\n")
    
    example_input = 'a'
    print('Input:', example_input)
    print('Expected Output:', ['a'])
    print('Actual Output:', get_permutations(example_input),"\n")
    
    example_input = 'bee'
    print('Input:', example_input)
    print('Expected Output:', ['bee', 'ebe', 'eeb'])
    print('Actual Output:', get_permutations(example_input),"\n")
    
    example_input = 'Aa'
    print('Input:', example_input)
    print('Expected Output:', ['Aa', 'aA'])
    print('Actual Output:', get_permutations(example_input),"\n")
    


