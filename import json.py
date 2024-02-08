import json

class JsonObject:
    def __init__(self):
        self.data = {}

    def add_value(self, key, value):
        self.data[key] = value
        return self  # Return self to allow method chaining

    def add_array_of_objects(self, key, object_list):
        objects = []
        for obj in object_list:
            if isinstance(obj, JsonObject):
                objects.append(obj.data)
            else:
                raise ValueError("Elements in the list must be instances of JsonObject")

        self.data[key] = objects
        return self  # Return self to allow method chaining

    def to_json_string(self):
        return json.dumps(self.data, separators=(',', ':'), ensure_ascii=False, cls=JsonObjectEncoder)

class JsonObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, JsonObject):
            return obj.data
        return super().default(obj)

# List to store JSON strings
json_objects_list = []


# Example usage
json_object1 = (
    JsonObject()
    .add_value("name", "John")
    .add_value("age", 25)
    .add_value("city", "New York")
    .add_array_of_objects("friends", [
        JsonObject().add_value("name", "Jane").add_value("age", 28).add_value("city", "San Francisco"),
        JsonObject().add_value("name", "Bob").add_value("age", 22).add_value("city", "Los Angeles")
    ])
)

json_object2 = (
    JsonObject()
    .add_value("name", "Alice")
    .add_value("age", 30)
    .add_value("city", "Seattle")
    .add_array_of_objects("friends", [
        JsonObject().add_value("name", "Charlie").add_value("age", 35).add_value("city", "Chicago"),
        JsonObject().add_value("name", "David").add_value("age", 27).add_value("city", "Boston")
    ])
)

json_object3 = (
    JsonObject()
    .add_value("name", "Gian")
    .add_value("age", 22)
    .add_value("city", "Genoa")
    .add_array_of_objects("friends", [
        JsonObject().add_value("name", "Charlie").add_value("age", 35).add_value("city", "Chicago"),
        JsonObject().add_value("name", "David").add_value("age", 27).add_value("city", "Boston")
    ])
)


# Append JSON strings to the list
json_objects_list.append(json_object1.to_json_string())
json_objects_list.append(json_object2.to_json_string())
json_objects_list.append(json_object3.to_json_string())

with open('output.json', 'w') as file:
    print("[", file=file)
    for index, value in enumerate(json_objects_list):
        if index < len(json_objects_list) - 1:
            print(value + ",", file=file)
        else:
            print(value , file=file)
    print("]", file=file)