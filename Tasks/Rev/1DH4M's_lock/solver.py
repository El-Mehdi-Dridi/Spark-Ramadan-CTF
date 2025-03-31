import itertools

def check_length(pin):
    return len(pin) == 4

def check_numeric(pin):
    return pin.isdigit()

def check_distinct_digits(pin):
    return len(set(pin)) == len(pin)

def check_even(pin):
    return int(pin) % 2 == 0

def check_modulo_3(pin):
    return int(pin) % 3 == 0

def check_modulo_7(pin):
    return int(pin) % 7 == 0

def check_first_greater_than_last(pin):
    return pin[0] > pin[-1]

def check_second_and_last_even(pin):
    return int(pin[1]) % 2 == 0 and int(pin[-1]) % 2 == 0

def check_second_and_fourth_digit_power_of_2(pin):
    return pin[1] in ('1', '2', '4', '8') and pin[3] in ('1', '2', '4', '8') 

def check_first_and_third_digit_not_even(pin):
    return pin[0] in ('1', '3', '5', '7', '9') and pin[2] in ('1', '3', '5', '7', '9')  

def check_sum_condition(pin):
    return (int(pin[0]) + int(pin[-1])) < (int(pin[1]) + int(pin[2]))  

def guess_pin():
    valid_pins = []

    
    for pin_tuple in itertools.product('0123456789', repeat=4):
        pin = ''.join(pin_tuple)

        if (check_length(pin) and
            check_numeric(pin) and
            check_distinct_digits(pin) and
            check_sum_condition(pin) and
            check_even(pin) and
            check_modulo_3(pin) and
            check_modulo_7(pin) and
            check_first_greater_than_last(pin) and
            check_second_and_last_even(pin) and
            check_second_and_fourth_digit_power_of_2(pin) and
            check_first_and_third_digit_not_even(pin)): 
            valid_pins.append(pin)

    
    if valid_pins:
        print("Valid PINs found:")
        for pin in valid_pins:
            print(pin)
    else:
        print("No valid PIN found.")

guess_pin()
