import pywars
import re
import pathlib
# 01-Apr-2015 10:00:03.428 client 249.169.199.235#55766: query: talkgadget.google.com IN A + ((8.8.8.8))
path = '/home/student/Public?log/dnslogs/'

def lab330(the_data):
    #Open specified file from /home/student/Public/log/dnslogs
    #Retrieve all the IP addresses from the log specified in the_data
    #Pass that list to sorted() and return it
    the_file, the_search = the_data
    for eachline in open(path+the_file):
        c.update(re.findall(r"client .*?query: (\s+) IN", eachline))
      
    pass


d = pywars.Client()
d.login()
print(d.answer(lab330(d.data('lab3.3.0'))))
