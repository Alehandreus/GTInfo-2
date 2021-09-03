function delete_user(id) {
    var user_block = document.getElementById("block-"+id);
    user_block.remove();
    var csrf_token_value = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/tracking_settings_delete_user/');
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
        if (xhr.status === 200) {
            console.log(xhr.responseText);
        }
        else {
            console.log('Request failed.  Returned status of ' + xhr.status);
        }
    };
    xhr.send(encodeURI('id='+id+'&csrfmiddlewaretoken='+csrf_token_value));
}

function add_user(id) {
    var html_block = '<div class="row m-4 justify-content-between align-items-center" id="block-'+id+'">'+
        '<div class="col-3 justify-content-center align-items-center text-center">'+
            '<p class="fs-4" id="'+id+'">'+id+'</p>'+
        '</div>'+
        '<div class="col-3 justify-content-center align-items-center text-center">'+
            '<button type="button" class="btn btn-primary" onclick="delete_user('+id+')"><i class="fas fa-minus"></i></button>'+
        '</div>'+
    '</div>';
    var add_button = '<div class="row m-4" id="add-button"><button type="button" class="btn btn-light" data-mdb-toggle="modal" data-mdb-target="#addUserModal"><i class="fas fa-plus"></i></button></div>';
    var csrf_token_value = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/tracking_settings_add_user/');
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
        if (xhr.status === 200) {
            console.log(xhr.responseText);
            var tracked_list = document.getElementById("tracked-list");
            document.getElementById("add-button").remove();
            tracked_list.innerHTML += html_block;
            tracked_list.innerHTML += add_button;
        }
        else {
            console.log('Request failed.  Returned status of ' + xhr.status);
            if (JSON.parse(xhr.responseText).status == "TooManyUsers") {
                var tooManyUsersModal = document.getElementById('tooManyUsersModal');
                var modal = new mdb.Modal(tooManyUsersModal);
                modal.show();
            } else if (JSON.parse(xhr.responseText).status == "InvalidID") {
                var invalidIDModal = document.getElementById('invalidIDModal');
                var modal = new mdb.Modal(invalidIDModal);
                modal.show();
            } else if (JSON.parse(xhr.responseText).status == "PrivateProfile") {
                var privateProfileModal = document.getElementById('privateProfileModal');
                var modal = new mdb.Modal(privateProfileModal);
                modal.show();
            } else if (JSON.parse(xhr.responseText).status == "UserAlreadyAdded") {
                var userAlreadyAddedModal = document.getElementById('userAlreadyAddedModal');
                var modal = new mdb.Modal(userAlreadyAddedModal);
                modal.show();
            }
        }
    };
    xhr.send(encodeURI('id='+id+'&csrfmiddlewaretoken='+csrf_token_value));
}

const addUserModal = document.getElementById('addUserModal');
const modal2 = new mdb.Modal(addUserModal);

function add_user_modal_function() {
    add_user(document.getElementsByName("steam-id-modal")[0].value);
    document.getElementsByName("steam-id-modal")[0].value = '';
    modal2.hide();
}