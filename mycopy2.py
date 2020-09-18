rfile=input("복사할 파일명 입력 : ")
wfile=input("생성할 파일명 입력 : ")

fdr=open(rfile, 'rb')
fdw=open(wfile, 'wb')

'''chunk_size=50

while True :
    buf=fdr.read(chunk_size)
    fdw.write(buf)

    if len(buf)<chunk_size :
        break
'''

for buf in fdr :
    fdw.write(buf)
    

fdr.close()
fdw.close()
