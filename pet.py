class Pet:
    allowed = ["cat","dog","fish","rat"]

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"Sorry {species}s are not allowed...")
        self.name = name
        self.species = species

cat = Pet("Walter", "Cat")
dog = Pet("Carter","Dog")
