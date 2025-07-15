def expand_range(input_string, delimiters=('-', '..', 'to', '~'), step_delimiter=':'):
    result = []
    tokens = [token.strip() for token in input_string.strip().split(',')]
    tokens = [token for token in tokens if token]
    
    for token in tokens:
        try:
            step = 1
            delimiter_used = None
            for delimiter in delimiters:
                if delimiter in token:
                    delimiter_used = delimiter
                    break
            if delimiter_used:
                if step_delimiter in token:
                    range_part, step = token.split(step_delimiter)
                    start, end = map(int, range_part.split(delimiter_used))
                    step = int(step)
                else:
                    start, end = map(int, token.split(delimiter_used))
                if start <= end:
                    result.extend(range(start, end + 1, step))
                else:
                    result.extend(range(start, end - 1, -step))
            else:
                result.append(int(token))
        except ValueError:
            raise ValueError(f"Invalid input: '{token}' is not a valid number or range")
    
    return result