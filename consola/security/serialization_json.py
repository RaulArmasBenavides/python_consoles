import json
import datetime

class SafeExploitEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()  # More standardized date-time representation
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

def serialize():
    data = [list(range(10)), datetime.datetime.now()]
    json_data = json.dumps(data, cls=SafeExploitEncoder)
    print(json_data)
    return json_data

def deserialize(exploit_code):
    # Assuming the datetime strings are in ISO format
    def date_hook(json_dict):
        for (key, value) in json_dict.items():
            try:
                json_dict[key] = datetime.datetime.fromisoformat(value)
            except (TypeError, ValueError):
                pass
        return json_dict
    
    data = json.loads(exploit_code, object_hook=date_hook)
    print(data)

if __name__ == '__main__':
    serialized_data = serialize()
    deserialize(serialized_data)