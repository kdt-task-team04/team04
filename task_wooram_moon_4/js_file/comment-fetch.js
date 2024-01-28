fetch("https://jsonplaceholder.typicode.com/comments")
    .then((response) => response.json())
    .then((comments) => {
        comments.forEach((e) => {
            const { email } = e;
            comment(email);
        });
    });

function comment(email) {
    console.log(email);
}
