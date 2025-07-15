def expand_range(input_string, delimiters=('-', '..', 'to', '~')):
    """
    Expand a comma-separated string of numbers and ranges into a list of integers.
    Handles whitespace, empty tokens, custom delimiters, reversed ranges, and invalid inputs.
    Example: "5-3,3..3" -> [5, 4, 3, 3]
    """
    result = []
    tokens = [token.strip() for token in input_string.strip().split(',')]
    tokens = [token for token in tokens if token]
    
    for token in tokens:
        try:
            delimiter_used = None
            for delimiter in delimiters:
                if delimiter in token:
                    delimiter_used = delimiter
                    break
            if delimiter_used:
                start, end = map(int, token.split(delimiter_used))
                if start <= end:
                    result.extend(range(start, end + 1))
                else:
                    result.extend(range(start, end - 1, -1))
            else:
                result.append(int(token))
        except ValueError:
            raise ValueError(f"Invalid input: '{token}' is not a valid number or range")
    
    return result