def expand_range(input_string):
    result = []
    tokens = [token.strip() for token in input_string.strip().split(',')]
    tokens = [token for token in tokens if token]
    
    for token in tokens:
        if '-' in token:
            start, end = map(int, token.split('-'))
            result.extend(range(start, end + 1))
        else:
            result.append(int(token))
    
    return result