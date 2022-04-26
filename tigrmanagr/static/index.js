// CREATE

// CREATETODO
function createTodo(board_id) {
    var todo_title = document.getElementById("todoTitle").value;
    var board_id = document.getElementById("boardID").innerHTML;
    
    axios({
        method: "POST",
        url: "/board/" + board_id +"/create",
        data: {
            todo_title: todo_title,
            board_id: board_id
        },
        headers: {
            "Content-Type": "application/json",
        }
    }).then(
        (response) => {
            var data = response.data;
            if (data.redirect) {
                window.location.href = data.redirect;
            }
                                                        
            if (data.status == 500) {
                alert(data.error);
                window.location.href = "/";
            }
        },
    )
}

// CREATE BOARD

function createBoard() {
    var board_name = document.getElementById("boardTitle").value;
    
    axios({
        method: "POST",
        url: "/board/create",
        data: {
            board_name: board_name
        },
        headers: {
            "Content-Type": "application/json",
        }
    }).then(
        (response) => {
            var data = response.data;
            if (data.redirect) {
                window.location.href = data.redirect;
            }
                                                        
            if (data.status == 500) {
                alert(data.error);
                window.location.href = "/";
            }
        },
    )
}

//EDIT TODO

function updateTodo(todo_id){
    var title_update = document.getElementById("todoEdit").value;
    var status_update = document.getElementById("status").innerHTML;

    if (status_update == 'Todo'){
        status_update = 0
    }else if(status_update == 'Doing'){
        status_update = 1
    }else{
        status_update = 2
    }

    axios({
        method: "POST",
        url: "/todo/edit/"+todo_id,
        data: {
            todo_id: todo_id,
            title_update: title_update,
            status_update: status_update
        },
        headers: {
            "Content-Type": "application/json",
        }
    }).then(
        (response) => {
            var data = response.data;
            if (data.redirect) {
                window.location.href = data.redirect;
            }

            if (data.status == 500) {
                alert(data.error);
                window.location.href = "/";
            }
        },
    )
}

function statusChange(status){

    if (status == 'Todo'){
        document.getElementById('status').innerHTML = 'Doing'
    }else if(status == 'Doing'){
        document.getElementById('status').innerHTML = 'Done'
    }else{
        document.getElementById('status').innerHTML = 'Todo'
    }
}

//EDIT BOARD

function updateBoard(board_id){
    var name_update = document.getElementById("boardEdit").value; 

    axios({
        method: "POST",
        url: "/board/edit/" + board_id,
        data: {
            board_id: board_id,
            name_update: name_update 
        },
        headers: {
            "Content-Type": "application/json",
        }
    }).then(
        (response) => {
            var data = response.data;
            if (data.redirect) {
                window.location.href = data.redirect;
            }

            if (data.status == 500) {
                alert(data.error);
                window.location.href = "/";
            }
        },
    )
}

//DELETE

// DELETE TODO
function deleteTodo(todo_id, todo_title) {
    var message = "Are you sure you want to delete Todo with title " + todo_title + " ?";
    var confirm_delete = confirm(message);

    if (confirm_delete == true) {
        var url = "/todo/delete/" + todo_id;
        axios({
            method: "POST",
            url: url,
        }).then(
            (response) => {
                var data = response.data;
                if (data.redirect) {
                    window.location.href = data.redirect;                        
                }
            }
        );
    }
}

// DELETE BOARD
function deleteBoard(board_id, board_name) {
    var message = "Are you sure you want to delete Board with title " + board_name + " ?";
    var confirm_delete = confirm(message);

    if (confirm_delete == true) {
        var url = "/board/delete/" + board_id;
        axios({
            method: "POST",
            url: url,
        }).then(
            (response) => {
                var data = response.data;
                if (data.redirect) {
                    window.location.href = data.redirect;                        
                }
            }
        );
    }
}

