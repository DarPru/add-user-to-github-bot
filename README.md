# Add user to repos

This telegram bot allows you to add users to github repos. Simply tag it in private chart or group and than set a list of repos you need to be added.

By default it has permission to write, but you can change it for any other one. 

````
@allow_my_id_to_github_bot my-repo-1 my-repo-2 my-new-repo
````

## Features

- **Admin notification** - You may put the telegram username of person who would be an administrator to **ADMIN** var. In this case administrator will be notified.
- **Restricted access** - Only people included in the user list can be added to your repos.
- **Typo protection** - You may put extra spaces between repo's name or write them at the new line, at the and you will have a clear list of repos's names.


## Don't forget

- to include libs:

````
pip install requests
pip install aiogram
````

- to add allowed users
