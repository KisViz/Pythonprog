#dekoratorok
#fagyi + cukorka

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*You add sprinkles:)*")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You add fudge:*")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavour: str):
    print(f"Here is your {flavour} ice cream!")

def add_sprinkles2(func):
    # def wrapper(): #igy nem jo!!!!!!!!!!
        print("*You add sprinkles:)*2")
        func()
    # return wrapper

@add_sprinkles2
def get_ice_cream2():
    print("Here is your ice cream!2")

if __name__ == "__main__":
    print("\n---------\n")
    get_ice_cream("vanilla")

    #a masikat meg se kell hivni is megy magatol mert nincs wrapperben
    #nekunk ez igy nem jo!!!!