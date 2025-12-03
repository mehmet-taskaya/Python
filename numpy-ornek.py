import numpy as np

# 1 boyutlu array oluşturma
arr1d = np.array ([1, 2, 3, 4, 5])

# 2 boyutlu array oluşturma
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Sıfırlardan oluşan bir array oluşturma
zeros_array = np.zeros ((3, 3)) # 3x3 boyutunda sıfırlardan oluşan array

# Birlerden oluşan bir array oluşturma
ones_array = np.ones((2, 4)) # 2x4 boyutunda birlerden oluşan array

# Belirli bir aralıkta sayılar içeren bir array oluşturma
range_array = np.arange(0, 10, 2) #0'dan 10'a kadar 2'şer artan sayılar

# Belirli bir aralıkta eşit aralıklı sayılar içeren bir array oluşturma
linspace_array = np.linspace(0, 5, 10) # 0 ile 5 arasında 10 eşit aralıklı sayı

# Rastgele sayılardan oluşan bir array oluşturma
random_array = np.random.randint(0, 10, size=(3, 3)) #0 ile 10 arasında rastgele sayılan

print(arr1d)
print(arr2d)
print(zeros_array)
print (ones_array)
print(range_array)
print (linspace_array)
print(random_array)