def remove_duplicates(lst):
    """Removes duplicate elements from a list."""
    return list(set(lst))

def chunk_list(lst, size):
    """Splits a list into smaller chunks of a specified size."""
    return [lst[i:i + size] for i in range(0, len(lst), size)]
