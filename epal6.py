hours=int(input("δωσε μου τις ωρες:"))
minutes=int(input("δωσε μου τα λεπτα:"))
seconds=int(input("δωσε μου τα δευτερολεπτα:"))
sec1=hours*3600
sec2=minutes*60
sec3=sec1+sec2+seconds
print("ο χρονος σε δευετερολεπτα ειναι:",sec3)
