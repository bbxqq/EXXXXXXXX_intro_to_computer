class Animals():
    def __init__(self, weight, mood, _type):
        self.weight = weight
        self.mood = mood
        self._type = _type
    def feed(self):
        pass
    def walk(self):
        pass
    def bath(self):
        self.mood -= 2
    def printf(self, n_feed, n_walk, n_bath):
        if(n_feed > 0):
            self.feed()
        if(n_walk > 0):
            self.walk()
        if(n_bath > 0):
            self.bath()
        n_feed -= 1
        n_walk -= 1
        n_bath -= 1
        if(n_feed > 0 or n_walk > 0 or n_bath > 0):
            self.printf(n_feed, n_walk, n_bath)
        else:
            print(self._type + '現在的體重=', round(self.weight, 2), 'kg, 心情', self.mood)
            if(self.mood > 90):
                print('mood最高只能為= 90')
                print('所以，' + self._type + '現在的心情', 90 )
class Dogs(Animals):
    def feed(self):
        self.weight += 0.2
        self.mood += 1
    def walk(self):
        self.weight -=0.2
        self.mood += 2

class Cats(Animals):
    def feed(self):
        self.weight += 0.1
        self.mood += 1     
    def walk(self):
        self.weight -= 0.1
        self.mood -= 1
class Shiba(Dogs):
    def feed(self):
        self.weight += 0.3
        self.mood += 5
dog = Dogs(4.8, 65, '狗狗') 
dog.printf(18, 10, 4) 

cat = Cats(8.2, 60, '貓貓') 
cat.printf(40, 7, 1) 

shiba = Shiba(5, 70, '柴犬')
shiba.printf(20, 10, 3)
