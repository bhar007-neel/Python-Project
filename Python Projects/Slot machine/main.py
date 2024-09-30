import random
MAX_LINES = 3
MAX_BET=100
MIN_BET=10

ROWS=3
COLS=3

symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
symbol_value={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}
def check_machine(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line +1)

    return winnings,winning_lines


def get_slotmachine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns= []
    for _ in range(cols):
        column=[]
        current_symbols= all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)    

    return columns    

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!= len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")

        print()        
def deposit():
    while True:
        amount = input("What would you like to deposit $ ")
        if amount.isdigit():
            amount = int (amount)
            if (amount >0):
                break
            else:
                print("Amount is soppose to be greater than Zero")
        else:
            print("Please Enter a NUMBER")
    return amount        

def get_Number_of_lines():
    while True:
        lines = input("how many lines would like to have your bet on (1-"+ str(MAX_LINES)+ ")?") 
        if lines.isdigit():
           lines = int (lines)
           if (1<=lines <= MAX_LINES):
                break
           else:
                print("Enter valid number of lines")
        else:
            print("Please Enter a NUMBER")
                                
    return lines  

def get_bet():
    while True:
        amount = input("What would you like to BET on each line $ ")
        if amount.isdigit():
            amount = int (amount)
            if (MIN_BET<= amount <= MAX_BET):
                break
            else:
                print(f'Amount MUST BE BETWEEN ${MIN_BET} and ${MAX_BET}.')
        else:
            print("Please Enter a NUMBER")
    return amount 



def main():
    balance= deposit()
    lines= get_Number_of_lines()
    while True:
        bet=get_bet()
        total_bet= bet*lines

        if (total_bet > balance):
            print(f'You dont have Enough money to bet on, your total balance is: ${balance}')
        else:
            break    

    
    print(f"You are betting ${bet} on {lines} lines. total bet is equal to: ${total_bet}")
    print(balance,lines,bet)

    slots= get_slotmachine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)

    winnings,winning_lines= check_machine(slots,lines,bet,symbol_value)
    print(f"You won ${winnings}")
    print(f"you won on line",*winning_lines)


main()    