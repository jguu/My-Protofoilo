from flask import Flask,render_template,request,url_for
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')
    

@app.route('/<string:page_name>')
def hmtl_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')
        
def write_to_csv(data):
    with open('database.csv',newline='',mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        file.writerow([email,subject,message])
    
@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict();
        write_to_file(data)
        write_to_csv(data)
        print(data)
        return render_template('thanks.html')
    else:
        return 'Something went wrong'
    
