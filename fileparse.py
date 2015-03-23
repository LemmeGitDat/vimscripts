import re
import vim

filein = open("../../work/python/test.vhd", "r")
#filein = open("test.vhd", "r")
#out = open("output.txt", "w")
filetext = filein.read()
filein.close()

m = re.search(r"entity.*?end",filetext, re.MULTILINE | re.DOTALL)
a = m.group(0)
numports = 0
counter = 0
numports = a.count(':')
while True:
  g = re.search(r"\s*(\w+)\s*:", a)
  if g is not None :
      if counter < numports-1:  
        a = re.sub(r":.*?(in|out)\s*", "=> %s,   --" % (g.group(1)), a, count =1)
        counter = counter+1
      else:
        a = re.sub(r":.*?(in|out)\s*", "=> %s   --" % (g.group(1)), a, count =1)
        counter = counter+1
  else :
    break
m = re.sub(r"entity ", "inst_name: entity work.", a)
j = re.sub(r"\(", "", m)
l = re.sub(r"port", "", j)
k = re.sub(r"is", "port map(", l)
z = re.sub(r"end", "", k)
#print (z)

#get the number of lines in the port map
numLines = z.count('\n')

#split the string into an array of lines
lineStrings = z.splitlines()

#get the current cursor position
(row, col) = vim.current.window.cursor

count = 0
rowCount = row
while count < numLines:
  vim.command("put =''")
  vim.current.buffer[rowCount] = lineStrings[count]
  count = count + 1
  rowCount = rowCount + 1
