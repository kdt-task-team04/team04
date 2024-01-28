fetch("https://jsonplaceholder.typicode.com/users")
    .then((response) => response.json())
    .then((posts) => {
        posts.forEach((e) => {
            const { name, email } = e;
            comment(name, email);
        });
    });

function comment(name, email) {
    console.log(`${"\n"} 이름: ${name}, ${"\n"} 이메일: ${email}`);
}
