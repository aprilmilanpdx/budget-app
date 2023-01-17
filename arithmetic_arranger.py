problemset = ['32 + 698', '3801 - 2', '45 + 43', '123 + 49']

import re

# turn it into this:
# "    3    3801    45     123\n+ 698    -2    + 43    + 49\n____    _____    ____    _____"

def arithmetic_arranger(problems, solve = False):
  num1 = ""
  num2 = ""
  operator = ""
  sumdiff = ""
  answer = ""

 # split problems by space and create num1, num2, and operator variables
  for problem in problems:
    if re.search("[^\s0-9.+-", problems]):

      
    num1 = problem.split()[0]
    num2 = problem.split()[2]
    operator = problem.split()[1]
    
# calculate longest line length
    width = max(len(num1), len(num2))
    
  # # create output lines
    line1 = num1.rjust(width + 2)
    line2 = operator + num2.rjust(width + 1)
    line3 = "-" * (width + 2)
  
    answer = line1 + '    \n' + line2 + '    \n' + line3 
    print(answer)

arithmetic_arranger(problemset)


