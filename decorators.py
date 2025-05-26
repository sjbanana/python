def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Hai aggiunto gli sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("Hai aggiunto fudge")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Ecco il tuo gelato al gusto {flavor}")

get_ice_cream("vaniglia")