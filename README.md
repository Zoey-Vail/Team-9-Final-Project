# Instructions to install and run

1. Download the zip file from the github page
2. Unzip the file and navigate to the `Team-9-Final-Project-main` folder in VS Code
3. Run the command `virtualenv env` in the terminal
4. In the terminal run `cd env`, then `cd Scripts`, then `. Activate` 
5. Navigate back to the `Team-9-Final-Project-main` folder
6. Run `pip install -r requirements.txt`
7. In the `app.py` file, on line 7, where it says `PASSWORDCHANGEHERE`, replace that with your mySQL password
8. Open mySQL workbench and navigate to the root connection
9. In the schemas tab on the left, right click and select `Create Schema`
10. Name the Schema `accounts`, the click `Apply`, then `Apply`, and then `Finish`
11. Open the `account_list.sql` and click the lightning bolt to run
12. In VS Code, run `python app.py` in the terminal, then navigate to the `http://127.0.0.1:5000/` to view the webpage
