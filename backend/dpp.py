# from flask import Flask,render_template,request,redirect,url_for,jsonify
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import desc
# from datetime import datetime,date
# import time
# import subprocess


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] =  "sqlite:///newdb.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# # db.init_app(app)

# class Job(db.Model):
#     __tablename__ = 'job'
#     id = db.Column(db.Integer, primary_key=True)
#     file = db.Column(db.String(255), nullable=False)  
#     def __repr__(self):
#         return f"<Jobs {self.id} - {self.file}>"


# class Job_Status(db.Model):
#     __tablename__ = 'job__status'
#     id = db.Column(db.Integer, primary_key=True)  # Primary key
#     job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
#     playbook = db.Column(db.String(50), nullable=False)
#     date = db.Column(db.Date, nullable=False)
#     start_time = db.Column(db.String(50), nullable=False)
#     end_time = db.Column(db.String(50), nullable=False)
#     duration = db.Column(db.String(50), nullable=False)
#     status = db.Column(db.String(50), nullable=False)

#     def __repr__(self):
#         return f"<Job_Status {self.id} - {self.job_id} >"



# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         selected_file = request.form.get('menu')
#         optionid = int(request.form.get("option_id"))
#         file_name = request.form.get("option_text")
#         dt =  date.today()
#         start = time.time()
#         human_readable = time.ctime(start)
#         human_readable_st = human_readable[11:19]
        
#         # Set initial status to 'in progress'
#         stat = "In Progress"

#         # Start the task (subprocess)
#         result = subprocess.run([f"python", "Folder/%s" % selected_file], capture_output=True, text=True)
        
#         # Check the result and update the status to success or failure
#         if result.returncode == 0:
#             stat = "Success"
#         else:
#             stat = "Failure"
        
#         end = time.time()
#         human_readable = time.ctime(end)
#         human_readable_en = human_readable[11:19]
#         dur = round(end-start, 2)
        
#         # Check if the Job already exists or create a new one
#         job = Job.query.filter_by(id=optionid).first()
#         if not job:
#             job = Job(id=optionid, file=selected_file)
#             db.session.add(job)
#             db.session.commit()

#         # Create Job_Status entry with 'in progress' initially
#         all_job = Job_Status(
#             job_id=optionid,
#             playbook=file_name,
#             date=dt,
#             start_time=human_readable_st,
#             end_time=human_readable_en,
#             duration=dur,
#             status=stat
#         )
#         db.session.add(all_job)
#         db.session.commit()

#         # Query to get all job statuses (including 'in progress', 'success', 'failure')
#         all_jobs = db.session.query(Job_Status).order_by(desc(Job_Status.date), desc(Job_Status.end_time)).all()
        
#         return render_template('home.html', all_jobs=all_jobs)

#     else:
#         # Query to get all job statuses on GET request
#         all_jobs = db.session.query(Job_Status).order_by(desc(Job_Status.date), desc(Job_Status.end_time)).all()
#         return render_template('home.html', all_jobs=all_jobs)






# # @app.route('/', methods=['GET','POST'])
# # def home():
# #     if request.method == 'POST':
# #         selected_file = request.form.get('menu')
# #         optionid = int(request.form.get("option_id"))
# #         file_name = request.form.get("option_text")
# #         dt =  date.today()
# #         start = time.time()
# #         human_readable = time.ctime(start)
# #         human_readable_st = human_readable[11:19]
# #         result = subprocess.run([f"python", "Folder/%s" % selected_file], capture_output=True, text=True)
# #         if result.returncode == 0:
# #          stat = "Success"
# #         else:
# #          stat = "Fail"
        
# #         end = time.time()
# #         human_readable = time.ctime(end)
# #         human_readable_en = human_readable[11:19]
# #         dur = round(end-start, 2)
# #         # job = Job(id = option_id,file=selected_file)
# #         # db.session.add(job)
# #         # db.session.commit()

# #         # all_job = Job_Status( job_id=option_id,playbook = file_name ,date=dt,start_time = human_readable_st,end_time = human_readable_en,duration=dur,status = stat)
# #         # db.session.add(all_job)
# #         # db.session.commit()

# #         job = Job.query.filter_by(id=optionid).first()
# #         if not job:
# #             job = Job(id=optionid, file=selected_file)
# #             db.session.add(job)
# #             db.session.commit()

# #         all_job = Job_Status(
# #             job_id=optionid,
# #             playbook=file_name,
# #             date=dt,
# #             start_time=human_readable_st,
# #             end_time=human_readable_en,
# #             duration=dur,
# #             status=stat
# #         )
# #         db.session.add(all_job)
# #         db.session.commit()
# #         print(f"{optionid}  {type(optionid)}")
# #         print(request.form)
# #     #     # result = db.session.execute(db.select(Job_Status).order_by(desc(Job_Status.end_time)))
# #         all_jobs= db.session.query(Job_Status).order_by(desc(Job_Status.date), desc(Job_Status.end_time)).all()
        
# #         return render_template('home.html', all_jobs = all_jobs)

# #         return f"Selected ID: {optionid}, File Name: {selected_file}, File: {file_name} ,Date:{dt}  ,Start: {human_readable_st}, End: {human_readable_en},Duration:{dur}, Status: {stat}"

# #     else:
# #     #     # result = db.session.execute(db.select(Job_Status).order_by(desc(Job_Status.end_time)))        
# #         all_jobs= db.session.query(Job_Status).order_by(desc(Job_Status.date), desc(Job_Status.end_time)).all()
# #         return render_template('home.html',all_jobs=all_jobs)


# if __name__ == "__main__":
#     with app.app_context():
#         app.run(debug=True)
 




         
         




#         # return f"Selected ID: {option_id}, File Name: {selected_file}, File: {file_name}"

#         # job = Job_Status()
#         # result = db.session.execute(db.select(Job_Status).order_by(Job_Status.sno)) # Get selected value
#     #     return f"Selected ID: {option_id}, File Name: {selected_file}, File: {file_name} ,Date:{dt}  ,Start: {human_readable_st}, End: {human_readable_en},Duration:{dur}, Status: {stat}"

#     # else:
#     #     return render_template('home.html')





# #         Job_Status = Job_Status(title = title,desc = desc)
# #         db.session.add(Job_Status)
# #         db.session.commit()
# #         result = db.session.execute(db.select(Job_Status).order_by(Job_Status.sno))
# #         alltodo = result.scalars()
# #         return render_template('index.html', alltodo=alltodo)
# #     else:
# #         # Handle GET request
# #         alltodo = Job_Status.query.all()  # Fetch all todos
# #         return render_template('index.html', alltodo=alltodo)

    
# # @app.route('/update/<int:sno>', methods=['GET', 'POST'])
# # def update(sno):

# #    if request.method == 'POST':
# #      # Get form data
# #     title = request.form.get('title')
# #     desc = request.form.get('desc')

# #     # Find the Job_Status item
# #     Job_Status = Job_Status.query.filter_by(sno=sno).first()
# #     if not Job_Status:
# #         print(f"No Job_Status found with sno: {sno}")
# #         return "Error: Job_Status not found", 404

# #     # Update fields
# #     print(f"Updating Job_Status {sno}: {Job_Status.title} -> {title}, {Job_Status.desc} -> {desc}")
# #     Job_Status.title = title
# #     Job_Status.desc = desc

# #     # Commit changes
# #     db.session.commit()
# #     print("Job_Status updated successfully!")

# #     return redirect("/")
   
# #    else:
    
# #     Job_Status = Job_Status.query.filter_by(sno=sno).first()
# #     return render_template('update.html', Job_Status=Job_Status)

    



# # @app.route('/delete/<int:sno>')
# # def delete(sno):
# #     Job_Status = db.get_or_404(Job_Status, sno)
# #     db.session.delete(Job_Status)
# #     db.session.commit()
# #     print(f"Sucessfully Deleted {Job_Status.sno}")
# #     return redirect(url_for('home'))



# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import desc
# from flask_cors import CORS  # Enable CORS
# from datetime import datetime, date
# import time
# import subprocess

# app = Flask(__name__)
# CORS(app)  # Allow requests from React frontend

# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///newdb.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


# class Job(db.Model):
#     __tablename__ = 'job'
#     id = db.Column(db.Integer, primary_key=True)
#     file = db.Column(db.String(255), nullable=False)

#     def __repr__(self):
#         return f"<Jobs {self.id} - {self.file}>"


# class Job_Status(db.Model):
#     __tablename__ = 'job__status'
#     id = db.Column(db.Integer, primary_key=True)
#     job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
#     playbook = db.Column(db.String(50), nullable=False)
#     date = db.Column(db.Date, nullable=False)
#     start_time = db.Column(db.String(50), nullable=False)
#     end_time = db.Column(db.String(50), nullable=False)
#     duration = db.Column(db.String(50), nullable=False)
#     status = db.Column(db.String(50), nullable=False)

#     def __repr__(self):
#         return f"<Job_Status {self.id} - {self.job_id} >"


# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         selected_file = request.json.get('menu')
#         optionid = int(request.json.get("option_id"))
#         file_name = request.json.get("option_text")

#         dt = date.today()
#         start = time.time()
#         human_readable_st = time.ctime(start)[11:19]
        
#         stat = "In Progress"

#         # Run the subprocess
#         result = subprocess.run(["python", f"Folder/{selected_file}"], capture_output=True, text=True)

#         stat = "Success" if result.returncode == 0 else "Failure"

#         end = time.time()
#         human_readable_en = time.ctime(end)[11:19]
#         dur = round(end - start, 2)

#         # Check or create Job
#         job = Job.query.filter_by(id=optionid).first()
#         if not job:
#             job = Job(id=optionid, file=selected_file)
#             db.session.add(job)
#             db.session.commit()

#         # Create Job_Status entry
#         all_job = Job_Status(
#             job_id=optionid,
#             playbook=file_name,
#             date=dt,
#             start_time=human_readable_st,
#             end_time=human_readable_en,
#             duration=str(dur),
#             status=stat
#         )
#         db.session.add(all_job)
#         db.session.commit()

#         # Fetch all job statuses
#         all_jobs = Job_Status.query.order_by(desc(Job_Status.date), desc(Job_Status.end_time)).all()

#         # Convert to JSON
#         job_list = [
#             {
#                 "id": job.id,
#                 "job_id": job.job_id,
#                 "playbook": job.playbook,
#                 "date": job.date.strftime("%Y-%m-%d"),
#                 "start_time": job.start_time,
#                 "end_time": job.end_time,
#                 "duration": job.duration,
#                 "status": job.status
#             }
#             for job in all_jobs
#         ]

#         return jsonify({"message": "Job executed", "jobs": job_list})

#     else:
#         # Handle GET request
#         all_jobs = Job_Status.query.order_by(desc(Job_Status.date), desc(Job_Status.end_time)).all()
#         job_list = [
#             {
#                 "id": job.id,
#                 "job_id": job.job_id,
#                 "playbook": job.playbook,
#                 "date": job.date.strftime("%Y-%m-%d"),
#                 "start_time": job.start_time,
#                 "end_time": job.end_time,
#                 "duration": job.duration,
#                 "status": job.status
#             }
#             for job in all_jobs
#         ]

#         return jsonify({"jobs": job_list})


# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()  # Ensure tables are created
#         app.run(debug=True)





from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from flask_cors import CORS  # Enable CORS
from datetime import datetime, date
import time
import subprocess

app = Flask(__name__)
CORS(app)  # Allow requests from React frontend

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///newdb.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Job(db.Model):
    __tablename__ = 'job'
    id = db.Column(db.Integer, primary_key=True)
    file = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Jobs {self.id} - {self.file}>"


class Job_Status(db.Model):
    __tablename__ = 'job__status'
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    playbook = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.String(50), nullable=False)
    end_time = db.Column(db.String(50), nullable=False)
    duration = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Job_Status {self.id} - {self.job_id} >"


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        selected_file = request.json.get('menu')
        optionid = int(request.json.get("option_id"))
        file_name = request.json.get("option_text")

        dt = date.today()
        start = time.time()
        human_readable_st = time.ctime(start)[11:19]
        
        stat = "In Progress"

        # Run the subprocess
        if selected_file.endswith(".py"):
            result = subprocess.run(["python", f"Folder/{selected_file}"], capture_output=True, text=True)
        elif selected_file.endswith((".yml",".yaml")):
            result = subprocess.run(["ansible-playbook", f"Folder/{selected_file}"], capture_output=True, text=True)
        print("Output",result.stdout)
        print("error",result.stderr)
        stat = "Success" if result.returncode == 0 else "Failure"

        end = time.time()
        human_readable_en = time.ctime(end)[11:19]
        dur = round(end - start, 2)

        # Check or create Job
        job = Job.query.filter_by(id=optionid).first()
        if not job:
            job = Job(id=optionid, file=selected_file)
            db.session.add(job)
            db.session.commit()

        # Create Job_Status entry
        all_job = Job_Status(
            job_id=optionid,
            playbook=file_name,
            date=dt,
            start_time=human_readable_st,
            end_time=human_readable_en,
            duration=str(dur),
            status=stat
        )
        db.session.add(all_job)
        db.session.commit()

        # Fetch all job statuses
        all_jobs = Job_Status.query.order_by(desc(Job_Status.date), desc(Job_Status.end_time)).all()

        # Convert to JSON
        job_list = [
            {
                "id": job.id,
                "job_id": job.job_id,
                "playbook": job.playbook,
                "date": job.date.strftime("%Y-%m-%d"),
                "start_time": job.start_time,
                "end_time": job.end_time,
                "duration": job.duration,
                "status": job.status
            }
            for job in all_jobs
        ]

        return jsonify({"message": "Job executed", "jobs": job_list})

    else:
        # Handle GET request
        all_jobs = Job_Status.query.order_by(desc(Job_Status.date), desc(Job_Status.end_time)).all()
        job_list = [
            {
                "id": job.id,
                "job_id": job.job_id,
                "playbook": job.playbook,
                "date": job.date.strftime("%Y-%m-%d"),
                "start_time": job.start_time,
                "end_time": job.end_time,
                "duration": job.duration,
                "status": job.status
            }
            for job in all_jobs
        ]

        return jsonify({"jobs": job_list})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensure tables are created
        app.run(debug=True)
