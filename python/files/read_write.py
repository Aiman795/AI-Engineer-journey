with open ('test.txt','r') as f:
    size=10
    text=f.read(size)
    while len(text)>0:
        print(text)
        text=f.read(size)

with open('text2.txt','w') as a:
    a.write("hello")


with open ('pic.jpeg','rb') as rf:
    with open ('pic-copy.jpeg','wb') as wf:
        size=4096
        pic=rf.read(size)
        while len(pic)>0:
            wf.write(pic)
            pic=rf.read(size)