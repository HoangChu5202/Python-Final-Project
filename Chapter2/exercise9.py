print("*** Celsius to Fahrenheit Temperature Converter ***")
def main():
    temperature = float(input("Give me a temperature in Celsius: "))
    calF_temperature(temperature)

def calF_temperature(temperature):
    fahrenheit = 9/5 * temperature + 32
    print("F = " + str(int(fahrenheit)))

main()
