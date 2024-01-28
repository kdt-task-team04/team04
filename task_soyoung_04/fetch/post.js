fetch('https://jsonplaceholder.typicode.com/posts')
  .then(response => response.json())
  .then(posts => {
    // userId가 1인 게시물의 title만을 추출하여 배열에 저장
    const filteredPosts = posts.filter(post => post.userId === 1)
        .map(post => {
            const {title} = post
            test(title);
        });

  })

function test(title) {
    console.log(title);
}
