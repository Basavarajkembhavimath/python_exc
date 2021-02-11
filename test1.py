def add1(num1=0,num2=0):
    result = (num1*num1 + num2*num2)
    return result

def add1(num1=0,num2=0):
    result = (num1*num2 + num2*num1)
    return result

def get_item(ln):
    ln = ln.replace('Q ', '')
    ln = ln.replace('p ', '')
    ln = ln.strip()
    item = ln.split(' ')
    return item
def get_idx(pg, qry):
    idx = pg.index(qry)
    return idx

Qr = {} 
pages = []
with open("first_test.txt") as file:
    file = file.readlines()

    for q_num, qry in enumerate(file[6:], 1):
        query = get_item(qry)
        temp    = []
        temp2   = []
        temp3   = []
        for p_num, pag in enumerate(file[:6], 1):
            page = get_item(pag)
            pages.append(page)
            if len(query) == 1 :
                if query[0] in page:
                    idx = get_idx(page, query[0])
                    if idx == 0:
                        p = 'p'+str(p_num)
                        temp.append(p)
                    else:
                        p = 'p'+str(p_num)
                        if p not in temp:
                            temp.append(p)

            if len(query) >= 2 :
                if query[0] in page and query[1] in page :
                    p = 'p'+str(p_num)
                    if len(page) == 2:
                        if p not in temp:
                            temp.append(p)
                    else:
                        if p not in temp:
                            temp.append(p)
                        
                if query[0] in page:
                    idx = get_idx(page, query[0])
                    if idx == 0:
                        p = 'p'+str(p_num)
                        if p not in temp:
                            temp.append(p)
                    else:
                        p = 'p'+str(p_num)
                        if p not in temp:
                            temp.append(p)

                if query[1] in page:
                    idx = get_idx(page, query[1])
                    if idx >= 1 :
                        p = 'p'+str(p_num)
                        if p not in temp:
                            temp.append(p)
                    else:
                        p = 'p'+str(p_num)
                        if p not in temp:
                            temp.append(p)

        Qr['Q'+str(q_num)] = temp+temp2+temp3
al = 'a b'
print(Qr)
name = iter(pages)
print(next(name))
print(str((al)))