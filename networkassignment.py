import matplotlib.pyplot as plt
print("Noiseless Channel")
Ulists1=list()
Blists1=list()
tplists1=list()
Ulists2=list()
Blists2=list()
tplists2=list()
wlists2=list()
Ulists3=list()
Blists3=list()
tplists3=list()
wlists3=list()
while True:
    print("Enter 1 for Analyzing Stop and Wait Protocol")
    print("Enter 2 for Analyzing GoBack-N Protocol")
    print("Enter 3 for Analyzing Selective Repeat Protocol")
    print("Enter 4 to exit")
    choice=int(input("Enter your Choice"))
    if choice==1:
        print("Stop and Wait Protocol")
        print("Enter 1 to analyse based on bandwidth")
        print("Enter 2 to analyse based on Delay")
        ch=int(input())
        if ch==1:
            tp=float(input("Enter the Processing Delay"))
            L=float(input("Enter the no of bits to be transmitted"))
            k=5
            while k>0:
                R=float(input("Enter the Bandwidth"))
                U=1/(1+2*((tp*R)/L))
                U=U*R
                Ulists1.append(U)
                Blists1.append(R)
                k=k-1
            plt.scatter(Blists1,Ulists1,color="blue")
            plt.plot(Blists1,Ulists1)
            plt.xlabel("Bandwidth in Mbps")
            plt.ylabel("Throughput")
            plt.show()

        elif ch==2:
            R=float(input("Enter the Bandwidth"))
            L=float(input("Enter the no of bits to be transmitted"))
            k=5
            while k>0:
                tp=float(input("Enter the Processing Delay"))
                U=1/(1+2*((tp*R)/L))
                U=U*R
                Ulists1.append(U)
                tplists1.append(tp)
                k=k-1
            plt.scatter(tplists1,Ulists1,color="blue")
            plt.plot(tplists1,Ulists1)
            plt.xlabel("Delay in μs")
            plt.ylabel("Throughput")
            plt.show()

        

    elif choice==2:
        print("GoBack-N Protocol")
        print("Enter 1 to analyse based on bandwidth")
        print("Enter 2 to analyse based on Delay")
        print("Enter 3 to analyse based on Windows Size")
        ch=int(input("Enter your choice"))
        if ch==1:
            W=int(input("Enter the Window Size"))
            tp=float(input("Enter the Processing Delay"))
            L=int(input("Enter the no of bits to be transmitted"))
            k=5
            while k>0:
                R=float(input("Enter the Bandwidth"))
                if W>=((2*((tp*R)/L))+1) :
                    U=1/(1+(2*((tp*R)/L)))
                    U=U*R
                else:
                    U=(W*(1))/((2*((tp*R)/L))+1)
                    U=U*R
                Ulists2.append(U)
                Blists2.append(R)
                k=k-1
            plt.scatter(Blists2,Ulists2,color="green")
            plt.plot(Blists2,Ulists2)
            plt.xlabel("Bandwidth in Mbps")
            plt.ylabel("Throughput")
            plt.show()

        elif ch==2:
            W=int(input("Enter the Window Size"))
            R=float(input("Enter the Bandwidth"))
            L=float(input("Enter the no of bits to be transmitted"))
            k=5
            while k>0:
                tp=float(input("Enter the Processing Delay"))
                if W>=((2*((tp*R)/L))+1) :
                    U=1/(1+(2*((tp*R)/L)))
                    U=U*R
                else:
                    U=(W*(1))/((2*((tp*R)/L))+1)
                    U=U*R
                Ulists2.append(U)
                tplists2.append(tp)
                k=k-1
            plt.scatter(tplists2,Ulists2,color="green")
            plt.plot(tplists2,Ulists2)
            plt.xlabel("Delay in μs")
            plt.ylabel("Throughput")
            plt.show()

        
        elif ch==3:
            R=float(input("Enter the Bandwidth"))
            tp=float(input("Enter the Processing Delay"))
            L=float(input("Enter the no of bits to be transmitted"))
            k=5
            while k>0:
                W=int(input("Enter the Window Size"))
                if W>=((2*((tp*R)/L))+1) :
                    U=1/(1+(2*((tp*R)/L)))
                    U=U*R
                else:
                    U=(W*(1))/((2*((tp*R)/L))+1)
                    U=U*R
                Ulists2.append(U)
                wlists2.append(W)
                k=k-1
            plt.scatter(wlists2,Ulists2,color="green")
            plt.plot(wlists2,Ulists2)
            plt.xlabel("Window Size")
            plt.ylabel("Throughput")
            plt.show()

    elif choice==3:
            print("Selective Repeat Protocol")
            print("Enter 1 to analyse based on bandwidth")
            print("Enter 2 to analyse based on Delay")
            print("Enter 3 to analyse based on Windows Size")
            ch=int(input("Enter your choice"))
            if ch==1:
                W=int(input("Enter the Window Size"))
                tp=float(input("Enter the Processing Delay"))
                L=float(input("Enter the no of bits to be transmitted"))
                k=5
                while k>0:
                    R=float(input("Enter the Bandwidth"))
                    if W>=((2*((tp*R)/L))+1) :
                        U=1
                        U=U*R
                    else:
                        U=(W*(1))/((2*((tp*R)/L))+1)
                        U=U*R
                    Ulists3.append(U)
                    Blists3.append(R)
                    k=k-1
                plt.scatter(Blists3,Ulists3,color="red")
                plt.plot(Blists3,Ulists3)
                plt.xlabel("Bandwidth in Mbps")
                plt.ylabel("Throughput")
                plt.show()

            elif ch==2:
                W=int(input("Enter the Window Size"))
                R=float(input("Enter the Bandwidth"))
                L=float(input("Enter the no of bits to be transmitted"))
                k=5
                while k>0:
                    tp=float(input("Enter the Processing Delay"))
                    if W>=((2*((tp*R)/L))+1) :
                        U=1
                        U=U*R
                    else:
                        U=(W*(1))/((2*((tp*R)/L))+1)
                        U=U*R
                    Ulists3.append(U)
                    tplists3.append(tp)
                    k=k-1
                plt.scatter(tplists3,Ulists3,color="red")
                plt.plot(tplists3,Ulists3)
                plt.xlabel("Delay in μs")
                plt.ylabel("Throughput")
                plt.show()
                    
            elif ch==3:
                R=float(input("Enter the Bandwidth"))
                tp=float(input("Enter the Processing Delay"))
                L=float(input("Enter the no of bits to be transmitted"))
                k=5
                while k>0:
                    W=int(input("Enter the Window Size"))
                    if W>=((2*((tp*R)/L))+1) :
                        U=1
                        U=U*R
                    else:
                        U=(W*(1))/((2*((tp*R)/L))+1)
                        U=U*R
                    Ulists3.append(U)
                    wlists3.append(W)
                    k=k-1
                plt.scatter(wlists3,Ulists3,color="red")
                plt.plot(wlists3,Ulists3)
                plt.xlabel("Window Size")
                plt.ylabel("Throughput")
                plt.show()

            else:
                print("Invalid Input")

    elif choice==4:
        break

    else:
        print("Invalid Input")


plt.scatter(Blists1,Ulists1,color="blue")
#plt.scatter(Blists2,Ulists2,color="red")
plt.scatter(Blists3,Ulists3,color="green")
plt.plot(Blists1,Ulists1)
#plt.plot(Blists2,Ulists2)
plt.plot(Blists3,Ulists3)
plt.xlabel("Bandwidth in Mbps")
plt.ylabel("Utilization")
plt.show()
