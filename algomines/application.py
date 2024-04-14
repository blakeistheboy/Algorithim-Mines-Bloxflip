import bloxflip
import random
import pyperclip
from time import sleep
from customtkinter import *



def predict():

    grid = ['❔', '❔', '❔', '❔', '❔', '❔', '❔', '❔', '❔', '❔', '❔', '❔', '❔', '❔', '❔', '❔', '❔', '❔', '❔', '❔', '❔',
            '❔', '❔', '❔', '❔']
    algo1 = [0, 6, 9, 10, 8, 15]
    algo2 = [6, 9, 2, 18, 20, 23]
    algo3 = [15, 20, 7, 11, 13, 3]
    algo4 = [7, 9, 10, 11, 16, 20]
    algo5 = [5, 19, 12, 15, 8, 24]
    algo6 = [4, 19, 20, 6, 9, 10]
    algo7 = [7, 19, 20, 24, 13, 2]

    algos = [algo1, algo2, algo3, algo4, algo5, algo6, algo7]
    algo_choice = random.choice(algos)

    for index in algo_choice:
        grid[index] = '☑️'


    label.configure(text=grid[0] + " " + grid[1] + " " + grid[2] + " " + grid[3] + " " + grid[4] + "\n" + grid[5] + " " + grid[6] + " " + grid[7] + " " + grid[8] + " " + grid[9] + "\n" + grid[10] + " " + grid[11] + " " + grid[12] + " " + grid[13] + " " + grid[14] + "\n" + grid[15] + " " + grid[16] + " " + grid[17] + " " + grid[18] + " " + grid[19] + "\n" + grid[20] + " " + grid[21] + " " + grid[22] + " " + grid[23] + " " + grid[24]
    )

def account_balance():
 #variables
 grr = auth_E.get()
 if grr:
    if bloxflip.Authorization.validate(auth_E.get()):

        balance = bloxflip.Currency.balance(auth=auth_E.get())
        affiliate = bloxflip.Currency.affiliate(auth=auth_E.get())
        b_label.configure(text=f'balance: {balance}R$')
        a_label.configure(text=f'affiliate: {affiliate}R$')
    else:
       print("auth token is invalid")
 else:
    print("please input an auth token in the 'auth' tab")


def light_mode():
    F = False
    if checkbox.get() == True:
        F = True
        print('enabled light mode')
        set_appearance_mode('light')
    else:
        F = False
        print('disabled light mode')
        set_appearance_mode('dark')


def discord():
   pyperclip.copy("https://discord.gg/GjRt2YtJkV")
   print("copied to clipboard")








print("Initilizing Program")
sleep(.5)




app = CTk()
app.geometry("800x800")
app.title("Algo Mines | https://discord.gg/GjRt2YtJkV")
app.iconbitmap('LOGO.ico')
set_appearance_mode("dark")

tabview = CTkTabview(app, width=750, height=650, segmented_button_selected_color='#2D0D5C', segmented_button_unselected_color='#7618FF', segmented_button_unselected_hover_color='#390F76')
tabview.pack(padx=20, pady=20, expand=True)

#tabs/borders
t1 = tabview.add("Predict")
t1.configure(border_color='#6000EE', border_width=2)


t2 = tabview.add("Currency")
t2.configure(border_color='#6000EE', border_width=2)

t3 = tabview.add("Auth")
t3.configure(border_color='#6000EE', border_width=2)

t4 = tabview.add("Misc")
t4.configure(border_color='#6000EE', border_width=2)

#predict tab
label = CTkLabel(tabview.tab('Predict'), text='No Prediction Loaded...', font=CTkFont('Times New Roman', 50), width=0, height=30)
label.pack(anchor='center', pady=10)

button = CTkButton(tabview.tab('Predict'), text='Predict An Algoritim', corner_radius=50, command=predict)
button.pack(anchor='center', pady=10)

#auth tab
auth_E = CTkEntry(tabview.tab('Auth'), 160, 25, placeholder_text='auth token')
auth_E.pack(anchor='s', pady=10)

auth_B = CTkButton(tabview.tab('Auth'), 50, 20, text='Link Auth', command=account_balance)
auth_B.pack(anchor='s', pady=10)

#currency tab
b_label = CTkLabel(tabview.tab('Currency'), text='No Balance found, link account to find balance.', font=CTkFont('Times New Roman', 20))
b_label.pack(anchor='s', pady=10)

a_label = CTkLabel(tabview.tab('Currency'), text='No Affiliate value found, link account to find affiliate value.', font=CTkFont('Times New Roman', 20))
a_label.pack(anchor='s', pady=10)

r_button = CTkButton(tabview.tab("Currency"), text='Refresh Data', command=account_balance)
r_button.pack(anchor='s', pady=10)

#misc tab
checkbox = CTkCheckBox(tabview.tab('Misc'), text='light mode', command=light_mode)
checkbox.pack(anchor='s', pady=10)

discord_button = CTkButton(tabview.tab('Misc'), text='Discord', width=56, height=25, corner_radius=30, command=discord)
discord_button.pack(anchor='s', pady=10)

app.mainloop()