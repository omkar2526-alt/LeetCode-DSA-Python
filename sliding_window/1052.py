# customers = [1, 0, 1, 2, 1, 1, 7, 5]
# grumpy =    [0, 1, 0, 1, 0, 1, 0, 1]
# minutes = 3

customers = list(map(int,input().split(",")))
grumpy = list(map(int,input().split(",")))
minutes = int(input())

def grumpy_book_store(customers,grumpy,minutes):
    customer_satisfied = 0
    extra_satisfied_customer = 0

    for i in range(len(grumpy)):
        if grumpy[i] == 0:
            customer_satisfied += customers[i]
            
    for i in range(minutes):
        if grumpy[i] == 1 :
            extra_satisfied_customer += customers[i]
            
    for i in range(minutes,len(customers)):
        if grumpy[i] == 1 :
            extra_satisfied_customer += customers[i]
        if grumpy[i-minutes] == 1:
            extra_satisfied_customer -= customers[i-minutes]
        
    return (customer_satisfied+extra_satisfied_customer)
    
print(grumpy_book_store(customers,grumpy,minutes))   