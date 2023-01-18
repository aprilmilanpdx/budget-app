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
    operator = values[1]
    num2 = values[2]

    # error if any number is more than 4 digits
    if len(num1) > 4 or len(num2) > 4:
      return "Error: Numbers cannot be more than four digits."
    
    # calculate longest line length and append value to list of values
    width = max(len(num1), len(num2)) + 2
    values.append(width)
    
    # line = " "
    # for i in range(width):
    #   line += "-"
            
    #perform problem and append answer to values list
    if operator == "+":
      answer = str(int(num1) + int(num2))
    else:
      answer = str(int(num1) - int(num2))
    values.append(answer)

    solutions.append(values)

  # print(solutions)
  
    # create output lines
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    # iterate through solutions list containing values list and create joined data for each line
    for output in solutions:
      padding = output[3]
      line1 += output[0].rjust(padding) + "    "
      line2 += output[1] + output[2].rjust(padding - 1) + "    "
      line3 += "-" * output[3] + "    "
      line4 += output[4].rjust(padding) + "    " 
  
  print(line1 + '\n' + line2 + '\n' + line3)
  print(line1 + '\n' + line2 + '\n' + line3 + '\n' + line4)
    

arithmetic_arranger(problemset)


