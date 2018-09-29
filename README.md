# website-blocker
This python script blocks user specified websites between user specified hours.

### Steps to use website blocker script
1. First list the websites (one per line) to be blocked in a file named “blocking_list.txt”. Refer sample file.

2. Set the variable `path_to_blocking_list_file` in the script to full path of folder containing “blocking_list.txt”.

3. Change the variables `start_hour` and `end_hour` in the script as required. Use 24 hour format.

4. Go to Task scheduler.

5. Click on “Create Task…”. In the General tab, enter the name for the task. And don’t forget to check “Run with highest privileges” since we want to run this file with administrator rights.

6. Go to Triggers tab. Click on “New…” and in the “Begin the task” list, choose “At log on”.

7. Now, go to Actions tab and click on “New…”. Select an action “Start a program” and write “`pythonw <path_of_website_blocker_script>`” in the program/script text box.

8. Now, go to Conditions tab and check/uncheck any conditions as per your preference. (In this case, you can uncheck “Start the task only if the computer is on AC power” because you may want to run your python script even when the laptop is running on battery.)

9. Now, just click OK and it’s done.

10. Now, whenever you start your computer, website blocker will start working. It will block the listed websites during specified hours.