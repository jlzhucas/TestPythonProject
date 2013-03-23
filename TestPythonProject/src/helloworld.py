'''
Created on Mar 23, 2013

@author: zhu
'''


class Test(object):
    def get_test_name(self):
        return "hello world!"


if __name__ == "__main__":
    t = Test()
    print t.get_test_name()
