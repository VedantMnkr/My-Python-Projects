print("""Hey, welcome to the American bill calculator. 
      Where we calculate the tip for you so you dont have to : ) """)

amount: int = int(input("Enter the amount to be paid - "))


while True:
    tip_percentage: int = int(input("Enter the precentage you want to tip\nPlease keep it mind that it should be between 10 -100 :)"))
    if tip_percentage >= 10:
        break
    else:
        print("Be a little generous BROKEY . . .")

print(f'The final amount to be paid is {amount + int(amount * (tip_percentage / 100))}')