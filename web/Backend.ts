/**************************************
 TITLE: portfolio.js							
 AUTHOR: Malik Falana (MF)			
 CREATE DATE: 06/23/2023	
 PURPOSE: To use jquery and functions for portfolio page
 LAST MODIFIED ON: 06/23/2023	
 LAST MODIFIED BY: Malik Falana (MF)
 MODIFICATION HISTORY:
 06/23/2023: Original Build
***************************************/


class User
{
    firstName: string;
    lastName: string;
    email: string;
    password: string;

    constructor(firstName: string, lastName: string, displayName: string, email: string, password: string)
    {
        this.firstName = firstName;
        this.lastName = lastName;
        this.displayName = displayName;
        this.email = email;
        this.password = password;
    }

    function changePassword(previousPassword: string) : void //Function to change password
    {
        if (previousPassword == this.password)
        {
            //Change password
        }
        else
        {
            //Display error message
        }
    }

    function changeEmail(previousEmail: string) : void //Function to change email
    {
        if (previousEmail == this.email)
        {
            //Change email
        }
        else
        {
            //Display error message
        }
    }

    function changeDisplayName(previousDisplayName: string) : void //Function to change display name
    {
        if (previousDisplayName == this.displayName)
        {
            //Change display name
        }
        else
        {
            //Display error message
        }
    }

    function verifyPassword(password: string) : boolean //Function to verify password
    {
        if (password == this.password)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    function verifyEmail(email: string) : boolean //Function to verify email
    {
        if (email == this.email)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    function verifyDisplayName(displayName: string) : boolean //Function to verify display name
    {
        //Check if display name is taken
        //Make a request to DB to check if display name is taken
        // return boolean
        if (displayName == this.displayName)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

   
}

