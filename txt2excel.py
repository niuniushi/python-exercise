import xlwt
#import Workbook
#import Worksheet
#f=open('test.txt','r')
book=xlwt.Workbook(encoding='utf8',style_compression=0)
sheet=book.add_sheet('grade', cell_overwrite_ok=True)



i=0
for line in open("test.txt"):
    if(len(line)>2):
        s1=line.split(':')
        s21=s1[0].split('"')
        s22=s1[1].split(',')
        s31=s22[0].split('"')
        s32=s22[3].split(']')
        sheet.write(i,0,s21[1])
        sheet.write(i,1,s31[1].decode('gbk'))
        sheet.write(i,2,s22[1])
        sheet.write(i,3,s22[2])
        sheet.write(i,4,s32[0])
        i=i+1

book.save('students.xls')
    

