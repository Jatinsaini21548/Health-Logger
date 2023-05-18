class HealthLogger:

    def __init__(self, id=None, name=None, phone=None, weight=None, bphigh=None, bplow=None,  sugar=None, created_on=None):
        self.id = id
        self.name = name
        self.phone = phone
        self.weight = weight
        self.bphigh = bphigh
        self.bplow = bplow
        self.sugar = sugar
        self.created_on = created_on

    def insert_sql(self):
        return "insert into HealthLogger (name, phone, weight, bphigh, bplow, sugar) " \
               "values " \
               "('{name}', '{phone}', '{weight}', '{bphigh}', '{bplow}', '{sugar}');".format_map(vars(self))

    def update_sql(self):
        return ""

    def delete_sql(self):
        return "delete from HealthLogger where cid = {}".format(self.id)

    def select_sql(self):
        return "select * from HealthLogger"


h1 = HealthLogger()
print(vars(h1))
