#!/usr/bin/env python

from library.rbac.acl import Registry
from library.rbac.context import IdentityContext, PermissionDenied


# -----------------------------------------------
# build the access control list and add the rules
# -----------------------------------------------

acl = Registry()
context = IdentityContext(acl)

acl.add_role("admin")
acl.add_role("student")
acl.add_role("teacher")
acl.add_resource("article")

acl.allow("admin", "view", "article")
acl.allow("admin", "edit", "article")

