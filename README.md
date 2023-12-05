# WhatsAppApiServer

## Cloning and starting project
1. - git clone https://github.com/esubalew-gosaye/ChatRoom.git
2. - cd WhatsAppApiServer
3. - pip install -r requirements.txt
4. - python manage.py runserver
# Chat API Documentation

## Login

**Endpoint:** `POST /login`

**Description:** Logs in a user and assigns a session.

**Parameters:**
- `username` (string, required): The username of the user.
- `password` (string, required): The password of the user.

**Response:**
- `user_id` (integer): ID of the logged-in user.
- `message` (string): Confirmation message.

## Logout

**Endpoint:** `GET /logout`

**Description:** Logs out the currently logged-in user.

**Response:**
- `message` (string): Logout confirmation message.

## Create User

**Endpoint:** `POST /create_user`

**Description:** Creates a new user and logs them in.

**Parameters:**
- `username` (string, required): The username for the new user.
- `password` (string, required): The password for the new user.

**Response:**
- `info` (string): Information message.
  
## Get Users

**Endpoint:** `GET /get_users`

**Description:** Retrieves a list of all users.

**Response:**
- `users` (array): List of users, each containing `user_id` and `username`.

## Create Room

**Endpoint:** `POST /create_room`

**Description:** Creates a new chat room.

**Parameters:**
- `room` (string, required): The name of the new room.

**Response:**
- `room_id` (integer): ID of the created room.
- `room_name` (string): Name of the created room.

## Get Rooms

**Endpoint:** `GET /get_rooms`

**Description:** Retrieves a list of all chat rooms.

**Response:**
- `rooms` (array): List of rooms, each containing `room_id` and `room_name`.

## Join Room

**Endpoint:** `POST /join_room`

**Description:** Joins a user to a chat room.

**Parameters:**
- `room` (string, required): The name of the room to join.

**Response:**
- `message` (string): Confirmation message.

## Send Message

**Endpoint:** `POST /send_message`

**Description:** Sends a message in the current chat room.

**Parameters:**
- `Note` This is implemented in frontend part select Room and user first.
- use `connect` Button to connect with socket and type your message then `enter`
- All your change is reflected to our database

**Response:**
- `message` (string): The message you entered.

## List Messages

**Endpoint:** `POST /list_message`

**Description:** Lists all messages in a specific chat room.

**Parameters:**
- `room` (string, required): The name of the room to list messages for.

**Response:**
- `room` (string): Name of the room.
- `messages` (array): List of messages, each containing `username`, `message`, and `timestamp`.

---

**Note:** Replace `localhost:8000` in the WebSocket URLs with the appropriate domain and port based on your server configuration.
