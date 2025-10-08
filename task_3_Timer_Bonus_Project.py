import time as t

while True:
    time = input("Insert time to count down (h:m:s) - ")
    parts = time.split(":")
    
    if len(parts) == 3 and all(part.isdigit() for part in parts):
        hour = parts[0]
        minute = parts[1]
        second = parts[2]
    
        break  

    else:
        print("Please enter time in h:m:s form with numbers only.")


while int(hour) > -1:
    if int(hour) < 10:
        for i in range(int(minute),-1,-1):
            for j in range(int(second),-1,-1):
                if i < 10:
                    if j < 10:
                       print(f"0{int(hour)}:0{i}:0{j}")
                    else:
                        print(f"0{int(hour)}:0{i}:{j}")
                else:
                    if j < 10:
                        print(f"0{int(hour)}:{i}:0{j}")
                    else:
                        print(f"0{int(hour)}:{i}:{j}")

                t.sleep(1)

               
            second = 59

        hour = int(hour)
        hour-=1
        
        minute = 59

    else:
        for i in range(int(minute),-1,-1):
            for j in range(int(second),-1,-1):
                if i < 10:
                    if j < 10:
                       print(f"{int(hour)}:0{i}:0{j}")
                    else:
                        print(f"{int(hour)}:0{i}:{j}")
                else:
                    if j < 10:
                        print(f"{int(hour)}:{i}:0{j}")
                    else:
                        print(f"{int(hour)}:{i}:{j}")

                t.sleep(1)

               
            second = 59

        hour = int(hour)
        hour-=1
        
        minute = 59
         

print("The End :)")
