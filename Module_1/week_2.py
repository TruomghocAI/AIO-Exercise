def exercise_1():
    def sliding_window(lst_data,k):
        data_sliding =[]
        n = len(lst_data)
        
        for i in range(n - k + 1):
            x = max(lst_data[i:i+k])
            data_sliding.append(x)
            
        return data_sliding
        
    def question_1():
        data = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
        k = 3
        print(sliding_window(data, k))
    question_1()
    
def exercise_2():
    def count_chars(strings):
        dic = {}
        for i in strings:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        return dic

    def question_2():
        strings = "Happiness"
        dic_cnt = count_chars(strings)
        for a , b in dic_cnt.items():
            print(a,b)
    question_2()

def exercise_3():
    file = open("C:\\Users\\admin\\OneDrive\\Tài liệu\\AIO-Exercise\Module_1\\file_data.txt")
    def count_word(file_data):
        tmp = {}
        for line in file_data:
            words = line.split()
            for word in words:
                word = word.lower()
                if word in tmp:
                    tmp[word] += 1
                else:
                    tmp[word] = 1
        return tmp
    
    def question_3():
        file_data = file.read()
        count_file = count_word(file_data)
        for a , b in count_file.items():
            print(a, b)
    question_3()
    file.close()

def exercise_4():
    def levenshtein_distance(s1, s2):
        m, n = len(s1), len(s2)
        
        distance = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            distance[i][0] = i
        for j in range(n + 1):
            distance[0][j] = j
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                cost = 0 if s1[i - 1] == s2[j - 1] else 1
                distance[i][j] = min(
                    distance[i - 1][j] + 1,    
                    distance[i][j - 1] + 1,   
                    distance[i - 1][j - 1] + cost  
                )
        for i in distance:
            print(i)
        print()
        print(distance[m][n])

    s1 = "yo"
    s2 = "you"
    levenshtein_distance(s1, s2)

if __name__ == "__main__":
  
    exercise = int(input("Select the exercise you want to test:\n 1:exercise_1\n 2:exercise_2\n 3:exercise_3\n 4:exercise_4\n"))
    if exercise == 1:
      exercise_1()
    elif exercise == 2:
      exercise_2()
    elif exercise == 3:
      exercise_3()
    elif exercise == 4:
      exercise_4()