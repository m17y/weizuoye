class Kls(object):
    no_inst = 0
    name = ''
    @classmethod
    def get_no_of_instance(cls_obj):
        return cls_obj.name
    @staticmethod
    def st(cls_obj):
        return cls_obj.name
if __name__ == '__main__':
    ik1 = Kls()
    ik1.name='xxxx'
    ik2 = Kls()
    print ik1.get_no_of_instance()
    print Kls.get_no_of_instance()

