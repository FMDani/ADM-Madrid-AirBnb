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

def write_to_json_file(filename, json_objects_list):
    with open(filename, 'w', encoding='utf-8') as file:
        print("[", file=file)
        for index, value in enumerate(json_objects_list):
            if index < len(json_objects_list) - 1:
                print(value + ",", file=file)
            else:
                print(value , file=file)
        print("]", file=file)



