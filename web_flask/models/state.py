@property
def cities(self):
    """Returns the list of City objects linked to the current State"""
    from models import storage
    from models.city import City
    city_list = []
    for city in storage.all(City).values():
        if city.state_id == self.id:
            city_list.append(city)
    return city_list
