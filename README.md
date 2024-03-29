# 1-1-call-management
Hey there! This repository gives you all the tools you need to run 1-1s successfully.
To start, install the SQLite3 library by pasting and running "pip install sqlite3" in your VS code console.
Then download all the files.
Then run "create_names_table.py" and "create_pairing_table.py". Please don't change the names of the tables, because then further editing would be necessary. Just run the two as they are. The first script creates a table called usernames which stores the names of the people signed up, and the second script records pairings to avoid repetition. 
Then add the usernames of the people signed up to "add_names.py" (I have left a comment, which is "#here", at all editable places).
Once you have added all the names, go to "pairing_generator.py". In case the number of people signed up before a pairing is odd, I have made an arrangement in the code that evens out the number of people by assigning two partners to someone willing to attend two calls. I have marked the place where you can add this person's name with a "#here" comment (I'd be willing to do it if that's fine!). Once you do that, run the code to generate the pairings. It compares the pairings with the past pairing data to ensure no repetition of partners.
You can list all the names in your table using "count_names.py".
You can list all the past pairings using "count_pairs.py".
You can delete names from the db using "delete_names.py".
You can delete pairings from the db using "delete_pairs.py".
You can add pairs to the db using "add_pairs.py".
You can see if a particular name is in the db using "name_finder.py".
You can see if there is any repetition of names using "name_repetition_check.py".
You can operate on multiple names/pairings in every script at once.
