fetch("https://jsonplaceholder.typicode.com/posts")
    .then((response) => response.json())
    .then((posts) => {
        posts.forEach((post) => {
            const { title } = post;

            postInfo(title);
        });
    });

function postInfo(title) {
    console.log(title);
}
