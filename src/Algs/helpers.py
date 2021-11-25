def parse_signature(signature):
    prefix, *metaoperations_s = signature.split(',')
    t, n, r = prefix.split('_')
    n = int(n)
    r = int(r)
    return t, n, r, metaoperations_s
