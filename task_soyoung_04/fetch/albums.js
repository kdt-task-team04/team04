fetch("https://jsonplaceholder.typicode.com/albums")
    .then((response) => response.json())
    .then((albums) => {
        albums.forEach((album) => {
            const {title} = album
            test(title);
        })
})

function test(title) {
    console.log(title)
}