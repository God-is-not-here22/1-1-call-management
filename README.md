# 1-1-call-management
Hey there! This repository gives you all the tools you need to run 1-1s sucessfully.
To start, install the sqlite3 library pasting and running "pip install sqlite3" in your VS code console.
Then download all the files.
Then run "Create names table.py" and "Create pairing table.py". Please don't change the names of the tables, because then further editing would be nessecary. Just run the two as they are. The first script creates a table called usernames which stores the names of the people signed up, and the second script records pairings to avoid repitition. 
Then add the usernames of the people signed up to "Add names.py" (I have left a comment, which is "#here", at all editable places).
Once you have added all the names, go to "Pairing generator.py". Now in case the no. of people signed up before a pairing is odd, I have made an arrangement in the code that evens out the no. of people by assigning two partners to someone who is willing to attend two calls. I have marked the place where you can add the name of this person with a "#here" comment (I'd be willing to do it if that's fine!). Once you do that, run the code to generate the pairings. It compares the pairings with the past pairing data to ensure no repitition of partners.
You can list all the names in your table using "Count names.py".
You can list all the past pairings using "Count pairs.py".
You can delete names from the db using "Delete names.py".
You can delete pairings from db using "Delete pairs.py".
You can add pairs to the db using "Add pairs.py".
You can see if a particular name is in the db using "Name finder.py".
You can see if there is any repitition of names using "Name reoccurence check.py".
In every script, you can operate on multiple names/pairings at once.
