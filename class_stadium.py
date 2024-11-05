import json
import pickle

class Stadium:
    def __init__(self, name: str, capacity: int, location: str):
        self.name = name
        self.capacity = capacity
        self.location = location

    def host_event(self, event_name: str):
        return f"{self.name} is hosting {event_name}."

    def get_details(self):
        return f"{self.name} located in {self.location}, capacity: {self.capacity}."

    class StadiumAdapter:
        @staticmethod
        def serialize(stadium):
            return {
                'name': stadium.name,
                'capacity': stadium.capacity,
                'location': stadium.location
            }

        @staticmethod
        def deserialize(data):
            return Stadium(data['name'], data['capacity'], data['location'])

    def to_json(self):
        return json.dumps(self.StadiumAdapter.serialize(self))

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        return Stadium.StadiumAdapter.deserialize(data)

    def to_pickle(self):
        return pickle.dumps(self)

    @staticmethod
    def from_pickle(pickle_data):
        return pickle.loads(pickle_data)

# Пример использования
stadium = Stadium("Camp Nou", 99354, "Barcelona")
json_data = stadium.to_json()
print(json_data)
new_stadium = Stadium.from_json(json_data)
print(new_stadium.host_event("football match"))
pickle_data = stadium.to_pickle()
new_stadium_from_pickle = Stadium.from_pickle(pickle_data)
print(new_stadium_from_pickle.get_details())