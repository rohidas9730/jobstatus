# from flask import Flask,render_template,request,redirect,url_for
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] =  "sqlite:///todo.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# # db.init_app(app)

# class Todo(db.Model):
#     sno = db.Column(db.Integer,primary_key = True)
#     title = db.Column(db.String(200),nullable = False)
#     desc = db.Column(db.String(500),nullable = False)
#     date_created = db.Column(db.DateTime,default = datetime.utcnow)

#     def __repr__(self) -> str:
#         return f"{self.sno} - {self.title}"

# @app.route('/', methods=['GET','POST'])
# def home():
#     if request.method == 'POST':
#         # Handle POST request
#         title = request.form.get('title')  # Safely get the 'title' from the form
#         desc = request.form.get('desc')
#         todo = Todo(title = title,desc = desc)
#         db.session.add(todo)
#         db.session.commit()
#         result = db.session.execute(db.select(Todo).order_by(Todo.sno))
#         alltodo = result.scalars()
#         return render_template('index.html', alltodo=alltodo)
#     else:
#         # Handle GET request
#         alltodo = Todo.query.all()  # Fetch all todos
#         return render_template('index.html', alltodo=alltodo)

    
# @app.route('/update/<int:sno>', methods=['GET', 'POST'])
# def update(sno):

#    if request.method == 'POST':
#      # Get form data
#     title = request.form.get('title')
#     desc = request.form.get('desc')

#     # Find the Todo item
#     todo = Todo.query.filter_by(sno=sno).first()
#     if not todo:
#         print(f"No Todo found with sno: {sno}")
#         return "Error: Todo not found", 404

#     # Update fields
#     print(f"Updating Todo {sno}: {todo.title} -> {title}, {todo.desc} -> {desc}")
#     todo.title = title
#     todo.desc = desc

#     # Commit changes
#     db.session.commit()
#     print("Todo updated successfully!")

#     return redirect("/")
   
#    else:
    
#     todo = Todo.query.filter_by(sno=sno).first()
#     return render_template('update.html', todo=todo)

    

    



# @app.route('/delete/<int:sno>')
# def delete(sno):
#     todo = db.get_or_404(Todo, sno)
#     db.session.delete(todo)
#     db.session.commit()
#     print(f"Sucessfully Deleted {todo.sno}")
#     return redirect(url_for('home'))




# if __name__ == "__main__":
#     app.run(debug=True)
 