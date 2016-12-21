import sys
salary = raw_input('Your current salary: ')
salary = int(salary)
products = [
    ['Iphone', 5800],
    ['MacPro', 12000],
    ['NB Shoes', 680],
    ['Cigarate', 48],
    ['MX4', 2500]
]

shopping_list = []
while True:
    for p in products:
        print products.index(p),p[0], p[1]
    choice = raw_input("\033[32;1mPlease to bug\033[0m;").strip()

    if choice == 'quit':
        print "Your have bought below sutff:"
        for i in shopping_list:
            print '\t', i
        sys.exit('Goodbye!')

    if len(choice) == 0: continue
    if not choice.isdigit():continue
    choice = int(choice)

    if choice > len(products):
        print "\033[32;1mFind not\033[0m;"
        continue
    pro = products[choice]

    if salary >= pro[1]:
        salary = salary - pro[1]
        shopping_list.append(pro)
        print "\033[34;1mAdding %s to shopping list \n your have left%s\033[0m;" % (pro[0], salary)
    else:
        print "\033[34;1mThe price %s is %s \n yet your current balance is %s \n so try anothe one \033[0m;" % (pro[1], pro[0], salary,)


