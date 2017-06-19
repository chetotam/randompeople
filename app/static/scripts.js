//'use strict'
// TODO: refactor this

createListItem = function(list, name) {
    let liseItemTemplate = document.querySelector('#members-list-item-template');
    let listItem = document.importNode(liseItemTemplate.content, true);
    listItem.querySelector('.member-name').innerHTML = name;

    list.appendChild(listItem);
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
    });

    addMemberForm.addEventListener('submit', (event) => {
        event.preventDefault();
        fetch('/api/v1/rooms/test/members/', {
	        method: 'post',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
		        name: event.target.elements['name'].value.trim()
	        })
        }).then((response) => {
            if (response.status != 409) {
                return response.json()
            }
            return null
        }).then((newMember) => {
            if (newMember) {
                createListItem(listMembers, newMember.name)
            }
        }).catch((error) => {
	        alert(error);
        });
    });

    listMembers.addEventListener('click', (event) => {
        if (event.target.tagName == 'BUTTON') {
            let listEntry = event.target.closest('li');
            name = listEntry.querySelector('.member-name').innerHTML;
            
            fetch('/api/v1/rooms/test/members/' + name, {
	            method: 'delete'
            }).then((response) => {
                if (response.status === 204) {
                    listEntry.setAttribute('hidden', true);
                }
            }).catch(function(error) {
	            alert(error);
            });
        }
    });

    updateList(listMembers);
});