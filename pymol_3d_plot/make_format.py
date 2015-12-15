import numpy as np
f = open('sample/data','r')
c1 = []
c2 = []
c3 = []
prb = []
for line in f:
    c1.append(float(line.split()[0]))
    c2.append(float(line.split()[1]))
    c3.append(float(line.split()[2]))
    prb.append(float(line.split()[3]))
f.close()

##### OUTPUT PC COORDINATES OF ALL STRUCTURES  
fn_out = 'out.pdb'
output = open(fn_out,'w')
ii = 1
for i in range(0,len( c1 ), 50):
    print >> output, "%-6s%5d  %-3s %-4s%c %-5d%10.3f%8.3f%8.3f%6.2f%6.2f%12s" \
            % ("ATOM",ii,"CA","ALA","A",ii,c1[i],c2[i],c3[i],1,prb[i],"C")
    ii = ii + 1
output.close()
