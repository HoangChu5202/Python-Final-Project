from datetime import date

def get_division():
    result = {}
    with open("divisions.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            result[data[0]] = data[1]
    return result

def get_salepeople_division():
    divisions = get_division()
    result = {}
    with open("employees.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            division = divisions.get(data[0])
            lastname = data[1]
            firstname = data[2]
            key = lastname + ", " + firstname
            result[key] = {}
            result[key]["division"] = division
    return result

def get_sale(dict):
    with open("sale.txt", "r") as file:
        employees_count = 0
        for line in file:
            data = line.strip()
            try:
                sale_item = float(data)
                sales_data.append(sale_item)
            except ValueError:
                if employees_count > 0:
                    dict[sale_person]["sale-data"] = sales_data
                employees_count += 1
                sale_person = data
                sales_data = []
        dict[sale_person]["sale-data"] = sales_data

def get_sales_total_and_average(dict):
    for person in dict:
        total = 0
        for sale in dict[person]["sale-data"]:
            total += sale
        dict[person]["sale-total"] = round(total, 2)
        dict[person]["sale-average"] = round(total / len(dict[person]["sale-data"]), 2)

def print_header(today_date, current_page):
    result = "\n" + today_date + (" " * 55) + "Page: " + str(current_page)
    result += "\n" + (" " * 34) + "SALES REPORT\n"
    result += "\n" + (" " * 23) + "NAME" + (" " * 23) + "|" + (" " * 5) + "TOTAL" + (" " * 5) + "|" + (" " * 5) + "AVERAGE"
    result += "\n" + ("-" * 80)
    return result

def create_blank_file(file_name, today_date, current_page):
    with open(file_name, "w") as file:
        file.write(print_header(today_date,current_page))

def print_division(salepeople_data, file_name, division, line_count, today_date, current_page,):
    with open(file_name, "a") as file:
        division_sale = 0
        file.write("\n** DIVISION: " + division + " **")
        line_count += 1
        for key in salepeople_data:
            if (division == salepeople_data[key]["division"]):
                if line_count >= 49: 
                    current_page += 1
                    file.write(("\n" + print_header(today_date, current_page)))
                    line_count = 5
                file.write("\n" + key)
                file.write(" " * (50 - len(key)))
                salesperson_sales = salepeople_data[key]["sale-total"]
                division_sale += salesperson_sales 
                file.write(f"{salesperson_sales:14,.2f}")
                file.write(" " * 3)
                salesperson_avarage = salepeople_data[key]["sale-average"]
                file.write(f"{salesperson_avarage:13,.2f}")
                line_count += 1
        file.write("\n\n" + ("-" * 80))
        file.write("\n** Division Total - " + division)
        file.write(" " * (50 - len(division) - 20))
        file.write(f"{division_sale:14,.2f}\n\n") 
        line_count += 5 
    return division_sale, line_count, current_page

def print_footer(file_name, total_sales):
    with open(file_name, "a") as file:
        file.write("\n\n" + ("-" * 80) + "\n" + ("-" * 80))
        file.write("\n*** Report Total")
        file.write(" " * (50 - 16)) # Prints spaces to fill column 1
        # file.write("|")
        file.write(f"{total_sales:14,.2f}\n\n\n")

def print_report(salepeople_data):
    today_date = str(date.today())
    current_page = 1
    file_name = today_date + "_SaleReport.txt"
    create_blank_file(file_name, today_date, current_page)
    divisions = get_division()
    total_sales = 0
    line_count = 5
    for key in divisions:
        division_sales, line_count, current_page = print_division(salepeople_data, file_name, divisions[key], line_count, today_date, current_page)
        total_sales += division_sales
    print_footer(file_name, total_sales)


def main():
    salepeople_data = get_salepeople_division()
    get_sale(salepeople_data)
    get_sales_total_and_average(salepeople_data)
    print_report(salepeople_data)
    
main()