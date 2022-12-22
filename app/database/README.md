<h1>Documentation</h1>

## Index
* [How to add new videos to be uploaded](#how-to-add-new-videos-to-be-uploaded)
* [Files](#files)
* [Folders](#folders)

## How to add new videos to be uploaded
The process is very simple, just move your favorite video to "videos" folder.

## Files
`identify.py`
Create selenium connection.

`tikbot_db`
Local database whose store informations from identities.

Informations from tikbot_db
Type: sqlite3
Tables: ACCOUNTS
Structure: 
        ACCOUNT_ID INTERGER PRIMAR KEY,
        ACCOUNT_NAME TEXT PRIMAR KEY,
        COOKIES ARRAY

`setup.py`
Create and configure local database.
       

## Folders
`videos`
Store videos to be uploaded