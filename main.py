from my3d import *
import sys

def main():
    myopengl = MyOpenGL(len(sys.argv),sys.argv)
    myopengl.SetupOpenGL()
    myopengl.BeginOpenGL()
    

if __name__=="__main__":
    main()
