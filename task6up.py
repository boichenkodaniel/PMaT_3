class MyList(list):
    def double(self):
        return MyList([x * 2 for x in self])
    def sum(self):
        return sum(self)

my_list = MyList([1, 2, 3, 4, 5])
print(my_list)
my_list.append(6)
print(my_list)
print(my_list.double())
print(my_list.sum())