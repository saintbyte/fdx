__author__ = 'sb'


def encode_face_link(num, top, right, bottom, left):
    return "{0:0>7}".format(num) + "{0:0>7}".format(top) + "{0:0>7}".format(right) + "{0:0>7}".format(
        bottom) + "{0:0>7}".format(left)


def decode_face_link(s):
    num = int(s[0:7])
    top = int(s[7:14])
    right = int(s[14:21])
    bottom = int(s[21:28])
    left = int(s[28:36])
    return (num, top, right, bottom, left)
