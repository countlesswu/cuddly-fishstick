Note=open('origin.txt',mode='w')
for num in range(1,501):
    num=str(num)
    number=num.zfill(4)
    a='/home/wuliang/target_tracker/data/Girl/img/' + number + '.jpg'
    Note.write(a)
    Note.write('\n')
Note.close()