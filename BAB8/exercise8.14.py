def make_car(manufacturer, model, **car_info):
    car = {
        "manufacturer": manufacturer,
        "model": model
    }

    car.update(car_info)
    return car

car = make_car(
    "Nissan",
    "GTR R35",
    color="Black",
    tow_package=True
)

print(car)