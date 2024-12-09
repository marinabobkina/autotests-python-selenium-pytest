def extract_figures(text):
    figures = ""
    for symbol in text:
        if "0" <= symbol <= "9" or symbol == ".":
            figures += symbol
        elif symbol == ",":
            figures += "."
    return float(figures)


def compare_prices_with_selected_level(list_elements):
    for position in range(len(list_elements)):
        checking_element = list_elements[position].text
        cipher = ""
        for symbol in checking_element:
            if "0" <= symbol <= "9":
                cipher += symbol
            elif symbol == "." or symbol == ",":
                break
        if (int(cipher)) <= 135:
            continue
        else:
            print("Цена больше 135 рублей.")
            return False
    return True
