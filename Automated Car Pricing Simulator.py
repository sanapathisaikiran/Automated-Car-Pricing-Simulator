class car_show_room:
    def __init__(self):
        self.cgst = 5555
        self.sgst = 4444
        self.insurance = 6666

    def company(self, name):
        while True:
            name = input("confirm  the company: ").lower()
            if name == "audi":
                print("Welcome to ", name.capitalize(), "company")
                self.f = name
                break
            elif name == "tata":
                self.f = name
                print("Welcome to ", name.capitalize(), "company")
                break
            elif name == "mahendhra":
                self.f = name
                print("Welcome to ", name.capitalize(), "company")
                break
            else:
                print("Try again, choose one of the above companies")

    def model(self, m):
        models = [["ax", "bx"], ["crystal", "inova"], ["thar", "xuv"]]

        if m == "audi":
            print("Select the model in ", m.capitalize(), "company")
            print(models[0])

        elif m == "tata":
            print("Select the model in ", m.capitalize(), "company")
            print(models[1])

        elif m == "mahendhra":
            print("Select the model in ", m.capitalize(), "company")
            print(models[2])

        else:
            print("Sorry, it is not available")

    def price(self, p):
        while True:
            if p == "ax":
                ax = 250000
                print("ax price is ", ax)
                tprice = self.cgst + self.sgst + self.insurance + ax
                print("The on-road price of ax is: ", tprice)
                break

            elif p == "bx":
                bx = 40000000
                print("bx price is ", bx)
                tprice = self.cgst + self.sgst + self.insurance + bx
                print("The on-road price of bx is: ", tprice)
                break

            elif p == "crystal":
                crystal = 5666778
                print("crystal price is ", crystal)
                tprice = self.cgst + self.sgst + self.insurance + crystal
                print("The on-road price of crystal is: ", tprice)
                break

            elif p == "inova":
                inova = 6000000
                print("inova price is ", inova)
                tprice = self.cgst + self.sgst + self.insurance + inova
                print("The on-road price of inova is: ", tprice)
                break

            elif p == "thar":
                thar = 999999
                print("thar price is ", thar)
                tprice = self.cgst + self.sgst + self.insurance + thar
                print("The on-road price of thar is: ", tprice)
                break

            elif p == "xuv":
                xuv = 8899000
                print("xuv price is ", xuv)
                tprice = self.cgst + self.sgst + self.insurance + xuv
                print("The on-road price of xuv is: ", tprice)
                break

            else:
                print("Enter the correct model")
                p = input("Enter model again: ")

# Main Program
companies = ["audi", "tata", "mahendhra"]
print(companies)

# Select company
n = input("Select the company: ").lower()
o = car_show_room()
o.company(n)

# Show available models
o.model(n)

# Select model
p = input("Select the model: ").lower()
o.price(p)
