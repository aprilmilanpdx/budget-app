problemset = ['32 + 698', '3801 - 2', '45 + 43', '123 + 49']

import re

def arithmetic_arranger(problems, solve = False):
  if len(problems) > 5:
    return "Error: Too many problems."

  num1 = ""
  num2 = ""
  operator = ""
  answer = ""

 # split problems by space and create num1, num2, and operator variables
  for problem in problems:
    if re.search("[^\s0-9.+-]", problem):
        if re.search("[*]", problem) or re.search("[/]", problem):
          return "Error: Operator must be '+' or '-'."
        return "Error: Numbers must only contain digits."

    num1 = problem.split()[0]
    num2 = problem.split()[2]
    operator = problem.split()[1]
    
    if len(num1) > 4 or len(num2) > 4:
      return "Error: Numbers cannot be more than four digits."
    
    solution = ""
    if operator == "+":
      solution = str(int(num1) + int(num2))
    else:
      solution = str(int(num1) - int(num2))

# calculate longest line length
    width = max(len(num1), len(num2))
    
  # create output lines
    line1 = num1.rjust(width + 2)
    line2 = operator + num2.rjust(width + 1)
    line3 = "-" * (width + 2)
    line4 = str(solution).rjust(width + 2)
  
    answer = line1 + '    \n' + line2 + '    \n' + line3 
    print(answer)

arithmetic_arranger(problemset)


