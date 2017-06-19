# randompeople
so random, very people

Get some at https://randompeople.herokuapp.com/

API:

GET /api/v1/rooms/<room_name> - get room by name (rooms are groups of people to choose from)
GET /api/v1/rooms/ - get all rooms
POST /api/v1/rooms/ {name: <room_name>} - create new room (name should be room_name)
DELETE /api/v1/rooms/<room_name> - delete room by name
DELETE /api/v1/rooms/ - delete all rooms

GET /api/v1/rooms/<room_name>/members/<member_name> - get member by name of specified room
GET /api/v1/rooms/<room_name>/members/ - get all members of specified room
POST /api/v1/rooms/<room_name>/members/ {name: <member_name>} - add new member to specified room (member_name should be unique)
DELETE /api/v1/rooms/<room_name>/members/<member_name> - delete member by name from specified room
DELETE /api/v1/rooms/<room_name>/members/ - delete all members of specified room
