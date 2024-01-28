fetch("https://jsonplaceholder.typicode.com/todos")
    .then((response) => response.json())
    .then((todos) => {
        todos.forEach((todo) => {
            const {completed} = todo
            test(completed);
        })
})

function test(completed) {
    console.log(completed)
}