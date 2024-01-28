// fetch("https://jsonplaceholder.typicode.com/photos")
//     .then((response) => response.json())
//     .then((photos) => {
//         photos.forEach((photo) => {
//             const { title, url, thumbnailUrl } = photo;
//             photoInfo(title, url, thumbnailUrl);
//         });
//     });

// function photoInfo(title, url, thumbnailUrl) {
//     console.log(
//         `타이틀: ${title}${"\n\n"}url: ${url}${"\n\n"}thumbnailUrl: ${thumbnailUrl}${"\n\n"}`
//     );
// }

// fetch("https://jsonplaceholder.typicode.com/todos")
//     .then((response) => response.json())
//     .then((todos) => {
//         todos.forEach((todo) => {
//             const { id, title, completed } = todo;
//             todoInfo(id, title, completed);
//         });
//     });

// function todoInfo(id, title, completed) {
//     console.log(
//         `id: ${id}${"\n\n"}title: ${title}${"\n\n"}completed: ${completed}${"\n\n"}`
//     );
// }

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
