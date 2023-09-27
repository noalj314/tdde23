def sum_all_numbers(the_list):
    if not the_list:
        return 0
    elif type(the_list[0]) == int:
        the_first_sum = the_list[0]
        rest_of_sum = sum_all_numbers(the_list[1:])
        return the_first_sum + rest_of_sum
    elif isinstance(the_list[0], str):
        return sum_all_numbers(the_list[1:])
    elif isinstance(the_list[0], list):
        the_first_sum = sum_all_numbers(the_list[0])
        rest_of_sum = sum_all_numbers(the_list[1:])
        return the_first_sum + rest_of_sum

def exists(bokstav, lista):
    if not lista:
        return False
    elif isinstance(lista[0], str):
        hej = lista[0]
        if bokstav == hej:
            return True
        else:
            return exists(bokstav, lista[1:])
    elif isinstance(lista[0], list):
        if exists(bokstav, lista[0]):
            return True
    return exists(bokstav, lista[1:])

"""
ETT LOGISKT UTTRYCK KAN VARA ENDAST ETT AV DE FÖLJANDE (OCH INGET ANNAT)
- en av de logiska konstanterna "true" eller "false" (som alltså ska vara dessa strängar, inte Python-värdena True och False)
- en propositionssymbol inom citattecken, t ex "p", "q", "cat_gone"
- ett uttryck på formen ["NOT", <logiskt uttryck>]
- ett uttryck på formen [<logiskt uttryck 1>, "OR", <logiskt uttryck 2>]
- ett uttryck på formen [<logiskt uttryck 1>, "AND", <logiskt uttryck 2>]'

"""

def interpret(uttrycken, tolkning):
    """ Översätter ett uttryck till antingen true eller false m.h.a. tolkningen """
    #Fall 1 uttrycket är 'true' eller 'false'
    if uttrycken == 'true' or uttrycken == 'false':
        return uttrycken

    #Fall2 uttrycket är typ cat_gone
    if isinstance(uttrycken,str):
        return tolkning.get(uttrycken)

    #Fall 3 är ["NOT", logiskt uttryck]
    if isinstance(uttrycken, list) and uttrycken[0] == "NOT" and len(range(uttrycken)) <= 2:
        """Fixa inflör inlämning att t.ex. ["NOT", "AND", "Cat_gone"]"""
        hoger_uttryck = interpret(uttrycken[1], tolkning)
        if hoger_uttryck == 'true':
            return 'false'
        else:
            return 'true'

    #Fall4 [logisktuttryck "OR" logiskt uttryck]
    if isinstance(uttrycken,list) and uttrycken[1] == "OR":
        hoger_uttryck = interpret(uttrycken[2], tolkning)
        vanster_uttryck = interpret(uttrycken[0], tolkning)
        if hoger_uttryck == 'true' or vanster_uttryck == 'true':
            return 'true'
        else:
            return 'false'

    # Fall4 [logisktuttryck "AND" logiskt uttryck]
    if isinstance(uttrycken, list) and uttrycken[1] == "AND":
        hoger_uttryck = interpret(uttrycken[2], tolkning)
        vanster_uttryck = interpret(uttrycken[0], tolkning)
        if hoger_uttryck == 'true' and vanster_uttryck == 'true':
            return 'true'
        else:
            return 'false'




