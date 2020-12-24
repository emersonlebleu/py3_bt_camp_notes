#---Iterators & Generators---

#--Iterator--
#an object that can be iterated upon


#--Iterable
#an object which will return an iterator when iter() is called upon it
#the string "Hello" os an iterable

#--next() when called on an iterator it returns the next item until stopiteration err

#custom for loop
def my_for(iterable, func):
    iteraor = iter(iterable)
    while True:
        try:
            thing = next(iteraor)
        except StopIteration:
            break
        else:
            func(thing)

def square(x):
    print(x*x)

my_for("hello", print)
my_for([1,2,3,4,5,6,7], square)

#--Writing a custom Iterator--
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration

for x in Counter(0,24):
    print(x)

#--Generators--
#subset of iterators

#generator fuctions with yield keyword
#can return/yield more than once and returns a generator which is an itorator

#example generator use
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

count = count_up_to(4)
#then you can iterate on the new variable
for num in count: 
    print(num)