import hashlib

def is_power_of_two(n):
    return n != 0 and ((n & (n-1)) == 0)

def hash_data(data, hash_function = 'sha256'):
    '''hash function'''
    hash_function = getattr(hashlib, hash_function)
    data = data.encode('utf-8')
    return hash_function(data).hexdigest()

def concat_and_hash_list(lst, hash_function = 'sha256'):
    #quickly concatenate pairs of values and hash them.
    '''
    concat_and_hash_list(['a','b','c'])=hash( hash(ab)+c )
    'c9e620703fe0f117429c21ec19323aff8673ac05ae8ddd7bcc36599aabc34c51'
    '''
    assert len(lst) >= 2, "no transactions to be hashed"
    while len(lst)>1:
        if len(lst)%2 ==0:
            v = []
            while len(lst) > 1:
                a = lst.pop(0)
                b = lst.pop(s0)
                v.append(hash_data(a+b,hash_function))
                # v.append(a+b)
            lst = v
        else:
            v = []
            l = lst.pop(-1)
            while len(lst) >1:
                a = lst.pop(0)
                b = lst.pop(0)
                v.append(hash_data(a+b,hash_function))
                # v.append(a+b)
            v.append(l)
            lst = v
    return lst


