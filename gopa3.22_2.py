#별찍기를 파일안에 출력해서 저장하기 
#with (파일경로,"모드") as 파일변수:
#파일변수.wirte()
#파일변수.read()

path = "/Users/parkmw/Desktop/PyWorkspace"
star =""
n = int(input("N :"))

for i in range(1,n+1):
    star = "*"*i
    star = star + "\n"
    with open(path+"/"+"py.txt","a", encoding='utf-8') as f:
        f.write(star)
       


