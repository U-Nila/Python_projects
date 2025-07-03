tasks=[]
while True:
    print("\n----to do list---")
    print("1.add task")
    print("2.remove task")
    print("3.view task")
    print("4.exit the app")
    choice=input("enter your choice(1-4):")
    if choice=="1":
        task=input("enter your task:")
        tasks.append(task)
        print("your tasks are added")
    elif choice=="2":
        if len(tasks)==0:
            print("there is no task to remove")
        else:
            for i,task in enumerate(tasks):
                print(f"{i+1}.{task}")
            index=int(input("enter a number to remove the task:"))
            if 1<=index<=len(tasks):
                removed=tasks.pop(index-1)
                print(f" Removed:{removed}")
            else:
                print("please enter the valid number")
    elif choice=="3":
        
        if len(tasks)==0:
            print("there is no task to remove")
        else:
            print("these are your tasks")
            for i,task in enumerate(tasks):
                print(f"{i+1}.{task}")
               
    elif choice=="4":
        print("bye!!!..see you next time")
        break
    else:
        print("please enter the valid number from above option")