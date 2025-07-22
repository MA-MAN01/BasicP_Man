# # แบบที่ 1 ไม่มี and 
# len = int(input("Enter your length :"));
# if len < 5 :
#     print("Price is Free");
# elif len <= 50 :
#     print("Price is 10");
# elif len <= 100 :
#     print("Price is 15");
# elif len <= 300 :
#     print("Price is 25");
# elif len <= 500 :
#     print("Price is 35");
# else :
#     print("Price is 45");



#แบบที่ 2 มี and
len = int(input("Enter your length :"));
if len < 5 :
    print("Price is free");
elif len >= 5 and len <= 50 :
    print("Price is 10");
elif len >= 51 and len <= 100 :
    print("Price is 15");
elif len >= 101 and len <= 300 :
    print("Price is 25");
elif len >= 301 and len <= 500 :
    print("Price is 35");
else :
    print("Price is 45");