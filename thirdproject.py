import random
org_sent = input()
sent_list = org_sent.split()
sent_list_n = list(map(list,sent_list))
jumble_list_n = []
for i in sent_list_n:
    jumble_list = []
    for j in range(len(i)): 
        temp_letter = random.choice(i)
        i.remove(temp_letter)
        jumble_list.append(temp_letter)
    jumble_list_n.append(jumble_list)
for x in range(len(jumble_list_n)):
    l = random.choice(jumble_list_n)
    print(''.join(l),end = ' ')
    jumble_list_n.remove(l)