fetch("https://jsonplaceholder.typicode.com/posts")
    .then((response) => response.json())
    .then((posts) => {
        posts.forEach((post) => {
            const { body } = post;

            postInfo(body);
        });
    });

function postInfo(body) {
    console.log(body);
}
