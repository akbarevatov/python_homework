class Vector:
    def __init__(self, *numbers):
        self.numbers=numbers
    def __str__(self):
        return f"Vector{self.numbers}"
    def __add__(self, other):
        if len(self.numbers)!=len(other.numbers):
            raise ValueError("Two vectors are not of the same dimention!")
        return Vector(*(a+b for a,b in zip(self.numbers, other.numbers)))
    def __sub__(self, other):
        if len(self.numbers)!=len(other.numbers):
            raise ValueError("'Two vectors are not of the same dimension!")
        return Vector(*(a-b for a,b in zip(self.numbers,other.numbers)))
    
    
vec1 = Vector(1,2,5,4,6)
vec2 = Vector(2,1,4,1,1)
vec3 = vec2-vec1
print(vec3)
print(vec1+vec2)