import _pickle as pkl
from pyCMeKG.model import CMeKG

class cmekg(object):
    def __init__(self, db_file = "cmekg_1.0"):
        self.kg = CMeKG(db_file)

    def subject(self, subject_name = None):
        """query by subject"""
        return self.kg.query_by_subject(subject_name)

    def subject_predicate(self, subject_name = None, predicate_name = None):
        """query by subject, predicate"""
        return self.kg.query_by_subject_predicate(subject_name, predicate_name)

