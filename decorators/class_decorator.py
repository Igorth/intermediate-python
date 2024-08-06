class Person:
    species = "Homo sapiens"

    @classmethod
    def get_species(cls):
        print(cls)
        return cls.species


# Usage
print(Person.get_species())
