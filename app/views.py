from flask import Blueprint, jsonify, request, current_app

from . import db
from .models import Student


bp_main = Blueprint('bp_main', __name__)

    
@bp_main.route('/')
def hanlde_hello():
    ua = request.headers.get('User-Agent')
    current_app.logger.info('access from User-Agent: %s', ua)
    return 'Hello, World!'


@bp_main.route('/student/', methods=['GET'])
def hanlde_show_students():
    records = Student.query.all()

    columns = ['id', 'name', 'age', 'address']
    return jsonify(
        success=True,
        data=[r.readyToJSON(columns) for r in records]
    )


"""
GET ?name=[str]&age=[int]&address=[str]
age, address is optional.
"""
@bp_main.route('/student/add', methods=['GET'])
def hanlde_add_student():
    name = request.args.get('name')
    if name is None:
        return jsonify(
            success=False,
            msg='You must assign a name field.'
        )

    age = request.args.get('age')
    if age is not None:
        age = int(age)

    address = request.args.get('address')    
    s = Student(name=name, age=age, address=address)
    db.session.add(s)
    db.session.commit()

    return jsonify(
        success=True,
        msg=f'Add student {name} success.'
    )
