import pywars
import re
import pathlib
# 01-Apr-2015 10:00:03.428 client 249.169.199.235#55766: query: talkgadget.google.com IN A + ((8.8.8.8))
path = '/home/student/Public?log/dnslogs/'
from collections import Counter

def lab330(the_data):
    #Open specified file from /home/student/Public/log/dnslogs
    #Retrieve all the IP addresses from the log specified in the_data
    #Pass that list to sorted() and return it
    the_file, the_search = the_data
    c = Counter()
    if os.path.isfile(path+the_file)=True:
        for eachline in open(path+the_file,'r').readlines():            
            the_client, the_dns = re.findall(r'client (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).+query: (\w\-\.]+)', eachline)

    pass


d = pywars.Client()
d.login()
print(d.answer(lab330(d.data('lab3.3.0'))))
