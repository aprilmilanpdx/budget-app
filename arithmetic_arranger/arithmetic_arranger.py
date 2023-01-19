import re

def arithmetic_arranger(problems, solve = False):
  # arranges addition/subtraction problems horizontally, first argument:list of 1 to 5 problems, each with two numbers 1 to 4 digits each, with the + or - operator in between, second argument: boolean whether to solve problem(s), default = False
  
  if len(problems) > 5:
    return "Error: Too many problems."
  
  # create empty output line
  line1 = ""
  line2 = ""
  line3 = ""
  line4 = ""
  
  # error if anything other than digits entered in numbers and if operator is not "+" or "-"
  for index, problem in enumerate(problems):
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
    
    # calculate longest line length 
    width = max(len(num1), len(num2)) + 2
        
    # perform problem 
    if operator == "+":
      answer = str(int(num1) + int(num2))
    else:
      answer = str(int(num1) - int(num2))
    
    spacer = "    " if index < len(problems) - 1 else ""
  
    line1 += num1.rjust(width) + spacer
    line2 += operator + num2.rjust(width - 1) + spacer
    line3 += "-" * width + spacer
    line4 += answer.rjust(width) + spacer 
    
  if solve == True:
    return line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
  else:
    return line1 + "\n" + line2 + "\n" + line3
