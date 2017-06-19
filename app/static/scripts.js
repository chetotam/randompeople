//'use strict'
// TODO: refactor this

createListItem = function(list, name) {
    let li = document.createElement('li');
    let article = document.createElement('article');
    article.innerHTML = '<h2>' + name + '</h2>'
    li.appendChild(article);

    list.appendChild(li);
}

updateList = function(list) {
    fetch('/api/v1/rooms/test/members/', {
	    method: 'get'
    }).then((response) => {
        return response.json();
    }).then((members) => {
        members.forEach((member) => {
            createListItem(list, member.name)
        });
    }).catch(function(error) {
	    alert(error);
    });
}

document.addEventListener("DOMContentLoaded", (event) => {

    let listMembers = document.querySelector('#members-list');
    let listWinners = document.querySelector('#winners-list');
    let addMemberForm = document.querySelector('#add-member-form');
    let selectWinnersButton = document.querySelector('#select-winners-button');

    selectWinnersButton.addEventListener('click', (event) => {
        fetch('/api/v1/rooms/test/members/?random=3', {
	        method: 'get',
        }).then((response) => {
            //alert(response.status)
            return response.json();
        }).then((winners) => {
            listWinners.innerHTML='';
            winners.forEach((member) => {
                createListItem(listWinners, member.name);
        });
        }).catch((error) => {
	        alert(error);
        });
    })

    addMemberForm.addEventListener('submit', (event) => {
        event.preventDefault();
        fetch('/api/v1/rooms/test/members/', {
	        method: 'post',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
		        name: event.target.elements['name'].value
	        })
        }).then((response) => {
            if (response.status != 409) {
                newMember = response.json()
                createListItem(listMembers, newMember.name)
            }
        }).catch((error) => {
	        alert(error);
        });
    })

    updateList(listMembers);
});