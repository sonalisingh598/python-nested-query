def get_value_from_nested_object(obj, key):
    keys = key.split("/")
    value = obj

    for k in keys:
        if isinstance(value, dict) and k in value:
            value = value[k]
        else:
            # Handle missing keys or non-dict values
            return None

    return value

#we can use the above function by passing your nested object and the desired key as arguments.

object1 = {"a": {"b": {"c": "d"}}}
key1 = "a/b/c"
value1 = get_value_from_nested_object(object1, key1)
print(value1)  # Output: d

object2 = {"x": {"y": {"z": "a"}}}
key2 = "x/y/z"
value2 = get_value_from_nested_object(object2, key2)
print(value2)  # Output: a

