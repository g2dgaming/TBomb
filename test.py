from urllib import response
import requests

def main():
    numbers=[]
    response=requests.get('http://127.0.0.1:8000/api/targets?key=FuckSociety', json={
    'key': 'FuckSociety',
    }).json()
    if len(response) > 0:
        for target in response:
            numbers.append(target['phone_number'])
    else:
        print('Empty')

    for number in numbers:
        print(number)
if __name__ == "__main__":
    main()