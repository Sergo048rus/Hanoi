

def FrameStewart(ndisks,npegs):
    if ndisks ==0: #zero disks require zero moves
        return 0
    if  ndisks == 1 and npegs > 1: #if there is only 1 disk it will only take one move
        return 1
    if npegs == 3:#3 pegs is well defined optimal solution of 2^n-1
        return 2**ndisks - 1
    if npegs >= 3 and ndisks > 0:
        potential_solutions = (2*FrameStewart(kdisks,npegs) + FrameStewart(ndisks-kdisks,npegs-1) for kdisks in range(1,ndisks))
        return min(potential_solutions) #the best solution
    #all other cases where there is no solution (namely one peg, or 2 pegs and more than 1 disk)
    return str("impossible") 

a = int(input("Disks [>] "))
b = int(input("rods [>] "))
print(FrameStewart(a, b)) 