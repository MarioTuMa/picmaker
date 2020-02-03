fout = open("pic.ppm","w")

fout.write("P3\n256 256\n255\n")

def gcd(n,k):
    if(k==n or k==0):
        return n
    if(n<k):
        return gcd(k,n)
    else:
        return gcd(k,n%k)

def lcm(n,k):
    if(n==0 or k==0):
        return 0
    return int(n*k/gcd(n,k))

for i in range(256):
    for j in range(256):
        fout.write(str(lcm(i,j)%255)+" "+str(gcd(i,j)%255)+" "+str((i+j)%255)+" ")