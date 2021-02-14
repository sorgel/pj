import subprocess, sys, os

script_line_1 = '''tell application \"Finder\" to set insertionLocation to insertion location as alias'''
script_line_2 = '''return POSIX path of insertionLocation'''

new_project_name = 'test folder'

location = str(subprocess.check_output(['osascript', '-e', script_line_1, '-e', script_line_2]))
location = location[2:-3]
location = location + new_project_name

print('Result:', location)

# f = open(location, "w+")
# for i in range(10):
#      f.write("This is line %d\r\n" % (i+1))
# f.close() 

try:
    os.mkdir(location)
except OSError:
    print ("Creation of the directory %s failed" % new_project_name)
else:
    print ("Successfully created the directory %s " % new_project_name)