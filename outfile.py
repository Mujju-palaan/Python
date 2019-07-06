#    WRITEFILE
#outFile = open('text.txt', 'w')
#outFile.write('this is a line 1\n')
#outFile.write('this is a line 2\n')
#outFile.close()
outFile = open('grades.txt','w')
grade = 0
while (grade != "q"):
    print("enter a grade (q to quit): ")
    grade = raw_input()
    outFile.write(grade + '\n')
outFile.close()


    