fetch("https://jsonplaceholder.typicode.com/comments")
    .then((response) => response.json())
    .then((comments) => {
        comments.forEach((comment) => {
            const {email} = comment
            test(email);
        })
})

function test(email) {
    console.log(email)
}