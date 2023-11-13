alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = [' ', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', '?', '/', '.', '>', ',', '<', '[', ']', ':', ';']
from art import logo
print(logo)

direction = input("Type \'encode\' to encrypt, type \'decode\' to decrypt \n").lower()
message = input("Type your message: \n").lower()
shift = int(input("Type the shift number \n"))

length = len(message)

def cipher(cipher_direction, start_message, shift_amount):
    global j
    j = 0
    end_message = ""
    shift_amount = shift_amount % 26
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_message += alphabet[new_position]

        else:
            end_message += char

    print(f"Here's the {cipher_direction}d result: {end_message}")


    #for i in range(0,length):
     #   if start_message[i] in symbols:
      #      end_message += start_message[i]
       #     continue

        #else:
         #   for letter in alphabet:
          #      if start_message[i] == letter:
           #         print(i)
            #        print(j)
             #       print(shift_amount)
              #      end_message += alphabet[j + shift_amount]
               #     j = 0
                #else:
                 #   j += 1
    #print(end_message)

cipher(direction, message, shift)

def restart(yes_or_no):
    while yes_or_no == "yes":
      direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
      message = input("Type your message:\n").lower()
      shift = int(input("Type the shift number:\n"))
      cipher(start_message=message, shift_amount=shift, cipher_direction=direction)
      yes_or_no = input("Would you like to restart the cipher program? Type yes or no. \n").lower()

decision = input("2Would you like to restart the cipher program? Type yes or no.\n").lower()

restart(yes_or_no = decision)