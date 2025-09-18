# import matplotlib.pyplot as plt
# import numpy as np
# from sklearn.linear_model import LinearRegression

# Sets

# my_set = {1, 2, 3, 4, 5, 5}
# my_set.add(100)
# my_set.add(2)
# print(my_set)

# my_list = [1, 2, 3, 4, 4, 5, 5]
# print(set(my_list))
# print(list(my_set))

# new_set = my_set.copy()
# my_set.clear()
# print(my_set)
# print(new_set)
# print('\n')


# # Set Methods

# my_set = {1, 2, 3, 4, 5}
# your_set = {4, 5, 6, 7, 8, 9, 10}

# print(my_set.difference(your_set))
# print(my_set.intersection(your_set))
# print(my_set.isdisjoint(your_set))
# print(my_set.issubset(your_set))
# print(my_set.issuperset(your_set))
# print(my_set.union(your_set))
# my_set.difference_update(your_set)
# print(my_set)
# my_set.discard(5)
# print(my_set)

my_set = {1,2,3,4,5}
print(my_set)
my_set.add(100000)
my_set.add('Hans og Grethe')
print(my_set)

my_list = [1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,4,5,6,1]
no_dup = set(my_list)
print(no_dup)

set_test = {1,2,3,4,5,65,6,6,6,6,6,4}
list_test = list(set_test)
print(list_test)

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a - set_b)
set_a.difference_update(set_b)
print(set_a)
print(set_a.isdisjoint(set_b))



# # 1. Define your Haar wavelet coefficients
# coefficients = np.array([2.75, -1.25, 0.5, 0, 0, -1, -1, 0])
# x_pos = np.arange(len(coefficients))

# # 2. Create the plot
# fig, ax = plt.subplots(figsize=(10, 6))

# # Create the bar chart
# ax.bar(x_pos, coefficients, color='skyblue', edgecolor='black')

# # Add a horizontal line at y=0 for reference
# ax.axhline(0, color='grey', linewidth=0.8)

# # 3. Add lines and text to show the multi-resolution structure
# # Line after the approximation coefficient
# ax.axvline(x=0.5, color='r', linestyle='--', linewidth=2)
# # Line after the first level of detail
# ax.axvline(x=1.5, color='g', linestyle='--', linewidth=2)
# # Line after the second level of detail
# ax.axvline(x=3.5, color='b', linestyle='--', linewidth=2)

# # Add text labels for each section
# ax.text(0, max(coefficients) * 0.9, 'Approx.', ha='center', va='bottom', fontsize=12)
# ax.text(1, max(coefficients) * 0.9, 'Detail L3', ha='center', va='bottom', fontsize=12)
# ax.text(2.5, max(coefficients) * 0.9, 'Detail L2', ha='center', va='bottom', fontsize=12)
# ax.text(5.5, max(coefficients) * 0.9, 'Detail L1', ha='center', va='bottom', fontsize=12)


# # 4. Set labels and title for clarity
# ax.set_xticks(x_pos)
# ax.set_xlabel('Coefficient Index')
# ax.set_ylabel('Magnitude')
# ax.set_title('Haar Wavelet Coefficients (Multi-Resolution Plot)')
# ax.grid(axis='y', linestyle=':', alpha=0.7)

# # 5. Display the plot
# plt.tight_layout()
# plt.show()




# # 1. Our original "noisy" data
# experience = np.array([1, 2, 3, 4, 5])
# noisy_salary = np.array([45, 55, 60, 62, 75])

# # Scikit-learn expects the input (X) to be a 2D array, so we reshape it
# X = experience.reshape(-1, 1)
# y = noisy_salary

# # 2. Create and train the linear regression model
# model = LinearRegression()
# model.fit(X, y)

# # 3. Get the "smoothed" values by predicting from the model
# # The model has learned the trend, so predicting gives us the points on the line
# smoothed_salary = model.predict(X)

# # 4. Print the results for comparison
# print("Original (Noisy) Salaries:", noisy_salary)
# print("Smoothed Salaries (from line):", np.round(smoothed_salary, 1))

# # 5. Visualize the results
# plt.figure(figsize=(8, 6))
# # Plot the original noisy data points
# plt.scatter(X, y, color='blue', label='Original Noisy Data')
# # Plot the regression line (the smoothed trend)
# plt.plot(X, smoothed_salary, color='red', linewidth=2, label='Regression Line (Smoothed Trend)')

# plt.title('Regression for Data Smoothing')
# plt.xlabel('Years of Experience')
# plt.ylabel('Salary (in thousands)')
# plt.legend()
# plt.grid(True)
# plt.show()

fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f'Index of {char} = {i}')
                         