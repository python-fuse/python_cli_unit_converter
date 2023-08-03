# Unit Converter: Build a script that converts units between various systems (e.g., length, weight, temperature).


#functions to convert the input

#Converting m to km
def m_to_km(metre):
    return metre/1000

#Converting m to yard
def m_to_yard(metre):
    return metre*1.09361

#Converting m to mile
def m_to_mile(metre):
    return metre * 0.000621

#Converting m to feet
def m_to_foot(metre):
    return metre * 3.28084

#Converting kilograms to pound
def kg_to_pound(kg):
    return kg * 2.205
    
#Converting kilograms to ounce
def kg_to_ounce(kg):
    return kg * 35.274

#Converting celcius to kelvin
def celcius_to_kelvin(c):
     return c + 273

#Converting celcius to farenheit
def celcius_to_farenheit(c):
    return(9/5) * c + 32

#Getting our input
def getInput(string):
    # Making sure te te input is in numbers
    try:
        return float(input(f'Enter value in {string}: '))
    #Incase it is not we print an error and retry
    except (ValueError,TypeError):
        print('Invalid input!')
	print('Please make sure the provided input is in numbers')
        return getInput(string)

        
#Individual conversion screens

# Here we convert our input using above functions and printing all the results
def weight_convert():
    print('Weight Conversion')
    weight_input = getInput('Kg')

    weight_ounce = kg_to_ounce(weight_input)
    weight_pound = kg_to_pound(weight_input)
    print('Conversion result:')
    print(f'Kg:{weight_input} kg\nPound:{weight_pound} pounds\nOunce:{weight_ounce} ounces')
    main()
    

def length_convert():
    print('Length/Distance Conversion')
    metre_input = getInput('Metre')

    length_foot = m_to_foot(metre_input)
    length_mile = m_to_mile(metre_input)
    length_yard = m_to_yard(metre_input)
    length_km = m_to_km(metre_input)
    print('Conversion result:')
    print(f'Metre:{metre_input} m\nKilometre:{length_km} km\nMile:{length_mile} miles\nYard:{length_yard} yards\nfoot:{length_foot} feet')
    main()

def temperature_convert():
    print('Temperature Conversion')
    
    celcius_input = getInput('Celcius')
    
    temp_f = celcius_to_farenheit(celcius_input)
    temp_k = celcius_to_kelvin(celcius_input)
    print('Conversion result:')
    print(f'Celcius:{celcius_input} C\nFarenheit:{temp_f} F\nKelvin:{temp_k} K')
    main()


# main function
# Our program starts here
def main():
    print('Unit Converter')
    # we print all available commands
    print('Commands:')
    print('"1" for weight conversion')
    print('"2" for length/distance conversion')
    print('"3" for temperature conversion')
    print('"4" to quit program')
    choice  = input('Enter a command: ')
    # Each input takes us to a different screen to convert chosen input and the last one exits the program
    if choice == '1':
        weight_convert()
    elif choice == '2':
        length_convert()
    elif choice == '3':
        temperature_convert()
    elif choice == '4':
        print('Hope you liked it')
        print('See you soon')
        quit()
    # Incase the input doesnt match any option above, we print an error and try taking input again
    else:
        print('Invalid command')
	print('You typed a non-existing command')

# Our program Starting point
if __name__ == '__main__':
    # we used a wile loop to make surethe program keeps running until the user decides to quit
    while True:
        main()
