from sys import maxsize

class Project:
    def __init__(self, id=None, name=None, description=None, status="development", view_status="public"):
         self.id = id
         self.name = name
         self.description = description
         self.status = status
         self.view_status = view_status

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.description)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.name == other.name) \
               and (self.description == other.description)

    def id_or_max(self):
        if self.id:
           return int(self.id)
        else:
            return maxsize