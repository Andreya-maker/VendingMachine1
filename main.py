#PRINT A MENU WITH THE CONTENTS OF YOUR VENDING MACHINE

selection_a = ("Ugg's - $90.00")
selection_b = ("Jordan - $150.00")
selection_c = ("Crocs - $40.00")
selection_d = ("Puma - $70.00")
selection_e = ("Doc Martens - $145.00")
selection_f = ("Finished? CHECKOUT!")

shoes = [selection_a, selection_b, selection_c, selection_d, selection_e]
prices = [90.00, 150.00, 40.00 ,70.00, 145.00]

items = []
finalSel= []

"""
The main_menu variable is using string interperlation to construct our menu using the option variables above. 

This is good pattern because lets say we want to change Midnight Lights to Morning Lights. We only have change option_a string value and these changes will be reflected across our entire program.
"""
main_menu = (f'A: {selection_a}\nB: {selection_b}\nC: {selection_c}\nD: {selection_d}\nE: {selection_e}\nF: {selection_f}')
border = ('~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~')
border2 = ('---------------------------------------------')

print (border)
print('Welcome to the Fast Shoe Selection!<3\n')
print (border2)
print('PLEASE SELECT FROM THE FOLLOWING MENU :')
print (main_menu)
print (border)

user_input = input()
user_input = user_input.upper()

while True:
  if user_input == "A":
    print(f'Selection: {selection_a}')
    items.append(prices[0])
    finalSel.append(shoes[0])

  elif user_input == "B":
    print(f'Selection: {selection_b}')
    items.append(prices[1])
    finalSel.append(shoes[1])
      
  elif user_input == "C":
    print(f'Selection: {selection_c}')
    items.append(prices[2])
    finalSel.append(shoes[2])

  elif user_input == "D":
    print(f'Selection: {selection_d}')
    items.append(prices[3])
    finalSel.append(shoes[3])
      
  elif user_input == "E":
    print(f'Selection: {selection_e}')
    items.append(prices[4])
    finalSel.append(shoes[4])

  elif user_input == "F":    
    print ("Are you sure you want to Checkout, Y/N?")

    user_input = input()
    user_input = user_input.upper()

    if user_input == "Y":
      print ("Your shopping bag:",'\n',('\n'.join(finalSel)))
      print (border2)
      total = float(sum(items))
      print (f'Your total is: ${total:.2f}')
      break
    else:
      user_input == "N"
      print (border2)
      print ("Returning to Main Menu: Please Continue Shopping!")
      print (border2)
      print (main_menu)
  
  else:
    print ("Invalid Entry: Please Try Again")
    print (border2)
    print (main_menu)
    print (border2)  
    user_input = input()
    user_input = user_input.upper()

# Update loop control variable 
  print (border2)
  print (main_menu)
  print (border2)    
  user_input = input()
  user_input = user_input.upper()

order_total = float(sum(items))

print("Please enter your total amount")
payment_input = input()
payment_input = float(payment_input)

while True:
  if payment_input == order_total:
    print ("Change is $0.00\n Thank you for your purchase!\n Don't forget to visit our webiste at www.fastshoes.com")
    break
  elif payment_input > order_total:
    change = payment_input - order_total
    print (f'Your change is ${change:.2f}, Thank you for your purchase')
    break
  else:
    print("Your paymount amount is less than the total\n")
    print("Your entry is not enough. Please enter the total amount")
    payment_input = input()
    payment_input = float(payment_input)

