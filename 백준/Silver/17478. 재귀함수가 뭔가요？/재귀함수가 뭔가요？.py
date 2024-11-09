n = int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")

def recursive_story(question, intro_line1, intro_line2, intro_line3, indentation, conclusion, depth):
    if n == depth:
        print(indentation + question)
        print(indentation + '"재귀함수는 자기 자신을 호출하는 함수라네"')
        print(indentation + conclusion)
        return

    print(indentation + question)
    print(indentation + intro_line1)
    print(indentation + intro_line2)
    print(indentation + intro_line3)

    recursive_story(question, intro_line1, intro_line2, intro_line3, indentation + '____', conclusion, depth + 1)
    print(indentation + conclusion)


question = '"재귀함수가 뭔가요?"'
intro_line1 = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
intro_line2 = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
intro_line3 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
indentation = ''
conclusion = '라고 답변하였지.'

recursive_story(question, intro_line1, intro_line2, intro_line3, indentation, conclusion, 0)
