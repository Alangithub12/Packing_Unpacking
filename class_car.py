import json
import pickle

class Automobile:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        return f"{self.brand} {self.model}'s engine started."

    def stop_engine(self):
        return f"{self.brand} {self.model}'s engine stopped."

    def to_json(self):
        return json.dumps({
            'brand': self.brand,
            'model': self.model,
            'year': self.year
        })

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        return Automobile(data['brand'], data['model'], data['year'])

    def to_pickle(self):
        return pickle.dumps(self)

    @staticmethod
    def from_pickle(pickle_data):
        return pickle.loads(pickle_data)

# Пример использования
car = Automobile("Toyota", "Corolla", 2020)
json_data = car.to_json()
print(json_data)
new_car = Automobile.from_json(json_data)
print(new_car.start_engine())
pickle_data = car.to_pickle()
new_car_from_pickle = Automobile.from_pickle(pickle_data)
print(new_car_from_pickle.stop_engine())