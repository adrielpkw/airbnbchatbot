1. Install XAMPP
2. Install Python
3. Extract System Files folder from the zip
4. Open command prompt as admin and run the following commands at your command prompt: 
cd /path/to/your/extracted/System Files
cd All source files
chatbot_env\Scripts\activate
pip install -r requirements.txt
python preprocessmethods.py

5. Edit the preprocessmethods.py file and remove the code "nltk.download("all")" at line 9 after running the preprocessmethods.py earlier at step 4.

6. Click start at Apache and MySQL modules on XAMPP and click Admin, click import tab and choose user-system.sql. Then scroll all the way down and click import.
7. Run the following command at command prompt:
flask --app app --debug run


8. Once it says "Debugger is active!", go to http://127.0.0.1:5000 on your browser and login with:
test1@gmail.com
password: 12345

Or
test2@gmail.com
password: 12345

test3@gmail.com
password: 12345

9. Enjoy using


To run and retrieve the results of every SVM or MNB models (such as ENSVM.py, ENMNB.py and others):

Uncomment the code below to get the classification report.

print(classification_report(Y_test, Y_pred_label, zero_division = 0))

1. Open command prompt as admin and run the following commands at your command prompt:
cd /path/to/your/extracted/System Files
cd Process Files
chatbot_env\Scripts\activate
pip install -r requirements.txt
python preprocessmethods.py

2. Edit the preprocessmethods.py file and remove the code "nltk.download("all")" at line 9 after running the preprocessmethods.py earlier.

3. Run this command: python filename.py 

***the filename can be ENSVM/ENMNB/BMSVM/BMMNB/CNSVM/CNMNB***



For contact:

19027531@imail.sunway.edu.my OR
adrielpkw19@gmail.com