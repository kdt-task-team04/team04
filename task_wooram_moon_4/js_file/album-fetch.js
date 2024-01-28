fetch("https://jsonplaceholder.typicode.com/albums")
    .then((response) => response.json())
    .then((comments) => {
        comments.forEach((e) => {
            const { title } = e;
            comment(title);
        });
    });

function comment(album) {
    console.log(album);
}
