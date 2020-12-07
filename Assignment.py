import matplotlib.pyplot as plt
print("NOISY CHANNEL")
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
        print("Enter 3 to analyse based on Probability")
        ch=int(input())
        if ch==1:
            Ulists=list()
            Blists=list()
            tp=float(input("Enter the Processing Delay"))
            P=float(input("Enter the probability"))
            L=float(input("Enter the no of bits to be transmitted"))
            k=5
            while k>0:
                R=float(input("Enter the Bandwidth"))
                U=(1-P)/(1+2*((tp*R)/L))
                U=U*R
                Ulists.append(U)
                Blists.append(R)
                k=k-1
            plt.scatter(Blists,Ulists,color="blue")
            plt.plot(Blists,Ulists)
            plt.xlabel("Bandwidth in Mbps")
            plt.ylabel("Throughput")
            plt.show()

        elif ch==2:
            Ulists=list()
            tplists=list()
            R=float(input("Enter the Bandwidth"))
            L=float(input("Enter the no of bits to be transmitted"))
            P=float(input("Enter the probability"))
            k=5
            while k>0:
                tp=float(input("Enter the Processing Delay"))
                U=(1-P)/(1+2*((tp*R)/L))
                Ulists.append(U)
                tplists.append(tp)
                k=k-1
            plt.scatter(tplists,Ulists,color="blue")
            plt.plot(tplists,Ulists)
            plt.xlabel("Delay in μs")
            plt.ylabel("Utilization")
            plt.show()

        elif ch==3:
            Ulists=list()
            plists=list()
            R=float(input("Enter the Bandwidth"))
            L=float(input("Enter the no of bits to be transmitted"))
            tp=float(input("Enter the Processing Delay"))
            k=5
            while k>0:
                P=float(input("Enter the probability"))
                U=(1-P)/(1+2*((tp*R)/L))
                U=U*R
                Ulists.append(U)
                plists.append(P)
                k=k-1
            plt.scatter(plists,Ulists,color="blue")
            plt.plot(plists,Ulists)
            plt.xlabel("Probability")
            plt.ylabel("Throughput")
            plt.show()

        else:
            print("Invalid Input")

    elif choice==2:
        print("GoBack-N Protocol")
        print("Enter 1 to analyse based on bandwidth")
        print("Enter 2 to analyse based on Delay")
        print("Enter 3 to analyse based on Probability")
        print("Enter 4 to analyse based on Windows Size")
        ch=int(input("Enter your choice"))
        if ch==1:
            Ulists=list()
            Blists=list()
            W=int(input("Enter the Window Size"))
            tp=float(input("Enter the Processing Delay"))
            P=float(input("Enter the probability"))
            L=int(input("Enter the no of bits to be transmitted"))
            k=5
            while k>0:
                R=float(input("Enter the Bandwidth"))
                if W>=((2*((tp*R)/L))+1) :
                    U=(1-P)/(1+(2*((tp*R)/L)*P))
                    U=U*R
                else:
                    U=(W*(1-P))/((1-P+W*P)((2*((tp*R)/L))+1))
                    U=U*R
                Ulists.append(U)
                Blists.append(R)
                k=k-1
            plt.scatter(Blists,Ulists,color="blue")
            plt.plot(Blists,Ulists)
            plt.xlabel("Bandwidth in Mbps")
            plt.ylabel("Throughput")
            plt.show()

        elif ch==2:
            Ulists=list()
            tplists=list()
            W=int(input("Enter the Window Size"))
            R=float(input("Enter the Bandwidth"))
            P=float(input("Enter the probability"))
            L=float(input("Enter the no of bits to be transmitted"))
            k=5
            while k>0:
                tp=float(input("Enter the Processing Delay"))
                if W>=((2*((tp*R)/L))+1) :
                    U=(1-P)/(1+(2*((tp*R)/L)*P))
                else:
                    U=(W*(1-P))/((1-P+W*P)((2*((tp*R)/L))+1))
                Ulists.append(U)
                tplists.append(tp)
                k=k-1
            plt.scatter(tplists,Ulists,color="red")
            plt.plot(tplists,Ulists)
            plt.xlabel("Delay in μs")
            plt.ylabel("Utilization")
            plt.show()

        elif ch==3:
            Ulists=list()
            plists=list()
            W=int(input("Enter the Window Size"))
            R=float(input("Enter the Bandwidth"))
            P=float(input("Enter the probability"))
            tp=float(input("Enter the Processing Delay"))
            L=float(input("Enter the no of bits to be transmitted"))
            k=5
            while k>0:
                P=float(input("Enter the probability"))
                if W>=((2*((tp*R)/L))+1) :
                    U=(1-P)/(1+(2*((tp*R)/L)*P))
                else:
                    U=(W*(1-P))/((1-P+W*P)((2*((tp*R)/L))+1))
                Ulists.append(U)
                plists.append(P)
                k=k-1
            plt.scatter(plists,Ulists,color="blue")
            plt.plot(plists,Ulists)
            plt.xlabel("Probability")
            plt.ylabel("Utilization")
            plt.show()
        
        elif ch==4:
            Ulists=list()
            wlists=list()
            R=float(input("Enter the Bandwidth"))
            P=float(input("Enter the probability"))
            tp=float(input("Enter the Processing Delay"))
            L=float(input("Enter the no of bits to be transmitted"))
            k=5
            while k>0:
                W=float(input("Enter the window size"))
                if W>=((2*((tp*R)/L))+1) :
                    U=(1-P)/(1+(2*((tp*R)/L)*P))
                else:
                    U=(W*(1-P))/((1-P+W*P)*((2*((tp*R)/L))+1))
                Ulists.append(U)
                wlists.append(W)
                k=k-1
            plt.scatter(wlists,Ulists,color="red")
            plt.plot(wlists,Ulists)
            plt.xlabel("Window Size")
            plt.ylabel("Utilization")
            plt.show()

    elif choice==3:
        print("Selective Repeat Protocol")
        print("Enter 1 to analyse based on bandwidth")
        print("Enter 2 to analyse based on Delay")
        print("Enter 3 to analyse based on Probability")
        print("Enter 4 to analyse based on Windows Size")
        ch=int(input("Enter your choice"))
        if ch==1:
            Ulists=list()
            Blists=list()
            W=int(input("Enter the Window Size"))
            tp=float(input("Enter the Processing Delay"))
            P=float(input("Enter the probability"))
            L=float(input("Enter the no of bits to be transmitted"))
            k=5
            while k>0:
                R=float(input("Enter the Bandwidth"))
                if W>=((2*((tp*R)/L))+1) :
                    U=1-P
                    U=U*R
                else:
                    U=(W*(1-P))/((2*((tp*R)/L))+1)
                    U=U*R
                Ulists.append(U)
                Blists.append(R)
                k=k-1
            plt.scatter(Blists,Ulists,color="blue")
            plt.plot(Blists,Ulists)
            plt.xlabel("Bandwidth in Mbps")
            plt.ylabel("Throughput")
            plt.show()

        elif ch==2:
            Ulists=list()
            tplists=list()
            W=int(input("Enter the Window Size"))
            R=float(input("Enter the Bandwidth"))
            P=float(input("Enter the probability"))
            L=float(input("Enter the no of bits to be transmitted"))
            k=5
            while k>0:
                tp=float(input("Enter the Processing Delay"))
                if W>=((2*((tp*R)/L))+1) :
                    U=1-P
                    U=U*R
                else:
                    U=(W*(1-P))/((2*((tp*R)/L))+1)
                    U=U*R
                Ulists.append(U)
                tplists.append(tp)
                k=k-1
            plt.scatter(tplists,Ulists,color="red")
            plt.plot(tplists,Ulists)
            plt.xlabel("Delay in μs")
            plt.ylabel("Throughput")
            plt.show()

        elif ch==3:
            Ulists=list()
            plists=list()
            W=int(input("Enter the Window Size"))
            R=float(input("Enter the Bandwidth"))
            tp=float(input("Enter the Processing Delay"))
            L=float(input("Enter the no of bits to be transmitted"))
            k=5
            while k>0:
                P=float(input("Enter the probability"))
                if W>=((2*((tp*R)/L))+1) :
                    U=1-P
                    U=U*R
                else:
                    U=(W*(1-P))/((2*((tp*R)/L))+1)
                    U=U*R
                Ulists.append(U)
                plists.append(P)
                k=k-1
            plt.scatter(plists,Ulists,color="blue")
            plt.plot(plists,Ulists)
            plt.xlabel("Probability")
            plt.ylabel("Throughput")
            plt.show()
        
        elif ch==4:
            Ulists=list()
            wlists=list()
            R=float(input("Enter the Bandwidth"))
            P=float(input("Enter the probability"))
            tp=float(input("Enter the Processing Delay"))
            L=float(input("Enter the no of bits to be transmitted"))
            k=5
            while k>0:
                W=int(input("Enter the Window Size"))
                if W>=((2*((tp*R)/L))+1) :
                    U=1-P
                    U=U*R
                else:
                    U=(W*(1-P))/((2*((tp*R)/L))+1)
                    U=U*R
                Ulists.append(U)
                wlists.append(W)
                k=k-1
            plt.scatter(wlists,Ulists,color="red")
            plt.plot(wlists,Ulists)
            plt.xlabel("Window Size")
            plt.ylabel("Throughput")
            plt.show()

        else:
            print("Invalid Input")

    elif choice==4:
        break

    else:
        print("Invalid Input")
