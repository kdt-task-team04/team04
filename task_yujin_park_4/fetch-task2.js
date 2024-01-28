// https://jsonplaceholder.typicode.com/users

// fetch("https://jsonplaceholder.typicode.com/users")
//     .then((response) => response.json())
//     .then((users) => {
//         users.forEach((user) => {
//             const { zipcode } = user.address;
//             console.log(zipcode);
//         });
//     });

// fetch("https://jsonplaceholder.typicode.com/albums")
//     .then((response) => response.json())
//     .then((albums) => {
//         console.log(albums);
//     });

// fetch("https://jsonplaceholder.typicode.com/albums")
// .then((response) => response.json())
// .then((albums) => {
//     albums.forEach((album) => {
//         const{title} = album;
//         console.log(title);

//     });
// });

// fetch("https://jsonplaceholder.typicode.com/comments")
//     .then((response) => response.json())
//     .then((comments) => {
//         comments.forEach((comment) => {
//             const { email } = comment;
//             console.log(email);
//         });
//     });

// fetch("https://jsonplaceholder.typicode.com/users")
//     .then((response) => response.json())
//     .then((users) => {
//         users.forEach((user) => {
//             const { geo } = user.address;
//             console.log(geo);
//         });
//     });

// fetch("https://jsonplaceholder.typicode.com/users")
//     .then((response) => response.json())
//     .then((users) => {
//         users.forEach((user) => {
//             const { lat } = user.address.geo;
//             console.log(lat);
//         });
//     });

fetch("https://jsonplaceholder.typicode.com/users")
    .then((response) => response.json())
    .then((users) => {
        users.forEach((user) => {
            const { lng } = user.address.geo;
            console.log(lng);
        });
    });
