
// fetch 를 활용한 todos 정보 찾기
fetch("https://jsonplaceholder.typicode.com/todos")
    .then((response) => response.json())
    .then((todos) => {
        todos.forEach((todo) => {
            const { id, title, completed } = todo;
            todoInfo(id, title, completed);
        });
    });

function todoInfo(id, title, completed) {
    console.log(
        `id: ${id}${"\n\n"}title: ${title}${"\n\n"}completed: ${completed}${"\n\n"}`
    );
}

// fetch를 활용한 users 내의 zipcode 정보 찾기
fetch("https://jsonplaceholder.typicode.com/users")
    .then((response) => response.json())
    .then((users) => {
        users.forEach((user) => {
            const zipcode = user.address.zipcode;

            console.log(`UserID : ${zipcode}`);
        });
    });


