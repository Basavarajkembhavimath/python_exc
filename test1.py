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
            p_len = len(temp) + len(temp2)
            pages.append(page)
            if len(query) == 1 :
                if query[0] in page:
                    idx = get_idx(page, query[0])
                    if idx == 0:
                        p = 'P'+str(p_num)
                        temp.append(p)
                    else:
                        p = 'P'+str(p_num)
                        if p not in temp2:
                            temp2.append(p)

            if len(query) >= 2 :
                if query[0] in page and query[1] in page :
                    p = 'P'+str(p_num)
                    #print("and",query)
                    if len(page) == 2:
                        temp.append(p)
                        #print("if",page,temp)
                    else:
                        if p not in temp and p not in temp2:
                            temp2.append(p)
                            #print("else",page,temp2)
                        
                if query[0] in page :
                    idx = get_idx(page, query[0])
                    #print("and",query)
                    if idx == 0:
                        p = 'P'+str(p_num)
                        if p not in temp and p not in temp2:
                            temp.append(p)
                            #print("q 0 if",page,temp)
                    else:
                        p = 'P'+str(p_num)
                        if p not in temp and p not in temp2:
                            temp2.append(p)
                            #print("q 0 else",page,temp2)

                if query[1] in page:
                    idx = get_idx(page, query[1])
                    p = 'P'+str(p_num)
                    if idx == 0:
                        if p not in temp and p not in temp2:
                            temp2.append(p)
                            #print("q 1 if",page,temp)
                    else:
                        p = 'P'+str(p_num)
                        if p not in temp and p not in temp2:
                            temp3.append(p)
                            #print("q 1 else",page,temp3)
                    
        p_len = len(temp) + len(temp2)+len(temp3)
        my_list = temp+temp2+temp3
        if p_len <= 5:
            Qr['Q'+str(q_num)] = my_list
        else:
            my_list.pop(-1)
            Qr['Q'+str(q_num)] = my_list
        
for qr, pg in Qr.items():
    print(qr+':',end = ' ')
    for item in pg:
        print(item, end = ' ')
    print('',end='\n')
