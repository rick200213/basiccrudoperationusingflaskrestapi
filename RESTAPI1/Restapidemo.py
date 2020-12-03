# using flask_restfu
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import pymysql


# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)


# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class MyAPI(Resource):

    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    # Connect to MySQL database
    con = pymysql.connect(host='localhost', user='root', passwd='Account1start', database='webdevsignup')
    print('connection sucessful')

    cur = con.cursor()
#GET CORRESPONDS TO FETCHING DATA FROM DB RETREIVE IN CRUD
    def get(self):
        data={'message': 'hello world'}
        # Connect to MySQL database

        str = "select * from employeeinfo "
        self.cur.execute(str)
        n = self.cur.fetchall()
        return jsonify(n)
#POST CORRESPONDS TO INSERT INTO DATABSAE
    def post(self):
      data=request.get_json()
      name = data['name']
      salary = data['salary']
      age = data['age']

      print(data)
      try:
        str = "insert into employeeinfo values('%s','%s','%s')"
        print("Hello")
        args = ( name, salary,age)
        print("hi")
        self.cur.execute(str % args)
        self.con.commit()
        resp=jsonify("Data inserted successfully")
        resp.status_code=200
        return resp
      except:
        print('Insertion Failed')
        self.con.rollback()

#put corresponds to update in CRUD
    def put(self):
#request.json converts json format data into normal format
        data=request.json
        name = data['name']
        age = data['age']
        print(data)
        try:
            str = "update employeeinfo set name='%s' where age='%s' "
            print("Hello")
            args = (name,age)
            print("hi")
            self.cur.execute(str % args)
            self.con.commit()
            resp=jsonify("Data inserted successfully")
            resp.status_code=200
            return resp
        except:
            print('Insertion Failed')
            self.con.rollback()
#delete deletes a row of the databse D of CRUD
    def delete(self):
        data = request.json
        name = data['name']

        print(data)
        try:
            str = "delete from employeeinfo where name='%s' "
            print("Hello")
            args = (name)
            print("hi")
            self.cur.execute(str % args)
            self.con.commit()
            resp = jsonify("Data inserted successfully")
            resp.status_code = 200
            return resp
        except:
            print('Insertion Failed')
            self.con.rollback()


# Corresponds to POST request
class MyAPI1(Resource):
    con = pymysql.connect(host='localhost', user='root', passwd='Account1start', database='webdevsignup')
    print('connection sucessful')

    cur = con.cursor()

    def get(self, get):
        str = "select * from student1 where name='%s'"
        args=get
        self.cur.execute(str%args)
        n = self.cur.fetchall()

        #data={'square': num ** 2}

        return jsonify(n)


api.add_resource(MyAPI, '/')
api.add_resource(MyAPI1, '/square/<string:get>')


# driver function
if __name__ == '__main__':
    app.run(debug=True)