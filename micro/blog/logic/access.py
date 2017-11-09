#!/usr/bin/env python
import tornado
from tornado.httpclient import HTTPError


paccess={}

def needcheck(**kwargs):
    def actual(handler):
        handler.__needcheck__ = kwargs
        assert(issubclass(handler, tornado.web.RequestHandler))
        handler_method = set(['get','post'])&set(handler.__dict__.keys())
        paccess[str(handler).split('\'')[1]]=dict((k,handler.__dict__.get(k).__doc__)for k in handler_method)
        return handler
    return actual

def check_access(handler, access):

    if not access:
        raise HTTPError(403)
    if not str(handler.__class__).split('\'')[1] in access:
        raise HTTPError(403)




from library.rbac.acl import Registry
from library.rbac.context import IdentityContext, PermissionDenied

acl = Registry()
context = IdentityContext(acl)

acl.add_role("admin")
acl.add_role("student")
acl.add_role("teacher")
acl.add_resource("article")

acl.allow("admin", "view", "article")
acl.allow("admin", "edit", "article")
