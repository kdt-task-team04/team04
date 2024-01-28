fetch("https://jsonplaceholder.typicode.com/users")
    .then((response) => response.json())
    .then((users) => {
        users.forEach((user) => {
            const {name} = user.company
            test(name);
        })
})

function test(name) {
    console.log(name)
}