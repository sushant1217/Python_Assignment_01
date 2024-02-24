def generate_square_dictionary(n):
    square_dict = {} 
    for i in range(1, n + 1):  
        square_dict[i] = i * i 
    return square_dict

n = int(input("Enter a number: "))

result_dict = generate_square_dictionary(n)

print(result_dict)
