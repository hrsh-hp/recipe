const heartIcons = document.querySelectorAll('.heart-icon');
const likeCounts = document.querySelectorAll('.like-count');
console.log(likeCounts.innerText);
    heartIcons.forEach(icon => {
        // likeCounts.forEach(count=>{
            icon.addEventListener('click', function() {
                
                const slug = this.dataset.slug;

                const isLiked = this.classList.contains('fa-heart');
                console.log(isLiked)
                console.log(JSON.stringify({ 'slug': slug }));
                fetch(path+'?slug='+slug )
                .then(response => response.json())
                .then(data => {
                    if (data.success){
                        if (isLiked) {
                            this.classList.remove('fa-heart');
                            this.classList.add('fa-heart-o');
                        } else {
                            this.classList.remove('fa-heart-o');
                            this.classList.add('fa-heart');
                        }
                        
                            count.innerText = data.likes;
                    
                        console.log(data.items);
                    } else {
                        alert(data.message);
                    }
                })
                .catch(error =>  {
                    console.log(error)
                })
                
            });
        // });


    });