if __name__ == '__main__':
    n = int(input())
    if n >=2 and n <=10:
        student_marks = {}
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores
 
        query_name = input()
    
        for name, scores in student_marks.items():
            if name == query_name:
                total = 0
                for score in scores:
                    total = total + score
            
                result = total / len(scores)
                print(f"{result:.2f}")