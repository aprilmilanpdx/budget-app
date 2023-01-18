problemset = ['32 + 698', '3801 - 2', '45 + 43', '123 + 49']

import re

def arithmetic_arranger(problems, solve = False):
  # error if more than 5 problems
  if len(problems) > 5:
    return "Error: Too many problems."

  # error if anything other than digits entered in numbers and if operator is not "+" or "-"
  for problem in problems:
    if re.search("[^\s0-9.+-]", problem):
        if re.search("[*]", problem) or re.search("[/]", problem):
          return "Error: Operator must be '+' or '-'."
        return "Error: Numbers must only contain digits."

    # split problems by space and create num1, num2, and operator variables
    values = problem.split()
    num1 = values[0]
    num2 = values[2]
    operator = values[1]
    
    # error if any number is more than 4 digits
    if len(num1) > 4 or len(num2) > 4:
      return "Error: Numbers cannot be more than four digits."
    
    # calculate longest line length and append output as "width" to values list
    width = max(len(num1), len(num2)) + 2
    values.append(width)
    
    #print list of list to check progress
    print(values)

    #perform problem and append answer to values list
    if operator == "+":
      answer = str(int(num1) + int(num2))
    else:
      answer = str(int(num1) - int(num2))
    values.append(answer)

  # create output lines
    line1 = num1.rjust(width)
    line2 = operator + num2.rjust(width - 1)
    line3 = "-" * (width)
    line4 = str(answer).rjust(width)
  
    solution = line1 + '    \n' + line2 + '    \n' + line3 
    print(solution)

arithmetic_arranger(problemset)


