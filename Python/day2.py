# def display(data):
#     print(f"the area is {data}")

# def get_input():
#     received_length=float(input("length  "))
#     received_width=float(input("width  "))
#     return (received_length,received_width)

# def compute_area(length,width):
#     data=float(length*width)
#     return data

# def main():
#     length,width=get_input()
#     data=compute_area(length,width)
#     display(data)

# main()


# def get_input():
#     n1 = float(input("Enter the number one: "))
#     n2 = float(input("Enter the number two: "))
#     n3 = float(input("Enter the number three: "))
#     n4 = float(input("Enter the number four: "))
#     return n1, n2, n3, n4

# def compute_sum(num1, num2, num3, num4):
#     sum = num1 + num2 + num3 + num4
#     return sum

# def compute_avg(sum):
#     average=sum/4
#     return average

# def display(average):
#     print(f"The average of the given four numbers is {average}")

# def main():
#     num1, num2, num3, num4 = get_input()  #inputs
#     sum = compute_sum(num1, num2, num3, num4) #sum
#     average=compute_avg(sum) #average
#     display(average) #display average

# main()

def get_input():
    n1 = float(input("Enter the number one: "))
    n2 = float(input("Enter the number two: "))
    n3 = float(input("Enter the number three: "))
    return n1,n2,n3

def Big_One(num1,num2,num3):
    if(num1>num2 and num1>num3):
        print(f"Number {num1} is Big ")
    elif(num2>num1 and num2>num3):
        print(f"Number {num2} is Big")
    else:
        print(f"Number {num3} is Big")

def main():
    n1,n2,n3=get_input()
    Big_One(n1,n2,n3)
main()