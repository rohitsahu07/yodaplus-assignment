def expand_range(input_string, delimiters=('-', '..', 'to', '~')):
    result = []
    tokens = [token.strip() for token in input_string.strip().split(',')]
    tokens = [token for token in tokens if token]
    
    for token in tokens:
        delimiter_used = None
        for delimiter in delimiters:
            if delimiter in token:
                delimiter_used = delimiter
                break
        if delimiter_used:
            start, end = map(int, token.split(delimiter_used))
            result.extend(range(start, end + 1))
        else:
            result.append(int(token))
    
    return result