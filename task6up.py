class MyList(list):
    def double(self):
        return MyList([x * 2 for x in self])
    def sum(self):
        return sum(self)

my_list = MyList([1, 2, 3, 4, 5])
print(f"Список:{my_list}")
my_list.append(6)
print(f"Список с добавленным элементом:{my_list}")
print(f"Список с удвоенными элементами:{my_list.double()}")
print(f"Сумма элементов списка:{my_list.sum()}")