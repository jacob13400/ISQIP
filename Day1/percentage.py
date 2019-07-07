if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
      #  print(student_marks[name])
    query_name = input()

    sum=student_marks[query_name][0]+student_marks[query_name][1]+student_marks[query_name][2]
    sum/=3.00
    sum*=10
    #print(sum)
    sum=round(sum,1)
    print(str(sum)[:-3]+"."+str(sum)[-3]+str(sum)[-1])
    
