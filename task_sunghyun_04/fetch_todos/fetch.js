fetch("https://jsonplaceholder.typicode.com/todos")
    .then((response) => response.json())
    .then((todos) => {
        todos.forEach((todo) => {
            const userId = todo.userId;
            const id = todo.id;
            const title = todo.title;
            const completed = todo.completed;

            console.log(
                `UserID : ${userId}`,
                `/ ID : ${id}`,
                `/ 제목 : ${title} `,
                `/완성도 : ${completed}`
            );
        });
    });