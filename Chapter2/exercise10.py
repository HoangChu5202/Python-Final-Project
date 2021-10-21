print("*** Ingredient Adjuster ***")

sugarForOne = 1.5/48
butterForOne = 1/48
flourForOne = 2.75/48

def main():
    cookies = float(input("How many cookies do you want? \n"))
    makeCookie(cookies)

def makeCookie(cookies):
    sugar  = sugarForOne  * cookies
    butter = butterForOne * cookies
    flour  = flourForOne  * cookies
    print("This is what you need:")
    print("  -   " + format(sugar, ".2f") + " cups of sugar")
    print("  -   " + format(butter, ".2f") + " cup of butter")
    print("  -   " + format(flour, ".2f") + " cups of flour")

main()