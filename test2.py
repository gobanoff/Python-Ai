import requests


def fetch_todos():
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)

    if response.status_code == 200:
        todos = response.json()
        for todo in todos[:10]:  # Get the first 10 todos
            print(
                f"ID: {todo['id']}, Title: {todo['title']}, Completed: {todo['completed']}"
            )
    else:
        print("Failed to fetch data, status code:", response.status_code)


if __name__ == "__main__":
    fetch_todos()


"""
Answer:

ID: 1, Title: delectus aut autem, Completed: False
ID: 2, Title: quis ut nam facilis et officia qui, Completed: False
ID: 3, Title: fugiat veniam minus, Completed: False
ID: 4, Title: et porro tempora, Completed: True
ID: 5, Title: laboriosam mollitia et enim quasi adipisci quia provident illum, Completed: False
ID: 6, Title: qui ullam ratione quibusdam voluptatem quia omnis, Completed: False
ID: 7, Title: illo expedita consequatur quia in, Completed: False
ID: 8, Title: quo adipisci enim quam ut ab, Completed: True
ID: 9, Title: molestiae perspiciatis ipsa, Completed: False
ID: 10, Title: illo est ratione doloremque quia maiores aut, Completed: True

"""
