def q1_sum(data):
    total = 0
    for elements in data:
        total += elements 
    return total


def move_vow(data):
    final = []
    for character in data:
        if character in 'aeiouAEIOU':
            final.append(character)
    for character in data:
        if character not in final:
            final.append(character)
    return "".join(final) 


class Memories():
    
    def __init__(self, **argv):
        self.argv = argv
        pass
    
    def remember(self, memory):
        if memory in self.argv.keys():
            return(self.argv[memory])
        else:
            return False
        

class Test():
    def __init__(self, name='', answers=[], pass_grade = ''):
        self.name = name
        self.answers = answers
        self.pass_grade = int(pass_grade[:-1])
    
class student():
    def __init__(self, name):
        self.name = name
        
    def take_test(self, exam=Test, answers=[]):
        score = 0
        poss_score = len(exam.answers)
        for i in range(len(answers)):
            if answers[i] == exam.answers[i]:
                score += 1
        percentage = (poss_score / 100) * score
        if percentage >= exam.pass_grade:
            print(f'{self.name} has passed the {exam.name} test with a score of {percentage}%')
        else:
            print(f'{self.name} has failed the {exam.name} test')#
            
            
def histogram(data, symbol):
    for n in data:
        print(n * symbol)


def filter_star(dict, number):
    for objects in dict:
        if dict[objects] == number * '*':
            print(f'{objects}:{dict[objects]}')