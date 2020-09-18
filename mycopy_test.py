i=1
rfile=input("복사할 파일명 입력 : ")
wfile=input("생성할 파일명 입력 : ")


fdr = open(rfile, 'rb')
fdw = open(wfile, 'wb')

fdr.seek(0,2)
last=fdr.tell()

while i<=last :
    
    fdr.seek(-1*i,2)

    x = fdr.read(1)
    fdw.write(x)

    i +=1

fdr.close()
fdw.close()
