'''
    while lykkja
        input frá notenda sett inn í lista

        endar while lykkju ef tala er neikvæð

    Kíkja á lista eftir for lykkju og finna stærstu töluna með max fallinu

'''

number_list = []
num_int = 0
while num_int >= 0:
    num_int = int(input("Input a number: "))    # Do not change this line
    # Fill in the missing code
    number_list.append(num_int)

print("The maximum is", max(number_list))    # Do not change this line
