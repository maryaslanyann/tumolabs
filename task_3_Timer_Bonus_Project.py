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

hour = int(hour)
minute = int(minute)
second = int(second)

while hour > -1:
    for i in range(minute,-1,-1):
        for j in range(second,-1,-1):
            if i < 10:
                if j < 10:
                   print(f"{hour}:0{i}:0{j}")
                else:
                    print(f"{hour}:0{i}:{j}")
            else:
                if j < 10:
                    print(f"{hour}:{i}:0{j}")
                else:
                    print(f"{hour}:{i}:{j}")

            t.sleep(1)

           
        second = 59
    hour-=1
    minute = 59
     

print("The End :)")
