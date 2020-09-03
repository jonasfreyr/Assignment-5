'''
    tek in input frá notanda um hversu marga tölur

    geri lista til að halda utan um þrjár seinustu tölur

    prenti út initialized tölurnar til að byrjar með

    geri for lykkju sem keyrir eins oft og inputtið
        plúsa tölurnar í listanum til að fá núverandi tölu
        prenti út töluna

        bæti tölunni við og hendi út fyrst stakinu úr listanum

'''

n = int(input("Enter the length of the sequence: ")) # Do not change this line

num_list = [0, 1 ,2]

# prenta út initialized tölurnar
print(num_list[1])
print(num_list[2])

for a in range(n -2):
    curr_num = sum(num_list)
    print(curr_num)

    num_list.append(curr_num)
    num_list.remove(num_list[0])