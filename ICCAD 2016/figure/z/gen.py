for i in range(5) :
    for j in range(5) :
        print '{:2d}'.format(i * 5 + j) + "@" + '{:2d}'.format(0),
    print ""

#Lfmap = 5;
#K = 3;
#Nfmap = 8;
#Ngroup = 1;
#
#Nfilter = 8;
#
#for r in range(Lfmap * Lfmap) :
#    for ngroup in range(Ngroup) :
#        for rk in range(K) :
#            for ck in range(K) :
#                rfmap = r / Lfmap + rk - 1;
#                cfmap = r % Lfmap + ck - 1;
#                ndx = rfmap * Lfmap + cfmap;
#                if (rfmap >= Lfmap or rfmap < 0) :
#                    print ' P',
#                elif (cfmap >= Lfmap or cfmap < 0) :
#                    print ' P',
#                else :
#                    print '{:2d}'.format(ndx),
#                    
#
#    print ""
#print ""
#print ""
#print ""
