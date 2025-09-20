import time
import winsound
num = int(input("Enter a number to start the countdown :"))

while num >=0:
    print(num)
    winsound.Beep(1000,200)
    #1000Hz 200ms
    num -= 1
    time.sleep(1)
print("Countdown is finished!")
        



   
             
           

                
                                      
