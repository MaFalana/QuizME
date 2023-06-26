- **Login Page**
    * **Description:** The login page allows users to login to their account. Users can enter their email address and password, and click on the "Log In" button to submit the login form. If the login information is valid, the user will be redirected to the dashboard page.
    * **URL:** `/login`
    * **Methods:** `GET`, `POST`
    * **Request Body:** 
        * **email:** String
        * **password:** String
    * **Response Body:** 
        * **user:** User
    * **Status Codes:** 
        * `200` - OK
        * `400` - Bad Request
        * `401` - Unauthorized
        * `500` - Internal Server Error
    * **Example:** 
        * **Request:** `POST /login`
        * **Response:** `200 OK`
        * **Body:** 
            ```
            {
                "email": "