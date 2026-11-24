import unittest
from runtime_demo import Desk,User
class TestDesk(unittest.TestCase):
    def setUp(self):
        self.d=Desk(); self.a=User('A','listing_agent',(self.d.case,)); self.b=User('B','broker',(self.d.case,)); self.x=User('X','broker',('OTHER',))
    def test_broker_only(self):
        v=self.d.draft(self.a,self.d.case)
        with self.assertRaises(PermissionError): self.d.approve(self.a,self.d.case,v)
        self.assertEqual(self.d.status,'pending_review')
    def test_case_isolation(self):
        with self.assertRaises(PermissionError): self.d.draft(self.x,self.d.case)
    def test_old_version(self):
        v=self.d.draft(self.a,self.d.case); self.d.draft(self.a,self.d.case)
        with self.assertRaises(ValueError): self.d.approve(self.b,self.d.case,v)
    def test_source_revision(self):
        v=self.d.draft(self.a,self.d.case); self.d.approve(self.b,self.d.case,v); self.d.source_changed()
        self.assertEqual(self.d.status,'stale')
        with self.assertRaises(ValueError): self.d.approve(self.b,self.d.case,v)
    def test_valid_approval(self):
        v=self.d.draft(self.a,self.d.case); self.d.approve(self.b,self.d.case,v); self.assertEqual(self.d.status,'approved')
if __name__=='__main__': unittest.main()
