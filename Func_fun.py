'''def my_func():
    print("Hello");
my_func();
def fun(name="zee"):
    print(name);
fun();
myDict={"Arson":"1","Barson":"2"};
t=myDict.get("Barson");
print(t);
a=ord('a');
print(a);
print(myDict);'''
string=input("Enter a string");
string=string.lower();
char=[0]*26;
l=0;
'''while l<27:
    char[l]=int(char[l]);
    l=l+1;'''
for i in string:
    a=ord(i)-97;
    char[a]+=1;
print(char);    
        

    
