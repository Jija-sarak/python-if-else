# Accept any city from the user and display the monument of that city.
#                   City                                 Monument
#                   Delhi                               Red Fort
#                   Agra                                Taj Mahal
#                   Jaipur                              Jal Mahal
city = input("enter city name:")
if city=="Delhi":
    print("Monument - Red Fort")
elif city=="Agra":
    print("Monument - Taj Mahal")
elif city=="Jaipur":
    print("Monument - Jal Mahal")
else:
    print("don't know , sorry")