import ast

a = "['4-7','10-20','25-45','95-105','107-135']"
b = "['4-7','10-25','33-55','95-105','107-135']"
res = ast.literal_eval(b)


len_res = len(res)
out_lst = []
i= 0
for l in range(len_res):
 
  if i < 1:
    data = res[i].split('-')[0]
    data1 = res[i].split('-')[-1]
    data2 = res[i+1].split('-')[0]
    data3 = res[i+1].split('-')[-1]
    differ = int(data2) - int(data1)
    if differ < 5:
      new = data + '-'+ data3
      differ1 = int(data3) - int(data)
      if differ1 >= 20:
        out_lst.append(new)
    
    
  elif i >= 1 and i < 3:
    data = res[i+1].split('-')[0]
    data1 = res[i+1].split('-')[-1]
    data2 = res[i+2].split('-')[0]
    data3 = res[i+2].split('-')[-1]
    differ = int(data2) - int(data1)
    differ1 = int(data3) - int(data)
    new = data + '-'+ data3
    if differ < 5:
      new = data + '-'+ data3
      differ1 = int(data3) - int(data)
      if differ1 >= 20:
        out_lst.append(new)
    else:
      diff = int(data1) - int(data)
      if diff >= 20:
        new = data + '-'+ data1
        out_lst.append(new)
  i += 1

  print(differ)
  print(data,data1)
print(out_lst)