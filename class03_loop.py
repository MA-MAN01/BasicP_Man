# sum = 0;
# n = 3; 

#   start   stop(หยุดก่อนถึง)   step(ข้ามไปตามตำแหน่งที่ใส่ 1 ขึ้นไป 2 = 3)
# for i in range(n) :
#     sum += i+1;
#     print(i);
# print(sum);

#-------------------FOR-----------------------
# num = int(input("Enter your number :"))
# for i in range(12) :
#     i += 1
#     sum = num*i
#     print(num,"*",i,":",sum)

#--------------------While-------------
start = True
arrow = 30
hammer = 60
sword = 20
mon = 100 

rehp1 = mon - arrow
rehp2 = mon - hammer
rehp3 = mon - sword

while start :
    print("[1]attackk")
    print("[2]runaway")
    choice1 = int(input("Chose your way :"))
    if choice1 == 1 :
            choice2 = int(input("จะตีกี่รอบ :"))
            for i in range(choice2) :
                print("Monster King HP",mon) 
                print("[1] Arrow",arrow," damage")
                print("[2] Hammer ",hammer," damage")
                print("[3] Sword ",sword," damage")
                choice3 = int(input("Chohse Your Waepon :"))
                if choice3 == 1 :
                    mon -= arrow  
                elif choice3 == 2 :
                    mon -= hammer 
                elif choice3 == 3 :
                    mon -= sword 
            if mon == 0 :
                 print("You win")
            elif mon < 0 and choice3 == 1:
                 print("Monster King HP",rehp1)
                 print("You lose")
            elif mon < 0 and choice3 == 2:
                 print("Monster King HP",rehp2)
                 print("You lose")
            elif mon < 0 and choice3 == 3:
                 print("Monster King HP",rehp3)
                 print("You lose")
    else :
        print("Good Bye")
    start = False