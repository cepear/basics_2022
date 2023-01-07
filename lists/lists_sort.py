#Chapter 3 Sorting  sort() - permanent sorting,  sorted() - temporary sorting
cars = ['bmw', 'toyota', 'lexus', 'moskvich', 'tesla']
print("List before sorting  ", cars)
cars.sort()
print("LIst after sorting ", cars)

names = ['john', 'nina','jane', 'mark']
print("Before sort ", names)
names.sort(reverse=True)
print("After ", names)

print("Sorting temporary - sorted()")
car_models = ['corolla', 'camry', 'honda', 'modelX', '550xi']
sorted_car_models_asc = sorted(car_models)
sorted_car_models_desc = sorted(car_models, reverse=True)

print(sorted_car_models_asc)
print(sorted_car_models_desc)
print(car_models)

# reversing list without sorting:
nums = [6, 3, 9, 7, 10]
print(nums)
nums.reverse()
print(nums)

#  number of elements in list len()
print(len(nums))
print(len(names))
print(len(cars))
print(nums[-1])
print(names [3])
print(cars[4])




