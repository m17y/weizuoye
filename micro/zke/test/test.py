# class Kls(object):
#     no_inst = 0
#     name = ''
#     @classmethod
#     def get_no_of_instance(cls_obj):
#         return cls_obj.name
#     @staticmethod
#     def st(cls_obj):
#         return cls_obj.name
# if __name__ == '__main__':
#     ik1 = Kls()
#     ik1.name='xxxx'
#     ik2 = Kls()
#     print ik1.get_no_of_instance()
#     print Kls.get_no_of_instance()


#!/usr/bin/env python

from rbac.acl import Registry
from rbac.context import IdentityContext, PermissionDenied


# -----------------------------------------------
# build the access control list and add the rules
# -----------------------------------------------

acl = Registry()
context = IdentityContext(acl)

acl.add_role("staff")
acl.add_role("editor", parents=["staff"])
acl.add_role("bad man", parents=["staff"])
acl.add_resource("article")

acl.allow("staff", "edit", "article")
acl.allow("editor", "edit", "article")
acl.deny("bad man", None, "article")

# def av(ccc):
#     import pdb;pdb.set_trace()
#     return ccc

# # -------------
# # to be a staff
# # -------------
# @av
# def bb():
#     a='1111'
#     print a



@context.set_roles_loader
def first_load_roles():
    yield "staff"

# import pdb;pdb.set_trace()
# print context.load_roles()
print("* Now you are %s." % ", ".join(context.load_roles()))

@context.check_permission("view", "article", message="can not view")
def article_page():
    return "<view>"


# use it as `decorator`
@context.check_permission("edit", "article", message="can not edit")
def edit_article_page():
    return "<edit>"
    print 


if article_page() == "<view>":
    print("You could view the article page.")

try:
    edit_article_page()
except PermissionDenied as exception:
    print("You could not edit the article page, ")
    print("the exception said: '%s'." % exception.kwargs['message'])

try:
    # use it as `with statement`
    with context.check_permission("edit", "article"):
        pass
except PermissionDenied:
    print("Maybe it's because you are not a editor.")


# --------------
# to be a editor
# --------------

@context.set_roles_loader
def second_load_roles():
    yield "editor"


print("* Now you are %s." % ", ".join(context.load_roles()))

if edit_article_page() == "<edit>":
    print("You could edit the article page.")


# ---------------
# to be a bad man
# ---------------

@context.set_roles_loader
def third_load_roles():
    yield "bad man"


print("* Now you are %s." % ", ".join(context.load_roles()))

try:
    article_page()
except PermissionDenied as exception:
    print("You could not view the article page,")
    print("the exception said: '%s'." % exception.kwargs['message'])

# use it as `nonzero`
if not context.check_permission("view", "article"):
    print("Oh! A bad man could not view the article page.")

# use it as `check function`
try:
    context.check_permission("edit", "article").check()
except PermissionDenied as exception:
    print("Yes, of course, a bad man could not edit the article page too.")