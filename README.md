### **1.** First of all you need to clone this repository
```python3
git clone https://github.com/karynabarkhatova/django-website.git
```
### **2.** Second step is installing a virtual environment
```python3
python3 -m venv venv
```
### **3.** Now you need to activate your virtual environment
```python3
source venv/bin/activate
```
### **4.** Install the pack of files from requirements.txt
```python3
pip install -r requirements.txt
```
### Now open a foulder "blog" where the manage.py file is set and run the program
```python3
./manage.py runserver
```
### To see the results you will need to open local host in your browser ###
```
http://127.0.0.1:8000
```
### Change the path to each of these to see if the program works right:
#### Here's admin page
```
http://127.0.0.1:8000/admin
```
#### And there are each page of the website
```
http://127.0.0.1:8000/
http://127.0.0.1:8000/about
http://127.0.0.1:8000/contact
```
### The data which you write into the contact form (/contact/) will be sent to the database, also you can check it in admin panel (/admin/)
