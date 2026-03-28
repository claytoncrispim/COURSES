# Basic data types in Python

msg: str = "Hello, World!"
print(msg)

name: str = "John" # String data type to store text values
count: int = 42 # Integer data type to store whole numbers
price: float = 19.99 # Float data type to store decimal numbers
is_available: bool = True # Boolean data type to store True or False values
items: list[str] = ["apple", "banana", "cherry"] # List data type to store an ordered collection of items (in this case, a list of strings) List is a mutable data type, meaning you can modify its contents after creation.
print("Data Types:", name, count, price, is_available, items, sep="\n")

profile: dict[str, str] = {
    "id": "1",
    "name": "Alice",
    "age": "30",
    "city": "New York"
} # Dictionary data type to store key-value pairs. In this case, a dictionary representing a user profile with keys like "id", "name", "age", and "city". Dictionary is a mutable data type, allowing you to add, modify, or remove key-value pairs after creation. In JavaScript, dict is the equivalent of an object, where you can store properties and their corresponding values.

#print(profile)

objects: list[dict] = [
    {
        "name": "apple",
        "type": "fruit",
        "color": "red",
        "price": 0.5
    }, {
        "name": "banana",
        "type": "fruit",
        "color": "yellow",
        "price": 0.3
    }, {
        "name": "cherry",
        "type": "fruit",
        "color": "red",
        "price": 0.2
    }]

print(objects[2]["name"])

