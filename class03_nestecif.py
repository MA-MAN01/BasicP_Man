# username = input("Enter oyue user name :");
# password = input("Enter your password :");

# if username == "admin" :
#     if password == "admin123" :
#         print("You're admin");
#     else :
#         print("Wrong");
# elif username == "user" :
#     if password == "user123" :
#         print("You're User");
#     else :
#         print("Wrong");
# else :
#     print("Not fond");

#-------------------------------------------------------
                      # WORKSHOP
k = "สาขากรุงเทพ";
i = "สาขาอิตาเลียนโน";
s = "สาขาสาทร";

meme = input("Enter Your REEL MEME :")
word1 = ""
station = input("Enter Your station :")
word1 += meme;
if meme == "ตะแน่ว":
    if station == k:#(เลือกสาขา =สาขากรุงเทพ,สาขาอิตาเลียนโน,สาขาสาทร)
        print("คุณสุดยอด","คุณคือ",word1);
    elif station == s :#(เลือกสาขา =สาขากรุงเทพ,สาขาอิตาเลียนโน,สาขาสาทร)
        print("คุณมาเกือบถุก");
    else :
        print("คุณไม่ตะแน่ว");
elif meme == "italianbrainrot":
    if station == i:#(เลือกสาขา =สาขากรุงเทพ,สาขาอิตาเลียนโน,สาขาสาทร)
        print("คุณสมองเน่า","คุณคือ",word1);
    elif station == k :#(เลือกสาขา =สาขากรุงเทพ,สาขาอิตาเลียนโน,สาขาสาทร)
        print("คุณมาเกือบถุก");
    else :
        print("คุณไม่สมองเน่า");
else :
    print("Not FOND");

   
    

    

    

