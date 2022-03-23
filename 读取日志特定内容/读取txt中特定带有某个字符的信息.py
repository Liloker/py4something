filename = 'HC.log'

with open(filename) as file_object:
    lines = file_object.readlines()

target_string = ' alt'
log_string = ''
tim = 15
flag = 0
for line in lines:
    #log_string += line.strip()
    #print(log_string)
    #print (line.rstrip())
    if target_string in line:
        flag = 1
    if flag == 1 and tim != 0:
        print(line.rstrip())
        tim -= 1


#if target_string in log_string:
 #   print(log_string[:500]+"...")