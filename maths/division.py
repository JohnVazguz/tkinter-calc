def division(*args):
    if len(args) < 2 or 0 in args[1:]:
        raise ValueError("Invalid input for division.")
    result = args[0]
    for num in args[1:]:
        result /= num
    return result