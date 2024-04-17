#! usr/bin/python3
"""

"""
import requests
import sys

def main():
    id = validate_input()
    base_url = 'https://jsonplaceholder.typicode.com'
    
    try:
        endpoint = f'users/{id}'
        user = get_response(base_url, endpoint)
    except requests.exceptions.HTTPError as e:
        print(e)
        
    try: 
        endpoint = f'/todos?userId={id}'
        todos = get_response(base_url, endpoint)
    except requests.exceptions.HTTPError as e:
        print(e)
          
    name = user['name']
    completed_tasks = [task for task in todos if task['completed']]
    task_count = len(todos)
    completed_count = len(completed_tasks)
    
    print(f"Employee {name} is done with tasks({completed_count}/{task_count}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")
    


def get_response(base_url, endpoint):
    response = requests.get(f'{base_url}/{endpoint}')
    if response.status_code == 200:
        return response.json()
    else:
        raise requests.exceptions.HTTPError(f'Error: {response.status_code}')


def validate_input():
    if len(sys.argv) != 2:
        print('Usage: python3 0-gather_data_from_an_API.py <employee_id>')
        sys.exit(1)
    try:
        id = int(sys.argv[1])
    except ValueError:
        print('Employee id must be an integer')
        sys.exit(1)
    return id

if __name__ == '__main__':
    main()