# name ='jhon smith'
# age=20
# isNew=True
# print(name, age, isNew)
# name= input('What is your name? ')
# print('Hi ' + name)
# person= input('What is Your name? ')
# person2=input('Your Favourite Color? ')
# print( person + ' Likes ' + person2)

# how to calculate age
# birth_year=input('Birth Year: ')
# age= 2021 - int(birth_year)
# print(age)

# calculate pound to kg
# weight_ibs= input('weight (ibs): ')
# weight_kg =int(weight_ibs) * 0.45
# print(weight_kg)

#course ='python is one of my favourite programimg language so far'
#print(course[-1])
#print(course[0:4]) # 1 THEKE GUNE 4 ta word dibe eivabe kor ajabe : clone means it clone or copy the code
# ## if want to see the nagetive index number then
# it will be give me the last letter of this variable

#exercise
# name ='Jennifer'
# print(name[1:-1])
# country='Bangladesh'
# print(country[2:-2])


# munna= 'I am getting so depress day  to day allah save me '
# # print(len(munna))
# print(munna.upper())
# print(munna.lower())
#
# import pycountry
# from tkinter import Tk, Label, Button, Entry
# from phone_iso3166.country import phone_country
#
#
# class Location_Tracker:
#     def __init__(self, App):
#         self.window = App
#         self.window.title("Phone number Tracker")
#         self.window.geometry("500x400")
#         self.window.configure(bg="#3f5efb")
#         self.window.resizable(False, False)
#
#         # ___________Application menu_____________
#         Label(App, text="+8801313885822", fg="white", font=("Times", 20), bg="#3f5efb").place(x=150, y=30)
#         self.phone_number = Entry(App, width=16, font=("Arial", 15), relief="flat")
#         self.track_button = Button(App, text="Track Country", bg="#22c1c3", relief="sunken")
#         self.country_label = Label(App, fg="white", font=("Times", 20), bg="#3f5efb")
#
#         # ___________Place widgets on the window______
#         self.phone_number.place(x=170, y=120)
#         self.track_button.place(x=200, y=200)
#         self.country_label.place(x=100, y=280)
#
#         # __________Linking button with countries ________
#         self.track_button.bind("<Button-1>", self.Track_location)
#         # 255757294146
#
#     def Track_location(self, event):
#         phone_number = self.phone_number.get()
#         country = "Country is Unknown"
#         if phone_number:
#             tracked = pycountry.countries.get(alpha_2=phone_country(phone_number))
#             print(tracked)
#             if tracked:
#                 if hasattr(tracked, "official_name"):
#                     country = tracked.official_name
#                 else:
#                     country = tracked.name
#         self.country_label.configure(text=country)


# PhoneTracker = Tk()
# MyApp = Location_Tracker(PhoneTracker)
# PhoneTracker.mainloop()
