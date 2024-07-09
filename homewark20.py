import itertools
def all_variants(text):
    list_ = []
    for list_1 in range(len(text) + 1):
        list_.append(list(itertools.combinations(text, list_1)))
    for list_2 in list_:
        for list_3 in list_2:
            if ''.join(list_3) != 'ac':
                yield ''.join(list_3)


a = all_variants("abc")
for i in a:
    print(i)
