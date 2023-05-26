let btns = document.getElementsByClassName('button-check')
console.log('hello world')

for(let i = 0; i < btns.length; i++){
    btns[i].addEventListener('click', () => {
        let buttonAction = btns[i].dataset.action
        let postId = btns[i].dataset.post
        let userId = btns[i].dataset.user

        if(buttonAction == 'delete'){
            Swal.fire({
                title: 'Are you sure?',
                text: "You won't be able to revert this!",
                icon: 'warning',
                showCancelButton: true,
                allowOutsideClick: false,
                allowEscapeKey: false,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Yes, delete it!'
              }).then((result) => {
                if (result.isConfirmed) {
                  Swal.fire(
                    'Deleted!',
                    'Your file has been deleted.',
                    'success'
                  )
                  sendData(buttonAction, postId, userId)
                }
              })

        } else{
            sendData(buttonAction, postId, userId)
        }
    })
}

const sendData = function(action, post, user){

    let url = 'post_action'

    fetch(url, {
        method:'POST',
        headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": csrfToken},
        body: JSON.stringify({'action': action, 'post': post, 'user': user})
        })
    
    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data', data)
    })

}

// To comment option
let commentButton = document.getElementsByClassName('comment-post')
let commentDiv = document.getElementsByClassName('comment-section')

for(let i = 0; i < commentButton.length; i++){
    commentButton[i].addEventListener('click', () => {
        commentDiv[i].classList.remove('hidden')
    })
}

// To delete a comment.
let commentInteract = document.getElementsByClassName('comments-buttons')

for(let i = 0; i < commentInteract.length; i++){
    commentInteract[i].addEventListener('click', () =>{
        let dataAction = commentInteract[i].dataset.action
        let commentID = commentInteract[i].dataset.comment
        let userID = commentInteract[i].dataset.user
        sendCommentData(dataAction,commentID, userID)

    })
}


const sendCommentData = (dataAction, commentID, userID) => {

    url = 'comment_action'

    fetch(url,{
        method : 'POST',

        headers: {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrfToken},

        body: JSON.stringify({'action': dataAction, 'commentID':commentID, 'userID':userID})
    }
    )

    .then((response) => {
        return response.json()
    })

    .then((data) =>{
        console.log('data:',data)
    })
}

let likeButton = document.getElementsByClassName('favorite-button')

window.addEventListener('load', ()=>{
    for (let i = 0; i < likeButton.length; i++){
        if (likeButton[i].dataset.active == "True"){
            let favoriteImg = document.getElementsByClassName('favorite-icon')
            favoriteImg[i].classList.remove('material-symbols-outlined')
            favoriteImg[i].innerHTML = "<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Heart_coraz%C3%B3n.svg/640px-Heart_coraz%C3%B3n.svg.png' width='23'>"
        }
    }
})
