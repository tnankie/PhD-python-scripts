def block(data,n):
    ntot=len(data[0])
    nnew=ntot/n
    x=zeroes(nnew,dtype=float)
    y=zeroes(nnew,dtype=float)
    for i in range(nnew):
        x[i]=sum(data[0][i*n:(i+1)*n])/float(n)
        y[i]=sum(data[1][i*n:(i+1)*n])/float(n)
    return [x,y][1ex]
def blockerror(data,blocksize=[10,20,40,60,80,100,125]):
    n=len(data[1])
    delt=(data[0][-1]-data[0][0])/float(n-1)
    xout=[]
    yout=[]
    ybars=[]
    for nb in blocksize:
        xyblock=block(data,nb)
        number=len(xyblock[1])
        std=xyblock[1].std()
        stderror =std/sqrt(number-1.)
        xout += [nb*delt]
        yout += [stderror]
        ybars += [stderror/sqrt(2.*(number-1.))]
    return [xout,yout,ybars]
