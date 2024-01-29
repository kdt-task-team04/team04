fetch("https://jsonplaceholder.typicode.com/posts")
    .then((response) => response.json())
    .then((posts) => {
        posts.forEach((post) => {
            const { userId, id, title, body } = post;

            postInfo(userId, id, title, body);
        });
    });

function postInfo(userId, id, title, body) {
    console.log(userId, id, title, body);
}
