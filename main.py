from tkinter import *
import tkinter.messagebox
import tkinter.messagebox as messagebox

root = Tk()
root.title("Encryption and Decryption Data")
root.geometry("1920x1000+0+0")
#==============================================================================================#
def encrypt_decrypt(text, key):
    encrypted = ''.join(chr(ord(x) ^ key) for x in text)
    return encrypted

def encrypt():
    try:
        key = int(key_entry.get())
        plaintext = plaintext_text.get("1.0", END).strip()
        encrypted = encrypt_decrypt(plaintext, key)
        plaintext_text.delete("1.0", END)
        plaintext_text.insert("1.0", encrypted)
        key_entry.delete(0, END)
    except Exception as e:
        tkinter.messagebox.showerror("Error", str(e))

def decrypt():
    try:
        key = int(key_entry.get())
        plaintext = plaintext_text.get("1.0", END).strip()
        decrypt = encrypt_decrypt(plaintext, key)
        plaintext_text.delete("1.0", END)
        plaintext_text.insert("1.0", decrypt)
        key_entry.delete(0, END)
    except Exception as e:
        tkinter.messagebox.showerror("Error", str(e))

def reset():
    key_entry.delete(0, END)
    plaintext_text.delete("1.0", END)

def iexit():
    result = tkinter.messagebox.askyesno("Exit Confirmation", "Confirm if you want to exit")
    if result:
        root.destroy()


#==============================================================================================#
intro_frame=Frame (root)
intro_frame.pack(pady=20)
intro_label = Label(intro_frame, font=('arial', 24, 'bold'), text="Welcome to the Encryption and Decryption Application!")
intro_label.pack(side=LEFT, padx=10)


button_frame=Frame(root)
button_frame.pack()

Encryption_button = Button(button_frame, font=('arial', 24, 'bold'), width=10, text="Encrypt", command=encrypt)
Encryption_button.pack(side=LEFT, padx=10)

Decryption_button = Button(button_frame, font=('arial', 24, 'bold'), width=10, text="Decrypt", command=decrypt)
Decryption_button.pack(side=LEFT, padx=10)

Rest_button = Button(button_frame, font=('arial', 24, 'bold'), width=10, text="Reset", command=reset)
Rest_button.pack(side=LEFT, padx=10)

Exit_button = Button(button_frame, font=('arial', 24, 'bold'), width=10, text="Exit", command=iexit)
Exit_button.pack(side=LEFT, padx=10)

#==============================================================================================#
# Create the key entry field
key_frame=Frame (root)
key_frame.pack(pady=20)

key_label = Label(key_frame, font=('arial', 24, 'bold'), text="Enter Key:")
key_label.pack(side=LEFT, padx=10)
key_entry = Entry(root, font=('arial', 24, 'bold'), width=12, justify='center', show="*")
key_entry.pack(pady=20)

plain_frame=Frame (root)
plain_frame.pack(pady=20)

plaintext_label = Label(plain_frame, font=('arial', 24, 'bold'), text="Enter Plain Text:")
plaintext_label.pack(pady=20)

plaintext_text = Text(plain_frame, font=('arial',24,'bold'), width=60, height=18)
plaintext_text.pack(pady=20)

root.mainloop()