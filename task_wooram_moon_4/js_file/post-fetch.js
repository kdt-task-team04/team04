fetch("https://jsonplaceholder.typicode.com/posts")
    .then((response) => response.json())
    .then((posts) => {
        posts.forEach((e) => {
            const { title } = e;
            console.log(title);
        });
    });
