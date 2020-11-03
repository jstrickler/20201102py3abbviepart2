
class AirportsRouter:
    def db_for_read(self, model, **hints):
        if model._meta.label.split('.')[-1] == 'Airports':
            return 'airports'
