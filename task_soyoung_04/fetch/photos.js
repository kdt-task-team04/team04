fetch("https://jsonplaceholder.typicode.com/photos")
    .then((response) => response.json())
    .then((photos) => {
        photos.forEach((photo) => {
            const {thumbnailUrl} = photo
            const {url} = photo
            test(thumbnailUrl, url);
        })
})

function test(...rest) {
    console.log(...rest)
}