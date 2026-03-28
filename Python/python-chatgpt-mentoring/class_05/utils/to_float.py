def to_float(s: int | float | str) -> float:
    try:
        return float(s)
    # Handle the case where the string cannot be converted to a float
    except ValueError:
        return 0.0

# Export the function
__all__ = ['to_float']