import string 


def conv_msg():
    user = input("enter your message")
    mod_user = user.lower()
    letters = string.ascii_lowercase
    shift_val = int(input("enter shift value"))
    enc_newletter = []
    dec_newletter = []

    
    def encrypt_letter():
        for user_data in mod_user:
            for ascii_letter in letters:
                if user_data == ascii_letter:
                    enc_newletter.append(letters[letters.index(ascii_letter) + shift_val])
        

        print("".join(enc_newletter))     
   
    
    def decrypt_msg():
        for n in enc_newletter:
            for ascii_let in letters:
                if n == ascii_let:
                    dec_newletter.append(letters[letters.index(ascii_let) - shift_val])
                

        print("".join(dec_newletter))

    encrypt_letter()


    ask_user = input("Do you want to decrypt your message, type (Y/N)")
    if ask_user == "Y" or "y":
        decrypt_msg()
    else:
        print("Thank you!!")
        
                
conv_msg()





