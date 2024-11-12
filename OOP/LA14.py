class Spiderman():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describeSpiderman(self):
        print(f"Name: {self.name} - Age: {self.age}")


class Tobey(Spiderman):
    def __init__(self, name, age, movieTitle):
        super(). __init__(name, age) 
        self.movieTitle = movieTitle

class Andrew(Spiderman):
    def __init__(self, name, age, movieTitle):
        super(). __init__(name, age)
        self.movieTitle = movieTitle

class Tom(Spiderman):
    def __init__(self, name, age, movieTitle):
        super(). __init__(name, age)
        self.movieTitle = movieTitle


tobey = Tobey("Tobey", 49, "Spiderman")
andrew = Andrew("Andrew", 41, "The Amazing Spiderman")
tom = Tom("Tom", 28, "Captain America: Civil War (2016)")

for item in (tobey, andrew, tom):
    print(f"{item.name.upper()} - {item.movieTitle}")

# print(f"{tobey.name.upper()} - {tobey.movieTitle}")
# print(f"{andrew.name.upper()} - {andrew.movieTitle}")
# print(f"{tom.name.upper()} - {tom.movieTitle}")