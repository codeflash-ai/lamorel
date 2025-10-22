from functools import reduce

concat = lambda x, y: x + y
concat_all = lambda xs: reduce(concat, xs, [])


def flatten_list(seqs):
    flattened, list_map = [], []
    for seq in seqs:
        flattened.extend(seq)
        list_map.append(len(seq))

    return flattened, list_map
