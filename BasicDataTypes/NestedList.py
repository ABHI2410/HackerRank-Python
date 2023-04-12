#Given the names and grades for each student in a class of  students,
#store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
if __name__ == '__main__':
    nested_list = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested_list.append([name,score])
    min_val = min(nested_list, key = lambda x : x[1] )
    nested_list = [item for item in nested_list if item[1] != min_val[1]]
    required_score = min(nested_list, key = lambda x : x[1] )
    answer = [item for item in nested_list if item[1] == required_score[1]]
    answer.sort()
    for item in answer:
        print(item[0])