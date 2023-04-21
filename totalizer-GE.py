import random

MAX_LINES = 3
MAX_BET = 100000
MIN_BET = 1

ROWS = 3
COLS = 3


symbol_count= {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
    "₾": 15
}
symbol_value= {
    "A": 50,
    "B": 40,
    "C": 25,
    "D": 15,
    "₾": 100
}

def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings,winning_lines
            

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" |")
            else: print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("რამდენის ჩარიცხვა გსურთ? ₾")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("თანხა უნდა იყოს 0-ზე მეტი.")
        else: 
            print("გთხოვთ შეიყვანეთ ციფრი.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("შეიყვანეთ ხაზების რაოდენობა ფსონის დასადებად (1-"+str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("შეიყვანეთ სტრიქონის სწორი რაოდენობა.")
        else: 
            print("გთხოვთ შეიყვანეთ ციფრი.")
    return lines

def get_bet():
    while True:
        amount = input("რა ფსონის დადება გსურთ თითოეულ ხაზზე? ₾")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"თანხის მაქსიმუმი და მინიმუმი უნდა შეადგენდეს ₾{MIN_BET} - ₾{MAX_BET}.")
        else: 
            print("გთხოვთ შეიყვანეთ ციფრი.")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True: 
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"თქვენ არ გაქვთ საკმარისი ფსონი ამ თანხის დასადებად, თქვენი მიმდინარე ბალანსი არის ₾{balance}")
        else: 
            break
    print(f"თქვენ ფსონს დებთ ₾{bet}  {lines} ხაზებზე. Total bet is equal to: ₾{total_bet}")

    slots =get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines = check_winnings(slots, lines,bet,symbol_value)
    print(f"თქვენ მოიგეთ ${winnings}.")
    print(f"თქვენ მოიგეთ ხაზებზე: ", * winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True: 
        print(f"თქვენი ბალანსი არის ${balance}")
        answer= input("ჩასართავად დააჭირეთ ენთერს.(q გასასვლელად)")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"თამაშის დასრულების შემდეგ თქვენი ბალანსი შეადგენს ${balance}")
main()