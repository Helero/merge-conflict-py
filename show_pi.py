#!/usr/bin/env python3

def approximate_pi():
    return 355 / 113

def show_pi():
<<<<<<< HEAD
    print("pi is approximately {:.8f}".format(approximate_pi()))
=======
    print("π is {:.5f}".format(approximate_pi()))
>>>>>>> 9c946a7cd5015d135042473d83c07a873a12ecb8

if __name__ == "__main__":
    show_pi()
