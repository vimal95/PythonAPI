import requests
import json

def func1():
    
    URL="https://jsonplaceholder.typicode.com/posts/1"
    
    response = requests.get(URL)
    
    rs = response.text
    print(response)
    print(rs)
    
    
def func2():
    
    URL1="https://jsonplaceholder.typicode.com/posts"
    
    response1 = requests.get(URL1)
    
    rs1 = response1.text
    print(response1)
    print(rs1)
    
def func3():
    
    URL2="https://jsonplaceholder.typicode.com/posts"
    Data ='''{
      title: 'HII Guidanz',
      body: 'bar',
      userId: 1
    })'''
    response2 = requests.post(URL2,data=Data)
    
    rs2 = response2.text
    print(response2)
    print(rs2)
    
    

if __name__=="__main__":
    func1()
    func2()
    func3()
    
    
