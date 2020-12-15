class Group:
    def __init__(self, groupname=None, grouphead1=None, groupfooter1=None, id=None):
        self.groupname = groupname
        self.grouphead1 = grouphead1
        self.groupfooter1 = groupfooter1
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.groupname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.groupname == other.groupname

    