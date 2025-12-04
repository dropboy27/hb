def unique_preserve_order(iterable):
    exists = set()
    result = []

    for item in iterable:
        if item not in exists:
            result.append(item)
            exists.add(item)

    return result
