from flask import *
from ProjectA1 import DBHelper
from ProjectA2 import HealthLogger

app = Flask("HealthLogger", template_folder="templates")
db_helper = DBHelper()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add")
def add_health_log():
    return render_template("add-health-log.html")


@app.route("/view")
def view_all_health_logs():

    health_logger_object = HealthLogger()
    sql = health_logger_object.select_sql()

    rows = db_helper.read(sql)

    return render_template("logs.html", result=rows)


@app.route("/save", methods=["POST"])
def save_health_data():
    print("Save health Data Executed...")

    """
    health_data = {
        "phone": request.form['txtPhone'],
        "weight": request.form['weight'],
        "bphigh": request.form['bphigh'],
        "bplow": request.form['bplow'],
        "sugar": request.form['sugar'],
    }
    print("health_data dictionary:", health_data)
    """

    health_data_object = HealthLogger(name=request.form["name"],
                                      phone=request.form["phone"],
                                      weight=request.form["weight"],
                                      bphigh=request.form["bphigh"],
                                      bplow=request.form["bplow"],
                                      sugar=request.form["sugar"])

    #   if len(health_data_object.name) == 0:
    #        return render_template("error.html", message=health_data_object.name + "Insertion Failed...")
    print(vars(health_data_object))
    sql = health_data_object.insert_sql()
    db_helper.write(sql)
    return health_data_object.name + "Inserted Successfully..."


#    return render_template("Success.html", message=health_data_object.name+"Inserted Successfully...")

def main():
    app.run()


if __name__ == "__main__":
    main()
