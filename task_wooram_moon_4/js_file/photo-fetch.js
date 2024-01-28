fetch("https://jsonplaceholder.typicode.com/photos")
    .then((response) => response.json())
    .then((comments) => {
        comments.forEach((e) => {
            const { title, thumbnailUrl } = e;
            comment(title, thumbnailUrl);
        });
    });

function comment(title, thumbnail) {
    console.log(`${"\n"} 타이틀: ${title}, ${"\n"} 썸네일: ${thumbnail}`);
}
