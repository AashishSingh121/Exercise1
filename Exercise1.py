import pandas as pd
import datetime as dt

x=pd.DataFrame([{'S.No':1,'Agent_Id':100,'Agent_Name':'A','Status':"Available"},                            #Database of Agents
               {'S.No':2,'Agent_Id':101,'Agent_Name':'B','Status':'Unavailable'},
               {'S.No':3,'Agent_Id':102,'Agent_Name':'C','Status':"Available"},
               {'S.No':4,'Agent_Id':103,'Agent_Name':'D','Status':"Unavailable"}])


def issue():
    start_time=dt.datetime.now()                                                                            #Time when new issue comes in
    p_status = 'RESOLVED'
    Ag=x.where(x['Status']=="Available")
    B=Ag.dropna()                                                                                           #List of Agent(s) free for work
    num=B['Agent_Id'].count()


    while p_status!='Abandoned':

        if num>=1:
            print("\nCurrently Available (",num,") Agents")
            n=int(input("Enter number of agent(s) required :" ))
            if n==1:
                D = B.sample()                                                                              #Selecting Agent randomly from available list
                assign_time = dt.datetime.now()
                na=((D['Agent_Name']).to_string(index=False))
                print('\nAgent Selected',na)
                print("Assigning Time",assign_time-start_time)
                l=""

                while l!='Y':
                    m = input("\nIs issue Resolved(Y/N)")
                    if m=='y' or m=='Y':                                                                    #When issue is resolved
                        resolve_time=dt.datetime.now()
                        total_time=resolve_time-assign_time
                        print("\nTime taken to resolve issue:\t",total_time)
                        p_status='Abandoned'
                        break
                    elif m=='n' or m=='N':                                                                  #When customer leaves without problem being resolved
                        abandon_time=dt.datetime.now()
                        total_time=abandon_time-assign_time
                        print("\nCustomer Left After:\t", total_time)
                        print("Issue Unresolved")
                        p_status='Abandoned'
                        break
                    else :
                        print("\nInvalid Input!!\nTry again")
                        continue

            elif n>1 and n<=num:
                G=B.sample(n)                                                                                #Selecting Agents randomly from available list
                assign_time = dt.datetime.now()
                nb = ((G['Agent_Name']).to_string(index=False))
                print('Agents Selected\n', nb)
                print("Assigning Time", assign_time - start_time)
                l = ""

                while l!= 'Y':
                    m = input("\nIs issue Resolved(Y/N)")

                    if m == 'y' or m == 'Y':                                                                 # When issue is resolved
                        resolve_time = dt.datetime.now()
                        total_time = resolve_time - assign_time
                        print("Time taken to resolve issue by ",n,"Agents",":\t", total_time)
                        p_status = 'Abandoned'
                        break
                    elif m == 'n' or m == 'N':                                                               # When customer leaves without problem being resolved
                        abandon_time = dt.datetime.now()
                        total_time = abandon_time - assign_time
                        print("Customer Left After:\t", total_time)
                        print("\nIssue Unresolved")
                        p_status = 'Abandoned'
                        break
                    else:
                        print("Invalid Input!!\nTry Again")
                        continue
            else:
                print("Invalid input!!\n Try Again")
                continue

        else:                                                                                                #This works when all the agents are unavailable
            print("No Agent available currently !!\nTry after sometime")
            break
issue()