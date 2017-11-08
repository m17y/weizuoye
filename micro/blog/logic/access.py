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


@context.set_roles_loader
def first_load_roles():
    yield "student"

print("* Now you are %s." % (context.role)),id(context)

# use it as `decorator`
@context.check_permission("edit", "article", message="can not edit")
def edit_article_page():
    return "<edit>"

try:
    edit_article_page()
except PermissionDenied as exception:
    print("You could not edit the article page, ")
    print("the exception said: '%s'." % exception.kwargs['message'])