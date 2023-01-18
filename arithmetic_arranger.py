problemset = ['32 + 698', '3801 - 2', '45 + 43', '123 + 49']

import re

def arithmetic_arranger(problems, solve = False):
  # error if more than 5 problems
  if len(problems) > 5:
    return "Error: Too many problems."
  
  # create empty list of solutions
  solutions = []

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
    
    # calculate longest line length 
    line = ""
    width = max(len(num1), len(num2)) + 2
    for i in range(width):
      line += "-"
    values.append(line)
        
    #perform problem and append answer to values list
    if operator == "+":
      answer = str(int(num1) + int(num2))
    else:
      answer = str(int(num1) - int(num2))
    values.append(answer)

    solutions.append(values)
  

    # create output lines
    # line1 = ""
    # line2 = ""
    # line3 = ""
    # line4 = ""

    # iterate through ********* to create joined data for lines 
    # for output in values:

    # line1 = output[0].rjust(width) + " " * 4
    # line2 = output[1] + output[2].rjust(width - 1) + " " * 4
    # line3 = output[3] + " " * 4
    # line4 = output[4].rjust(width) + " " * 4
  
    # solution = line1 + '    \n' + line2 + '    \n' + line3 
    # print(solution)

arithmetic_arranger(problemset)


