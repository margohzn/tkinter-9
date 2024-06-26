
class Dog:
    #adding atributes for a dog: breed, color...
    breed = "golden"
    color = "white"
    
    def show_detail(self):
        print("I am a", self.color, self.breed)


dog = Dog()
dog.show_detail()
