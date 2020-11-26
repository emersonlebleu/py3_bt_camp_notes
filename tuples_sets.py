#tuples & sets

#tuple: ordered collection of items that is immutable ()
#tuples are faster than lists, and you can always expect the tuple to be the same
#usecases: months, days of the week etc.
#can use tuple as key in dictionary (not lists)
#lots of methods return tuples

months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov","Dec")

#tuple methods & loops
for month in months:
    print(month)
print(months.index("Feb"))

#sets: formal mathematical sets
#no duplicate values with no order cannot use indexing obviously because there is no order
#can use loops just fine
#usecases: easily allows for you to find unique values in some larger body of data
    #can simply create a set(some iterable) returns set of the unique values of the iterable
some_set = {1,2,3,4,5}
print(4 in some_set)
print(len(some_set))
some_set.add(6) #only can add one item at a time
print(some_set)
some_set.remove(2) #could use .discard() if you didnt want any key errors for missing val
print(some_set)

#set math: union, intersection, Symmetric_difference 
#set comps: Same as dictionary but without the : 
    #mostly used more for the set math/like behavior 