uw=0
Social_credit=0


while uw<1:
    pytanie1=input("Co to taiwan? \n1.Kraj \n2.co to jest wogóle?: ")

    if pytanie1 in ["Kraj", "1.Kraj", "kraj", "1.kraj", "1", "1."]:
        Social_credit=Social_credit-10
        print(f"\nSocial Credit  {Social_credit}")
        uw=uw+1
        print("---------------------------")

    elif pytanie1 in ["co to jest wogóle?","co to jest wogóle","Co to jest wogóle?", 
"Co to jest wogóle", "2.co to jest wogóle?", "2.Co to jest wogóle?", "2", "2." ]:
        Social_credit=Social_credit+10
        print(f"\nSocial Credit  {Social_credit}")
        uw=uw+1
        print("---------------------------")

    else:
        print("Źle napisałx, spróbuj jeszcze raz.")
        print("---------------------------")


# -------------------------------------
while uw<2:
    pytanie2=input("Co się stało w 1989? \n1.nic \n2.coś: ")
    
    if pytanie2 in ["nic", "Nic", "1", "1.", "1.nic", "1.Nic"]:
        Social_credit=Social_credit+10
        print(f"\nSocial Credit  {Social_credit}")
        uw=uw+1
        print("---------------------------")

    elif pytanie2 in ["coś", "Coś", "2", "2.", "2.coś", "2.Coś" ]:
        Social_credit=Social_credit-10
        print(f"\nSocial Credit  {Social_credit}")
        uw=uw+1
        print("---------------------------")

    else:
        print("Źle napisałx, spróbuj jeszcze raz.")
        print("---------------------------")
# ------------------------------------------------
while uw<3:
    pytanie3=(input("Ile masz dzieci?: "))

    if (pytanie3.isnumeric()):
        if (pytanie3)!="1":
            Social_credit=Social_credit-10
            print(f"\nSocial Credit  {Social_credit}")
            uw=uw+1
            print("---------------------------")
    if (pytanie3.isnumeric())==False:
        print('Napisz numer bez przecinka') 
            
    if pytanie3=="1":
        Social_credit=Social_credit+10
        print(f"\nSocial Credit  {Social_credit}")
        uw=uw+1
        print("---------------------------")

# ------------------------------------------------------
if uw<4:

    import tkinter as tk
    from tkinter import ttk
    from PIL import Image, ImageTk

    class App(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title('Nie śmieszny obrazek ')

            self.image = Image.open('./assets/resizePooh.png')
            self.python_image = ImageTk.PhotoImage(self.image)

            ttk.Label(self, image=self.python_image).pack()

    if __name__ == '__main__':
        app = App()
        app.mainloop()

while uw<4:
    pytanie4=input("Czy to cię śmieszy? \n1.nie \n2.tak: ")
        
    if pytanie4 in ["nie", "Nie", "1", "1.", "1.Nie", "1.nie"]:
        Social_credit=Social_credit+10
        print(f"\nSocial Credit  {Social_credit}")
        uw=uw+1
        print("---------------------------")

    elif pytanie4 in ["Tak", "tak", "2", "2.", "2.Tak", "2.tak"]:
        Social_credit=Social_credit-10
        print(f"\nSocial Credit  {Social_credit}")
        uw=uw+1
        print("---------------------------")

    else:
        print("Źle napisałx, spróbuj jeszcze raz.")
        print("---------------------------")
# -------------------------------------------------
if uw<5:
    import webbrowser
    webbrowser.open('https://www.youtube.com/watch?v=OjNpRbNdR7E')
    print('\033[1m' + f"Suma Social creditów= \033[91m{Social_credit}" + '\033[0m')
    if Social_credit==40:
        print("您已獲得最高社會信用額度，您將獲得更多一碗米飯")

    if Social_credit<40 and Social_credit>=0:
        print("你沒有最高分，但他們仍然是積極的，你得到半碗米飯和工廠二十四小時的額外工作")

    if Social_credit<0:
        print("您的社會信用為負，執行將發生 兩天 ")
    




    