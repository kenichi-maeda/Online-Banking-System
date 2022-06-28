import ast
from tkinter import *
from tkinter import messagebox, ttk
from tkcalendar import *

# Main window for sign in page.
window = Tk()
window.title("Sign in")
window.geometry("900x500+300+200")
window.resizable(False, False)
window.config(background="white")


# Function for the sign-in button
def sign_in():
    username = name.get()  # Get username from the input box
    password = pword.get()  # Get password from the input box

    file = open("datasheet.txt", "r")
    data = file.read()
    dic = ast.literal_eval(data)
    file.close()

    # If username and the corresponding password are valid, move onto a new window.
    if username in dic.keys() and password == dic[username]:
        new_window = Toplevel(window)
        new_window.title("Welcome")
        new_window.geometry("900x500+300+200")
        new_window.resizable(False, False)
        new_window.config(background="white")
        new_title = Label(new_window, text="    BANK OF BANK", font=("Microsoft YaHei UI", 14, "bold"), fg="white",
                          bg="#DE2700",
                          width=120, height=2, anchor="w")
        new_title.place(x=0, y=0)
        new_title2 = Label(new_window, text="Online Banking", font=("Microsoft YaHei UI", 14), fg="white",
                           bg="#DE2700",
                           width=20, height=2, anchor="w")
        new_title2.place(x=220, y=0)
        label1 = Label(new_window, text="Hello, " + username, font=("Microsoft YaHei UI", 18), fg="black", bg="white")
        label1.place(x=10, y=100)

        ##############################################
        # Account data
        saving = 1000000
        amount_to_pay = 1000
        invest_amount = 100
        ##############################################

        label2 = Label(new_window, text="Personal accounts                                                      ",
                       font=("Microsoft YaHei UI", 14, "underline"), fg="black",
                       bg="white")
        label2.place(x=10, y=150)

        label3 = Label(new_window, text="Adv SafeBalance Banking - 1234", font=("Microsoft YaHei UI Light", 13),
                       fg="#331140", width=40,
                       height=2, anchor="w",
                       bg="#F9F7F7")
        label3.place(x=10, y=180)

        label4 = Label(new_window, text="$" + str(saving), font=("Microsoft YaHei UI", 13), fg="black", width=10,
                       height=2, anchor="e",
                       bg="#F9F7F7")
        label4.place(x=400, y=180)

        #####################################################
        def make_payment():
            new_window2 = Toplevel(new_window)
            new_window2.title("Make payment")
            new_window2.geometry("500x500")
            new_window2.resizable(False, False)
            new_window2.config(background="white")

            title = Label(new_window2, text="Make Payment                                         ",
                          font=("Microsoft YaHei UI", 17, "underline"), fg="black",
                          bg="white")
            title.place(x=10, y=10)
            sub_title = Label(new_window2, text="Unlimited Cash Rewards Visa Signature - 1234          ",
                              font=("Microsoft YaHei UI Light", 14, "underline"), fg="black",
                              bg="white")
            sub_title.place(x=10, y=42)

            def close():
                new_window2.destroy()

            close_button = Button(new_window2, text="Close", border=0, cursor='hand2',
                                  font=("Microsoft YaHei UI Light", 11, "underline"),
                                  bg="white", fg="blue", command=close)
            close_button.place(x=440, y=0)

            pay_to_label1 = Label(new_window2, text="Pay to", font=("Microsoft YaHei UI", 16), bg="white", fg="black")
            pay_to_label1.place(x=10, y=100)

            pay_to_label2 = Label(new_window2, text="Unlimited Cash Rewards Visa Signature - 1234",
                                  font=("Microsoft YaHei UI Light", 13), bg="white", fg="black")
            pay_to_label2.place(x=140, y=103)

            pay_from_label1 = Label(new_window2, text="Pay From", font=("Microsoft YaHei UI", 16), bg="white",
                                    fg="black")
            pay_from_label1.place(x=10, y=150)

            pay_from_label2 = Label(new_window2, text="Adv SafeBalance Banking - 1234",
                                    font=("Microsoft YaHei UI Light", 13), bg="white", fg="black")
            pay_from_label2.place(x=140, y=153)

            amount_label1 = Label(new_window2, text="Amount", font=("Microsoft YaHei UI", 16), bg="white",
                                  fg="black")
            amount_label1.place(x=10, y=200)

            amount_list = ["$" + str(amount_to_pay)]
            amount_label2 = ttk.Combobox(new_window2, font=("Microsoft YaHei UI Light", 16))
            amount_label2["values"] = amount_list
            amount_label2.place(x=140, y=204)

            deliver_label1 = Label(new_window2, text="Deliver", font=("Microsoft YaHei UI", 16), bg="white",
                                   fg="black")
            deliver_label1.place(x=10, y=250)

            deliver_label2 = Calendar(new_window2, selectmode="day")
            deliver_label2.place(x=140, y=254)

            ############################
            def make_payment_command():
                nonlocal amount_to_pay
                nonlocal saving
                saving -= amount_to_pay
                amount_to_pay = 0
                new_label4 = Label(new_window, text="$" + str(saving), font=("Microsoft YaHei UI", 13), fg="black",
                                   width=10, height=2, anchor="e", bg="#F9F7F7")
                new_label4.place(x=400, y=180)
                new_label6 = Label(new_window, text="$" + str(amount_to_pay), font=("Microsoft YaHei UI", 13),
                                   fg="black", width=10, height=2, anchor="e", bg="#F9F7F7")
                new_label6.place(x=400, y=240)

                new_window2.destroy()

            ############################

            pay_button = Button(new_window2, text="Make Payment", font=("Microsoft YaHei UI", 14), bg="#4096E2",
                                fg="white", command=make_payment_command)
            pay_button.place(x=180, y=430)

        #####################################################

        label5 = Button(new_window, border=0, cursor='hand2', text="Unlimited Cash Rewards Visa Signature - 1234",
                        font=("Microsoft YaHei UI Light", 12),
                        fg="#331140", width=50,
                        height=2, anchor="w",
                        bg="#F9F7F7", command=make_payment)
        label5.place(x=10, y=240)

        label6 = Label(new_window, text="$" + str(amount_to_pay), font=("Microsoft YaHei UI", 13), fg="black", width=10,
                       height=2, anchor="e",
                       bg="#F9F7F7")
        label6.place(x=400, y=240)

        label7 = Label(new_window, text="Investment accounts                                                  ",
                       font=("Microsoft YaHei UI", 14, "underline"), fg="black",
                       bg="white")
        label7.place(x=10, y=310)

        label8 = Label(new_window, text="ABCD Investment", font=("Microsoft YaHei UI", 13),
                       fg="#063970", width=40,
                       height=3, anchor="w",
                       bg="#F9F7F7")
        label8.place(x=10, y=350)

        label9 = Label(new_window, text="$" + str(invest_amount), font=("Microsoft YaHei UI", 13), fg="black", width=10,
                       height=3, anchor="e",
                       bg="#F9F7F7")
        label9.place(x=400, y=350)

        def log_out():
            new_window.destroy()

        log_out_button = Button(new_window, text="Log Out", border=0, cursor='hand2',
                                font=("Microsoft YaHei UI", 12, "bold"),
                                bg="#DE2700", fg="white", command=log_out)
        log_out_button.place(x=800, y=0)

        new_window.mainloop()

    else:
        messagebox.showerror("Invalid", "Wrong username or password")


# Function for creating a sign-up page
def sign_up_command():
    window2 = Toplevel(window)
    window2.title("Sign up")
    window2.geometry("900x500+300+200")
    window2.resizable(False, False)
    window2.config(background="white")

    def shutdown():
        window2.destroy()

    # Function for the sign-up button.
    def sign_up():
        username = name.get()
        password = pword.get()
        confirm_password = p2word.get()

        if password == confirm_password:
            try:
                file = open('datasheet.txt', 'r+')
                data = file.read()
                dic = ast.literal_eval(data)

                new_pair = {username: password}
                dic.update(new_pair)
                file.truncate(0)
                file.close()

                file = open("datasheet.txt", "w+")
                w = file.write(str(dic))

                messagebox.showinfo("Sign up", "Successfully sign up")

            except:
                file = open("datasheet.txt", "w")
                pair = str({'Username': "password"})
                file.write(pair)
                file.close()
        else:
            messagebox.showerror("Invalid", "Password Unmatched")

    # Image for the sign-up page
    photo2 = PhotoImage(file="data/sign up.png")
    image2 = Label(window2, image=photo2, bg="white")
    image2.place(x=4, y=-30)

    # Title for the sign-up page
    title2 = Label(window2, text="Create Account", font=("Microsoft YaHei UI", 25), fg="#7EE382", bg="white")
    title2.place(x=550, y=40)

    l1_2 = Label(window2, text="Username", font=("Microsoft YaHei UI", 13), fg="#555353", bg="white")
    l1_2.place(x=560, y=117)
    name2 = Entry(window2, font=("Microsoft YaHei UI Light", 13), bg="#F9F7F7", fg="black", width=25)
    name2.place(x=560, y=150)

    l2_2 = Label(window2, text="Password", font=("Microsoft YaHei UI", 13), fg="#555353", bg="white")
    l2_2.place(x=560, y=188)
    pword_2 = Entry(window2, font=("Microsoft YaHei UI Light", 13), bg="#F9F7F7", fg="black", width=25)
    pword_2.place(x=560, y=220)

    l3_2 = Label(window2, text="Confirm Password", font=("Microsoft YaHei UI", 13), fg="#555353", bg="white")
    l3_2.place(x=560, y=258)
    p2word = Entry(window2, font=("Microsoft YaHei UI Light", 13), bg="#F9F7F7", fg="black", width=25)
    p2word.place(x=560, y=290)

    sign_up_button = Button(window2, text="Sign up", font=("Microsoft YaHei UI", 15), width=18, height=1, bg="#4096E2",
                            fg="white", command=sign_up)
    sign_up_button.place(x=560, y=335)

    l3_2 = Label(window2, text="Already have an account?", font=("Microsoft YaHei UI Light", 11), fg="black",
                 bg="white")
    l3_2.place(x=560, y=390)
    move_to_the_sign_in_page = Button(window2, text="Sing in here!", border=0, cursor='hand2',
                                      font=("Microsoft YaHei UI Light", 13), bg="white", fg="#4096E2", command=shutdown)
    move_to_the_sign_in_page.place(x=740, y=385)

    window2.mainloop()


# Image for sign in page.
photo1 = PhotoImage(file="data/sign in.png")
image1 = Label(window, image=photo1, bg="white")
image1.place(x=1, y=50)

# title for sign in page.
title1 = Label(window, text="Welcome Back", font=("Microsoft YaHei UI", 25), fg="#4096E2", bg="white")
title1.place(x=550, y=80)

# Input box for entering username
l1 = Label(window, text="Username", font=("Microsoft YaHei UI", 13), fg="#555353", bg="white")
l1.place(x=560, y=157)
name = Entry(window, font=("Microsoft YaHei UI Light", 13), bg="#F9F7F7", fg="black", width=25)
name.place(x=560, y=190)

# Input box for entering password
l2 = Label(window, text="Password", font=("Microsoft YaHei UI", 13), fg="#555353", bg="white")
l2.place(x=560, y=228)
pword = Entry(window, font=("Microsoft YaHei UI Light", 13), bg="#F9F7F7", fg="black", width=25)
pword.place(x=560, y=260)

# Sign in button
button1 = Button(window, text="Sign in", font=("Microsoft YaHei UI", 15), width=18, height=1, bg="#4096E2", fg="white",
                 command=sign_in)
button1.place(x=560, y=300)

# Ask to sign up for those who do not have an account
l3 = Label(window, text="New User?", font=("Microsoft YaHei UI Light", 13), fg="black", bg="white")
l3.place(x=560, y=350)
button2 = Button(window, text="Sing up here!", border=0, cursor='hand2', font=("Microsoft YaHei UI Light", 13),
                 bg="white", fg="#4096E2", command=sign_up_command)
button2.place(x=650, y=347)

window.mainloop()
