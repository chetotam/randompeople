# randompeople
so random, very people

Get some at https://randompeople.herokuapp.com/

API (/api/v1):

GET /rooms/<room_name> - get room by name (rooms are groups of people to choose from)

GET /rooms/ - get all rooms

POST /rooms/ {name: <room_name>} - create new room (name should be room_name)

DELETE /rooms/<room_name> - delete room by name

DELETE /rooms/ - delete all rooms


GET /rooms/<room_name>/members/<member_name> - get member by name of specified room

GET /rooms/<room_name>/members/ - get all members of specified room

POST /rooms/<room_name>/members/ {name: <member_name>} - add new member to specified room (member_name should be unique)

DELETE /rooms/<room_name>/members/<member_name> - delete member by name from specified room

DELETE /rooms/<room_name>/members/ - delete all members of specified room
