from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from mycube import *


class MyOpenGL():
    def __init__(self,argc,argv):
        self.argc = argc
        self.argv = argv
        self.debug = True
        self.ESCAPE = '\033'
        self.ori_position_x = 50
        self.ori_position_y = 50
        self.window_width = 512
        self.window_height = 512
        self.window_back_color = [0.0, 0.0, 0.0, 1.0]
        self.window_back_depth = 1.0

        self.xy = 0.0
        self.yz = 90.0

        self.viewSpeed = 2.0

        self.magiccube = MagicCube()
    def _Debug(self,data):
        if self.debug:
            print data
    def _InitOpenGL(self):
        self._Debug("_InitOpenGL")
        glEnable(GL_TEXTURE_2D)
        glShadeModel(GL_SMOOTH)
        glClearColor(self.window_back_color[0],\
                     self.window_back_color[1],\
                     self.window_back_color[2],\
                     self.window_back_color[3])

        glClearDepth(self.window_back_depth)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
        #glHint(GL_PERSPECTIVE_COORRECTION_HINT,GL_NICEST)
        
        #gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()					# Reset The Projection Matrix
        # Calculate The Aspect Ratio Of The Window
        gluPerspective(50.0, float(self.window_width)/float(self.window_height), 0.5, 100.0)
        glMatrixMode(GL_MODELVIEW)

        glFrontFace(GL_CCW)
        glCullFace(GL_BACK)
        glEnable(GL_CULL_FACE)
        #glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
    def _Resize(self,width,height):
        self._Debug("_Resize")
        if height == 0:
            height = 1
        self.window_width = width
        self.window_height = height
        glViewport(0,0,self.window_width,self.window_height)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        gluPerspective(50.0,float(self.window_width)/float(self.window_height),0.5,100.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        #gluLookAt(5.0,5.0,5.0,1.0,1.0,1.0,0,1,0)

    def _SetupRC(self):
        self._Debug("SetupRC")
        ambientLight = [0.0,0.0,0.0,1.0]
        diffuseLight = [1.0,1.0,1.0,1.0]
        positionLight = [0.0,0.0,1.0,0.0]
        specularLight = [1.0,1.0,1.0,1.0]
        lmodel_ambient = [0.4,0.4,0.4,1.0]
        local_view = 0.0

        glClearColor(0.0,0.1,0.1,0.0)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)

        glLightfv(GL_LIGHT0,GL_AMBIENT,ambientLight)
        glLightfv(GL_LIGHT0,GL_DIFFUSE,diffuseLight)
        glLightfv(GL_LIGHT0,GL_SPECULAR,specularLight)
        glLightfv(GL_LIGHT0,GL_POSITION,positionLight)
        
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT,lmodel_ambient)
        glLightModelfv(GL_LIGHT_MODEL_LOCAL_VIEWER,local_view)

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        
    def SetupOpenGL(self):
        self._Debug("SetupOpenGL")
        glutInit(self.argc,self.argv)
        glutInitDisplayMode(GLUT_DEPTH|GLUT_DOUBLE|GLUT_RGBA)
        glutInitWindowPosition(self.ori_position_x,self.ori_position_y)
        glutInitWindowSize(self.window_width,self.window_height)
        glutCreateWindow("CG Course Lesson 1")

        self.magiccube.InitCubes()
        self._InitTextTure()
        self._SetupRC()

        glutReshapeFunc(self._Resize)
        glutDisplayFunc(self._Display)
        glutKeyboardFunc(self._KeyPressed)
        glutMouseFunc(self._MouseFunc)
        glutIdleFunc(self._Display)
        self._InitOpenGL()
        
    def BeginOpenGL(self):
        self._Debug("BeginOpenGL")
        glutMainLoop()            

    def _InitTextTure(self):
        self.magiccube.LoadTextures()
        

    def _polarView(self,distance,twist,elevation,azimuth):
        glTranslated(0.0,0.0,-distance)
        glRotated(-twist,0.0,0.0,1.0)
        glRotated(-elevation,1.0,0.0,0.0)
        glRotated(azimuth,0.0,0.0,1.0)
        
    def _Display(self):
        #self._InitTextTure()
	glEnable(GL_TEXTURE_2D)
	glShadeModel(GL_SMOOTH)
	glClearDepth(self.window_back_depth)
	glEnable(GL_DEPTH_TEST)
	glDepthFunc(GL_LEQUAL)
	glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

	glClearColor(0.0,0.0,0.0,0.0)
	glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT)
	glPushMatrix()
	self._polarView(9.0,0.0,self.yz,self.xy)
	#drawCube()
	self.magiccube.DrawCubes()
	glPopMatrix()
        glutSwapBuffers()

    def _KeyPressed(self,*args):
        if args[0] == self.ESCAPE:
            sys.exit()
        if ( self.magiccube.spinning == False ):
            if args[0] == 's':
                self.yz -= self.viewSpeed
                glutPostRedisplay()
            elif args[0] == 'w':
                self.yz += self.viewSpeed
                glutPostRedisplay()        
            elif args[0] == 'd':
                self.xy -= self.viewSpeed
                glutPostRedisplay()
            elif args[0] == 'a':
                self.xy += self.viewSpeed
                glutPostRedisplay()
            elif args[0] == 'c':
                self.magiccube.SetGoBackFlag()
            else:
                self.magiccube.CubeTransform(args[0])
    def _GetSelectRay(self,mx,my):
        modelview = None
        projection = None
        viewport = None
        wx = 0
        wy = 0
        wz = 0
        
        glGetDoublev(GL_MODELVIEW_MATRIX,modelview)
        glGetDoublev(GL_PROJECTION_MATRIX,projection)
        glGetDoublev(GL_VIEWPORT,viewport)

        #gluUnProject(mx,my,0.0,modelview,projection,viewport,wx,wy,wz)
        gluUnProject(mx,my,0.0,wx,wy,wz)
        print near_point(wx,wy,wz)
        
    def _MouseFunc(self,button,state,x,y):
        pass
        #self._GetSelectRay(x,y)
