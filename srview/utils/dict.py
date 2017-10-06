
def has_keys(dct, *keys):
    """
    True iff all specified keys are present in dct
    """
    for key in keys:
        if not key in dct:
            return False
    return True