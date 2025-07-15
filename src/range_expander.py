def expand_range(input_string):
    result = []
    tokens = input_string.split(',')
    for token in tokens:
        if '-' in token:
            start, end = map(int, token.split('-'))
            result.extend(range(start, end + 1))
        else:
            result.append(int(token))
    return result