from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from datetime import datetime,date
import time
import subprocess


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  "sqlite:///example.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# db.init_app(app)

class Job(db.Model):
    # __tablename__ = 'job'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), primary_key=True)
    # statuses = db.relationship('Job_Status', backref='job', lazy=True)

class Job_Status(db.Model):
    # __tablename__ = 'job_status'
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    date = db.Column(db.Date)
    start_time = db.Column(db.String(100), nullable=False)
    end_time = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"Job Status ID: {self.id}, Status: {self.status}"
    

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        selected_file = request.form.get('menu')
        option_id = request.form.get("option_id")
        file_name = request.form.get("option_text")
        datetime_obj = datetime.now()
        dt = datetime_obj.date()
        start = time.time()
        human_readable = time.ctime(start)
        human_readable_st = human_readable[11:19]
        result = subprocess.run([f"python", "Folder/%s" % selected_file], capture_output=True, text=True)
        if result.returncode == 0:
         stat = "Success"
        else:
         stat = "Fail"
        
        end = time.time()
        human_readable = time.ctime(end)
        human_readable_en = human_readable[11:19]
        dur = round(end-start, 2)

       # Save to Job table
        job = Job(id=option_id, name=file_name)
        db.session.add(job)
        db.session.commit()

        # Save to Job_Status table
        job_status = Job_Status(id=option_id, date=dt, start_time=human_readable_st, end_time=human_readable_en,
                                duration=dur, status=stat)
        db.session.add(job_status)
        db.session.commit()

        # Query all Job_Status records ordered by end_time
        all_jobs = db.session.query(Job_Status).join(Job).order_by(desc(Job_Status.end_time)).all()

        return render_template('home.html', all_jobs=all_jobs)
    else:
        # Query all Job_Status records ordered by end_time
        all_jobs = db.session.query(Job_Status).join(Job).order_by(desc(Job_Status.end_time)).all()
        return render_template('home.html', all_jobs=all_jobs)







         
         




        # return f"Selected ID: {option_id}, File Name: {selected_file}, File: {file_name}"

        # job = Job_Status()
        # result = db.session.execute(db.select(Job_Status).order_by(Job_Status.sno)) # Get selected value
    #     return f"Selected ID: {option_id}, File Name: {selected_file}, File: {file_name} ,Date:{dt}  ,Start: {human_readable_st}, End: {human_readable_en},Duration:{dur}, Status: {stat}"

    # else:
    #     return render_template('home.html')





#         Job_Status = Job_Status(title = title,desc = desc)
#         db.session.add(Job_Status)
#         db.session.commit()
#         result = db.session.execute(db.select(Job_Status).order_by(Job_Status.sno))
#         alltodo = result.scalars()
#         return render_template('index.html', alltodo=alltodo)
#     else:
#         # Handle GET request
#         alltodo = Job_Status.query.all()  # Fetch all todos
#         return render_template('index.html', alltodo=alltodo)

    
# @app.route('/update/<int:sno>', methods=['GET', 'POST'])
# def update(sno):

#    if request.method == 'POST':
#      # Get form data
#     title = request.form.get('title')
#     desc = request.form.get('desc')

#     # Find the Job_Status item
#     Job_Status = Job_Status.query.filter_by(sno=sno).first()
#     if not Job_Status:
#         print(f"No Job_Status found with sno: {sno}")
#         return "Error: Job_Status not found", 404

#     # Update fields
#     print(f"Updating Job_Status {sno}: {Job_Status.title} -> {title}, {Job_Status.desc} -> {desc}")
#     Job_Status.title = title
#     Job_Status.desc = desc

#     # Commit changes
#     db.session.commit()
#     print("Job_Status updated successfully!")

#     return redirect("/")
   
#    else:
    
#     Job_Status = Job_Status.query.filter_by(sno=sno).first()
#     return render_template('update.html', Job_Status=Job_Status)

    



# @app.route('/delete/<int:sno>')
# def delete(sno):
#     Job_Status = db.get_or_404(Job_Status, sno)
#     db.session.delete(Job_Status)
#     db.session.commit()
#     print(f"Sucessfully Deleted {Job_Status.sno}")
#     return redirect(url_for('home'))



if __name__ == "__main__":
    with app.app_context():
       db.create_all()

    app.run(debug=True)
 