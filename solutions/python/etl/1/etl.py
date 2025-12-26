def transform(legacy_data):
    new_data = {}
    for key, value in legacy_data.items():
        print(value)
        for letter in value:
            new_data[letter.lower()] = key
    return new_data
