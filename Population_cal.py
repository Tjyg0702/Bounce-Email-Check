# -*- coding: utf-8 -*-
import copy
file = open('Population_list.txt', 'r')
people = 329500000
population=[]
state=[]
for line in file.readlines():
    temp = line.split('\t')
    population.append(round((float(temp[2].replace('\n', '').replace(',',''))/people)*100,3))
    state.append(temp[1])
file.close()
#print(population)



CA_0 = {}
CA_1 = {}

for i in state:
    CA_0[i] = 0
    CA_1[i] = 1

result_CA = []
file1 = open('FEDEX_CA.txt','r')
for line in file1.readlines():
    temp1 = line.split('\t')
    temp = temp1
    temp[-1] = temp1[-1].replace('\n', '')
    if(temp[0] == '0'): 
        CA = copy.deepcopy(CA_0)
        i = 1
        while i < len(temp):
            CA[temp[i]] = temp[i+1]
            i += 2
        result_CA.append(CA)
    elif(temp[0] == '1'):
        CA = copy.deepcopy(CA_1)
        i = 1
        while i < len(temp):
            CA[temp[i]] = temp[i+1]
            i += 2
        result_CA.append(CA)
    else:
        result_CA.append(CA_1)
        
file.close()
#print(result_CA)
file1 = open('UPS_CA.txt','r')
index = 0
for line in file1.readlines():
    temp1 = line.split('\t')
    temp = temp1
    temp[-1] = temp1[-1].replace('\n', '')
    if(temp[0] == '0'): 
        CA = copy.deepcopy(CA_0)
        i = 1
        while i < len(temp):
            CA[temp[i]] = temp[i+1]
            i += 2
        #print(
        for j in CA.keys():
            if(float(result_CA[index][j]) < float(CA[j])):
                result_CA[index][j] = CA[j]
    elif(temp[0] == '1'):
        CA = copy.deepcopy(CA_1)
        i = 1
        while i < len(temp):
            CA[temp[i]] = temp[i+1]
            i += 2
        j = 0
        for j in CA.keys():
            if(float(result_CA[index][j]) < float(CA[j])):
                result_CA[index][j] = CA[j] 
    else:
        CA = copy.deepcopy(CA_1)
        result_CA[index] = copy.deepcopy(CA)
    index += 1
file.close()
#print(result_CA)


result_NJ = []
file1 = open('FEDEX_NJ.txt','r')
for line in file1.readlines():
    temp1 = line.split('\t')
    temp = temp1
    temp[-1] = temp1[-1].replace('\n', '')
    if(temp[0] == '0'): 
        CA = copy.deepcopy(CA_0)
        i = 1
        while i < len(temp):
            CA[temp[i]] = temp[i+1]
            i += 2
        result_NJ.append(CA)
    elif(temp[0] == '1'):
        CA = copy.deepcopy(CA_1)
        i = 1
        while i < len(temp):
            CA[temp[i]] = temp[i+1]
            i += 2
        result_NJ.append(CA)
    else:
        result_NJ.append(CA_1)
        
file.close()
#print(result_CA)
file1 = open('UPS_NJ.txt','r')
index = 0
for line in file1.readlines():
    temp1 = line.split('\t')
    temp = temp1
    temp[-1] = temp1[-1].replace('\n', '')
    if(temp[0] == '0'): 
        CA = copy.deepcopy(CA_0)
        i = 1
        while i < len(temp):
            CA[temp[i]] = temp[i+1]
            i += 2
        #print(
        for j in CA.keys():
            if(float(result_NJ[index][j]) < float(CA[j])):
                result_NJ[index][j] = CA[j]
    elif(temp[0] == '1'):
        CA = copy.deepcopy(CA_1)
        i = 1
        while i < len(temp):
            CA[temp[i]] = temp[i+1]
            i += 2
        j = 0
        for j in CA.keys():
            if(float(result_NJ[index][j]) < float(CA[j])):
                result_NJ[index][j] = CA[j] 
    else:
        CA = copy.deepcopy(CA_1)
        result_NJ[index] = copy.deepcopy(CA)
    index += 1
file.close()

length = min(len(result_CA), len(result_NJ))
result_ary = []
for i in range(length):
    result_dic = {}
    for j in result_CA[i].keys():
        if(float(result_NJ[i][j]) < float(result_CA[i][j])):
            result_dic[j] = result_CA[i][j]
        else:
            result_dic[j] = result_NJ[i][j]
    result_ary.append(result_dic)

print("CA only:\n")
final_result=''
n = 0
for i in result_CA:
    n += 1
    day_result = 0.0
    for j in i.keys():
        if(j == 'PR'): continue
        index = state.index(j)
        day_result += float(population[index]) * float(i[j])
    final_result += 'Day ' + str(n) + ': ' + str(day_result) + '\n'
print(final_result)

print("NJ only:\n")
final_result=''
n = 0
for i in result_NJ:
    n += 1
    day_result = 0.0
    for j in i.keys():
        if(j == 'PR'): continue
        index = state.index(j)
        day_result += float(population[index]) * float(i[j])
    final_result += 'Day ' + str(n) + ': ' + str(day_result) + '\n'
print(final_result)

print("Combined:\n")
final_result=''
n = 0
for i in result_ary:
    n += 1
    day_result = 0.0
    for j in i.keys():
        if(j == 'PR'): continue
        index = state.index(j)
        day_result += float(population[index]) * float(i[j])
    final_result += 'Day ' + str(n) + ': ' + str(day_result) + '\n'
print(final_result)
