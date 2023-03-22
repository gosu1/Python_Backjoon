path = "/Users/parkmw/Desktop/PyWorkspace"
star =""
n = int(input("N :"))

for i in range(1,n+1):
    star = "*"*i
    star = star + "\n"
    with open(path+"/"+"py.txt","a", encoding='utf-8') as f:
        f.write(star)
       


