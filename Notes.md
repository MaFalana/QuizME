# Notes

## Backend

Password hashing
 additional features you'd like to incorporate, such as study analytics, progress tracking, and social interactions between users.

### Class/Objects


- **Database Manager**
    * **Properties:**
        * **id:** String
        * **host:** String

    * **Methods:**
        * **openConnection:** Void
        * **closeConnection:** Void
        * **addUser:** Void
        * **editUser:** Void
        * **findUser:** Void
        * **deleteUser:** Void , deletes/removes account from DB


- **User**
    * **Properties:**
        * **id:** String
        * **firstName:** String
        * **lastName:** String
        * **displayName:** String
        * **email:** String
        * **password:** String
        * **Study Buddies:** Array<String>

    * **Methods:**
        * **editDisplay** Void
        * **editEmail:** Void
        * **editPassword:** Void
        * **addBuddy:** Void
        * **removeBuddy:** Void


- **Library**
    * **Properties:**
        * **Study Sets:** Array<String>

    * **Methods:**
        * **createStudySet** Void
        * **editStudySet** Void
        * **removeStudySet** Void  


- **Study Set** //Json format
    * **Properties:**
        * **Flashcards:** Array<Flashcard>

    * **Methods:**
        * **addFlashcard** Void
        * **editFlashcard** Void
        * **removeFlashcard** Void
        * **Study** Void       



- **Flashcard**
    * **Properties:**
        * **Question:** String //Should be able to choose what is on each side, like an audio snippet, image or string of text
        * **Answer:** String

    * **Methods:**
        * **addFlashcard** Void
        * **editFlashcard** Void
        * **removeFlashcard** Void    
