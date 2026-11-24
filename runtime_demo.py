"""Deterministic classroom simulation. No LLM, network, real identity or storage."""
from dataclasses import dataclass
@dataclass(frozen=True)
class User:
    name: str
    role: str
    cases: tuple[str, ...]
class Desk:
    def __init__(self):
        self.case='CASE-DEMO-001'; self.source_revision=1; self.version=0
        self.status='empty'; self.draft_source=None; self.trace=[]
    def _check(self, user, case):
        if case != self.case or case not in user.cases:
            raise PermissionError('case access denied')
        if user.role not in ('listing_agent','coordinator','broker','marketing'):
            raise PermissionError('role denied')
    def draft(self, user, case):
        self._check(user,case); self.version+=1; self.draft_source=self.source_revision
        self.status='pending_review'; self.trace.append(('draft', self.version, self.source_revision)); return self.version
    def approve(self,user,case,version):
        self._check(user,case)
        if user.role!='broker': raise PermissionError('broker required')
        if self.status!='pending_review' or version!=self.version or self.draft_source!=self.source_revision:
            raise ValueError('stale or invalid approval')
        self.status='approved'; self.trace.append(('approve',version,self.source_revision))
    def source_changed(self):
        # trusted system event, not an exposed model tool
        self.source_revision+=1
        if self.version: self.status='stale'
        self.trace.append(('source_changed',self.source_revision))
if __name__=='__main__':
    desk=Desk(); agent=User('Demo agent','listing_agent',(desk.case,)); broker=User('Demo broker','broker',(desk.case,))
    v=desk.draft(agent,desk.case); print('Draft:',v,desk.status)
    try: desk.approve(agent,desk.case,v)
    except PermissionError as e: print('Expected block:',e)
    desk.approve(broker,desk.case,v); print('Broker:',desk.status)
    desk.source_changed(); print('Source changed:',desk.status)
    try: desk.approve(broker,desk.case,v)
    except ValueError as e: print('Expected block:',e)
    v=desk.draft(agent,desk.case); desk.approve(broker,desk.case,v); print('New version:',v,desk.status)
    print('Trace:',desk.trace)
