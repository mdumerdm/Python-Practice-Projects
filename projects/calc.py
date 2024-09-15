print("<<<<<<<<<<<<WELCOME TO SIMPLE CALCULATOR APPLICATION>>>>>>>>>>>>>>>>>>>>>>>>>>")

n1=input("ENTER  A NUMBER:  ")
op1=input("ENTER A OPERATOR:  ")
n2=input("ENTER SECOND NUMBER:   ")
nu1=float(n1)
nu2=float(n2)
if(op1=="+"):
    res=nu1+nu2
    print(res)
elif(op1=="-"):
    res=nu1-nu2
    print(res)
elif(op1=="/"):
    if(nu2!=0):
      res=nu1/nu2
      print(res)
    else:
        print("no zeros")
elif(op1=="*"):
    res=nu1*nu2
    print(res)
