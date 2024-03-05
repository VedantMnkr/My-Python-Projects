import pandas

nato_csv = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_characters = {series[0] : series[1] for _, series in nato_csv.iterrows()}

print('''
  _   _       _______ ____                            
 | \ | |   /\|__   __/ __ \                           
 |  \| |  /  \  | | | |  | |                          
 | . ` | / /\ \ | | | |  | |                          
 | |\  |/ ____ \| | | |__| |                          
 |_|_\_/_/ _  \_|_|  \____/       _   _               
   |  __ \| |                    | | (_)              
   | |__) | |__   ___  _ __   ___| |_ _  ___          
   |  ___/| '_ \ / _ \| '_ \ / _ | __| |/ __|         
   | |    | | | | (_) | | | |  __| |_| | (__          
   |_|    |_| |_|\___/|_| |_|\___|\__|_|\___| _       
         /\   | |     | |         | |        | |      
        /  \  | |_ __ | |__   __ _| |__   ___| |_ ___ 
       / /\ \ | | '_ \| '_ \ / _` | '_ \ / _ | __/ __|
      / ____ \| | |_) | | | | (_| | |_) |  __| |_\__ \
     /_/    \_|_| .__/|_| |_|\__,_|_.__/ \___|\__|___/
                | |                                   
                |_|                                   
      
''')

word = input("Enter the word for it's corresponding NATO Alphabet calls\nword : ")

res = [nato_characters[char.upper()] for char in word if char.upper() in nato_characters]

print(f"The NATO alphabets for the word {word} are\n--> {res}")
