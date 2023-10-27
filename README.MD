# REST API with FastAPI and MongoDB !

This is a simple REST API built using FastAPI and MongoDB.

## API Documentation

The API is documented using OpenAPI (formerly known as Swagger). You can find the OpenAPI specification in the [swagger.json](swagger.json) file.

## Endpoints

### Get All Users

- **Endpoint**: `/users`
- **Method**: GET
- **Description**: Retrieve a list of all users.
- **Response**: Returns a JSON array of user objects.

### Create User

- **Endpoint**: `/users`
- **Method**: POST
- **Description**: Create a new user.
- **Request Body**: Expects a JSON object with user details.
- **Response**: Returns the created user as a JSON object.

### Get User by ID

- **Endpoint**: `/users/{id}`
- **Method**: GET
- **Description**: Retrieve a user by their ID.
- **Parameters**: `id` (path) - The ID of the user.
- **Response**: Returns a JSON object representing the user.

### Update User

- **Endpoint**: `/users/{id}`
- **Method**: PUT
- **Description**: Update an existing user by their ID.
- **Parameters**: `id` (path) - The ID of the user.
- **Request Body**: Expects a JSON object with user details.
- **Response**: Returns the updated user as a JSON object.

### Delete User

- **Endpoint**: `/users/{id}`
- **Method**: DELETE
- **Description**: Delete a user by their ID.
- **Parameters**: `id` (path) - The ID of the user.
- **Response**: Returns a 204 No Content response on success.

## Version

- **Version**: 0.0.1

## Author

- **Author**: [Joseandres Montesino]



## Installation

To run this API, you'll need to have FastAPI and MongoDB set up. Please refer to the API documentation for more details.
```bash
pip install -r requirements.txt
```

## Running the API

You can run the API with the following command:

```bash
uvicorn main:app --reload
