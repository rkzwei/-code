alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def cipher (text, shifts):
  if direction == "encode":
    message = list(text)
    encrypted = list.copy(alphabet)
    final = ""
    for char in message:
        shoft = (encrypted.index(char))
        encryption = (encrypted[shoft+shift])
        final += encryption
    print (final)

cipher(text=text,shifts=shift)
