def arithmetic_arranger(problems, show_answers=False):
    pass

# define arithmetic problem
problems = ["3 + 8765","2 - 99", "4000 + 300","1 - 55"]
output = ['','','','']

if len(problems) > 4:
    raise ValueError('Error: Too many problems.')
else:
    for problem in problems:
        first_operand=''
        second_operand=''
        operator=''
        result=''
        
        # remove any whitespaces
        problem = problem.translate(str.maketrans('','',' '))
        
        # check if operator exists
        index = problem.find('+')
        if index > 0:
            operator = problem[index]
        else:
            index = problem.find('-')
            if index > 0:
                operator = problem[index]
            else:
                raise ValueError("Error: Operator must be '+' or '-'.")
        
        first_operand = problem[:index]
        second_operand = problem[index+1:]
        
        # check operators
        if len(first_operand) > 4 or len(second_operand) > 4:
            raise ValueError('Error: Numbers cannot be more than four digits.')
        if not first_operand.isnumeric() or not second_operand.isnumeric():
            raise ValueError('Error: Numbers must only contain digits.')
        
        # longest operand + 2 (operand + whitespace) is total length
        problem_length = max(len(first_operand), len(second_operand)) + 2
        
        # first row
        for _ in range(problem_length - len(first_operand)):
            output[0] += ' '
        output[0] += first_operand
        output[0] += '    '

        # second row
        output[1] += operator
        for _ in range(problem_length - 1 - len(second_operand)):
            output[1] += ' '
        output[1] += second_operand
        output[1] += '    '

        # third row
        for _ in range(problem_length):
            output[2] += '-' 
        output[2] += '    '

        # calculate result
        if operator == '+':
            result = str(int(first_operand) + int(second_operand))
        else:
            result = str(int(first_operand) - int(second_operand))

        # result row
        for _ in range(problem_length - len(result)):
            output[3] += ' '
        output[3] += result
        output[3] += '    '

        #print(index, first_operand, operator, second_operand, result)

print(output[0])
print(output[1])
print(output[2])
print(output[3])

            

        

