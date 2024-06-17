from urllib import response
import requests
import sys

a = '='*40

print(a,'\nA program for calculating the number of repositories on GitHub in the desired language','\n',a)
print("1. Java", "\n2. Python", "\n3. JavaScript", "\n4. C+")

lang = input(f'In which language do you want to know the number of repositories? --> ')
if lang == '1':
    lang = 'java'
elif lang == '2':
    lang = 'python'
elif lang == '3':
    lang = 'javascript'
elif lang == '4':
    lang = 'c++'
else: 
    print('Wrong number, try again.')
    sys.exit()
    
params = {'q' : '' + lang}
response = requests.get('https://api.github.com/search/repositories', params=params)
response_json = response.json()
print("Total count of repositories on",lang,"is",response_json['total_count'])
    


    




