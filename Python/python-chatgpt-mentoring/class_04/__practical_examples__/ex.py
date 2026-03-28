# 1. Iterables and transformations
# Iterables are objects that can be iterated over, such as lists, tuples, and strings.
# Transformations are operations that can be applied to iterables to produce new iterables.
# For example, we can use the map() function to apply a transformation to each element of an iterable.

currencies = ['USD', 'EUR', 'JPY']

#Best: comprehension
upper = [c.upper() for c in currencies]

# Works, but often less readable
upper2 = list(map(str.upper, currencies))

# lambda is ok, but usually avoid when a normal function exists
upper3 = list(map(lambda c: c.upper(), currencies))

# Outputs:
print("Comprehension:", upper)  # ['USD', 'EUR', 'JPY']
print("Map with function:", upper2) # ['USD', 'EUR', 'JPY']
print("Map with lambda:", upper3) # ['USD', 'EUR', 'JPY']

# For "join allowed values" in an error message:
allowed = ['USD', 'EUR', 'JPY']
msg = "Must be one of: " + ", ".join(allowed) # Already strings
print(msg)  # Must be one of: USD, EUR, JPY

# If they are not strings:
allowed = [1, 2, 3]
msg2 = "Must be one of:" + ",".join(map(str, allowed)) # Convert to strings first"
print(msg2)  # Must be one of: 1, 2, 3


# 2. Dictionaries vs arrays/objects
# Python equivalents:
# list -> like an Array
# dict -> most similar to a JS Object / map (key -> value) (but not exactly, since it can have non-string keys)
# tuple -> like an immutable list (like a frozen array - fixed-size vibe)
# set -> unique value, fast membership checks (x in set) (like a JS Set)

# So for validation checks like "is currency allowed?", use a set:
currency = 'USD'
ALLOWED_CURRENCIES = {'USD', 'EUR', 'JPY'} #set
if currency not in ALLOWED_CURRENCIES:
    raise ValueError("Invalid currency")
