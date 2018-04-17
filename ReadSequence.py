__author__ = 'Razvan'
#sequence = 1
#while sequence != "0":
 #   sequence = input("Geef in een sequence van cijfers: ")

 #   sequence.split(" ",)
#
 #   print(sequence.isdigit())

#string = input("geef numbers ")
#numbers = [int(x)for x in string.split(" ")]
#string.endswith("0")
#print(sum(numbers))

sequence = int(input("Please input the code of life: "))
teller = 0
som = 0
while sequence != 0:
    if teller % 2 == 0:
        som = som + sequence
        teller = teller + 1
    else:
        som = som - sequence
        teller = teller + 1

    sequence = int(input("Add to the awesomeness of that 1 number: "))
print(som)
