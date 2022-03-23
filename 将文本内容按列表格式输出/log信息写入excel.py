filename = 'RNC.log'

with open(filename) as file_project:
    lines = file_project.readlines()

str = 'UtranCell'
Cellname = ''
nodename = ''
RBSname = ''
PSC = ''
CLD = ''
LA = ''
RA = ''
uD = ''
rncld = ''
LDN = ''
for line in lines:
    #print(line.rstrip())
    if str in line:
        Cellname = line[10:17]
        nodename = line[11:16]
        RBSname = line[10:16]
        PSC = line[24:27]
        CLD = line[18:23]
        LA = line[59:63]
        RA = line[76:78]
        uD = line[79:83]
        rncld = '118'
        LDN = '4201-'+rncld+'-'+CLD
        print('Z'+nodename+' '+Cellname+' '+RBSname+' '+PSC+' '+CLD+' '+LA+' '+RA+' '+uD+' '+rncld+' '+LDN)
#print(Cellname)
