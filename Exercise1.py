import pandas as pd
import datetime as dt

x=pd.DataFrame([{'S.No':1,'Agent_Id':100,'Agent_Name':'A','Status':"Available"},                            #Database of Agents
               {'S.No':2,'Agent_Id':101,'Agent_Name':'B','Status':'Unavailable'},
               {'S.No':3,'Agent_Id':102,'Agent_Name':'C','Status':"Available"}])


def issue():
    start_time=dt.datetime.now()                                                                            #Time when new issue comes in
    p_status = 'RESOLVED'
    Ag=x.where(x['Status']=="Available")
    B=Ag.dropna()                                                                                           #List of Agent(s) free for work
    num=B['Agent_Id'].count()


    while p_status!='Abandoned':

        if num>=1:
            print("Currently Available (",num,") Agents")
            n=int(input("Enter number of agent(s) required" ))
            if n==1:
                D = B.sample()                                                                              #Selecting Agent randomly from available list
                assign_time = dt.datetime.now()
                na=((D['Agent_Name']).to_string(index=False))
                print('Agent Selected',na)
                print("Assigning Time",assign_time-start_time)
                m=input("Is issue Resolved(Y/N)")

                if m=='y' or m=='Y':                                                                         #When issue is resolved
                    resolve_time=dt.datetime.now()
                    total_time=resolve_time-assign_time
                    print("Time taken to resolve issue:\t",total_time)
                    p_status='Abandoned'
                elif m=='n' or m=='N':                                                                       #When customer leaves without problem being resolved
                    abandon_time=dt.datetime.now()
                    total_time=abandon_time-assign_time
                    print("Customer Left After:\t", total_time)
                    print("\nIssue Unresolved")
                    p_status='Abandoned'
                else :
                    print("Invalid Input!!")
                    continue

            elif n>1 and n<=num:
                G=B.sample(n)                                                                                #Selecting Agents randomly from available list
                assign_time = dt.datetime.now()
                nb = ((G['Agent_Name']).to_string(index=False))
                print('Agents Selected\n', nb)
                m = input("Is issue Resolved(Y/N)")

                if m == 'y' or m == 'Y':                                                                     # When issue is resolved
                    resolve_time = dt.datetime.now()
                    total_time = resolve_time - assign_time
                    print("Time taken to resolve issue by ",n,"Agents",":\t", total_time)
                    p_status = 'Abandoned'
                elif m == 'n' or m == 'N':                                                                   # When customer leaves without problem being resolved
                    abandon_time = dt.datetime.now()
                    total_time = abandon_time - assign_time
                    print("Customer Left After:\t", total_time)
                    print("\nIssue Unresolved")
                    p_status = 'Abandoned'
                else:
                    print("Invalid Input!!")
                    continue
            else:
                print("Invalid input!!\n Try Again")
                continue

        else:
            print("No Agent available currently !\n Try after sometime")
            break
issue()