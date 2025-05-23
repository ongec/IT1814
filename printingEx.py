a=99
b=88.888888
c= True

print("a=",a,"b=",b,"c=",c)
print("a="+str(a) + "b=" + str(b) + "c="+str(c))
print("Using separator, endline   a=",a,"b=",b,"c=",c,sep="",end=".")
print("going to next line")
print("Using  round               a=",a,"b=",round(b,2),"c=",c)
print("Using formating            a=%d b=%.2f, c=%s" %(a,b,c))
print("Using formating 2          a={} b={}, c={}".format(a,round(b,2),c))
print(f"Using f                   a={a} b={round(b,2)} c={c}")
print(f"Using f2                  a={a} b={b:.2f} c={c}")

