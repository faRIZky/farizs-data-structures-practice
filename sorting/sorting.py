# BASIC OF SORTING

print()
print("SORT ===")

numbers = [5, 3, 8, 1, 2]
numbers.sort()                              # modifying the original list
print(numbers)

numbers = [5, 3, 8, 1, 2]
sorted_list = sorted(numbers)
print(f"sorted_list: {sorted_list}")
print(f"original list: {numbers}")

# REVERSE
print()
print("REVERSE ===")

numbers = [5, 3, 8, 1, 2]
numbers.sort(reverse=True)
print(f"sort() :{numbers}")

numbers = [5, 3, 8, 1, 2]
sorted_list_reversed = sorted(numbers, reverse=True)
print(f"reversed sorted list: {sorted_list_reversed} ")
print(f"original list: {numbers}")

# SORT WITH KEY PARAMETERS
print()
print("KEY PARAM ===")

words = ["apple", "kiwi", "banana", "cherry"]
words.sort(key=len)
print(f"sorted by length: {words}")

numbers = [10, -3, 2, -15]
numbers.sort(key=abs)
print(f"sorted by abs value: {numbers}")

def fun(word):
    return word[-1]
words = ["apple", "kiwi", "banana", "cherry"]
last_alphabet_sorting = sorted(words, key=fun)
print(f"sorting with custom function by last alphabet: {last_alphabet_sorting}")

# SORT WITH KEY PARAMETERS (OOP)
print()
print("KEY PARAM OOP ===")

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __repr__(self):
        return f"{self.name} ({self.age}) from {self.city}"

    # list of Person objects
people = [
    Person("Alice", 30, "Cia"),
    Person("Bob", 24, "Neb"),
    Person("Charlie", 29, "NY")
]
    # sort people by age
people.sort(key=lambda person:person.age)
print("Sorted by age:", people)

    # sort people by name
people.sort(key=lambda person:person.name)
print("Sorted by name:", people)

    # sort people by city
people.sort(key= lambda person: person.city)
print("Sorted by city:", people)

# another case

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} ({self.price})"

listItem = [
    Item("pizza", 100),
    Item("orange", 200),
    Item("rice", 15)
]

listItem.sort(key=lambda Item1 : Item1.name, reverse=True)
print("Sorted by name:", listItem)