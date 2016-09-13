from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

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
        self.rtri = 0
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
        
    def SetupOpenGL(self):
        self._Debug("SetupOpenGL")
        glutInit(self.argc,self.argv)
        glutInitDisplayMode(GLUT_DEPTH|GLUT_DOUBLE|GLUT_RGBA)
        glutInitWindowPosition(self.ori_position_x,self.ori_position_y)
        glutInitWindowSize(self.window_width,self.window_height)
        glutCreateWindow("CG Course Lesson 1")
        glutReshapeFunc(self._Resize)
        glutDisplayFunc(self._Display)
        glutKeyboardFunc(self._KeyPressed)
        glutIdleFunc(self._Display)
        self._InitOpenGL()
    def BeginOpenGL(self):
        self._Debug("BeginOpenGL")
        glutMainLoop()
    def _Display(self):
        """
        self._Debug("_Display")
        glClear(GL_COLOR_BUFFER_BIT)
        glPointSize(5.0)
    
        glColor3f(1.0, 1.0, 0.0)
        glBegin(GL_LINES)
        glVertex2f(-5.0, 0.0)
        glVertex2f(5.0, 0.0)
        glVertex2f(0.0, 5.0)
        glVertex2f(0.0, -5.0)
        glEnd()
 
        glColor3f(0.0, 0.0, 0.0)
        glBegin(GL_LINES)
        #for x in arange(-5.0, 5.0, 0.1):
        for x in (i * 0.1 for i in range(-50, 50)):
            y = x * x * x
            glVertex2f(x, y)
        glEnd()
        glFlush()
        """
      	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);	# Clear The Screen And The Depth Buffer
	glLoadIdentity();					# Reset The View
	#glTranslatef(-1.5,0.0,-6.0);				# Move Left And Into The Screen
        glTranslatef(0.0,0.0,-6.0);
    
	glRotatef(self.rtri,0.0,1.0,0.0);				# Rotate The Pyramid On It's Y Axis

	glBegin(GL_TRIANGLES);					# Start Drawing The Pyramid

	glColor3f(1.0,0.0,0.0);			# Red
	glVertex3f( 0.0, 1.0, 0.0);		# Top Of Triangle (Front)
	glColor3f(0.0,1.0,0.0);			# Green
	glVertex3f(-1.0,-1.0, 1.0);		# Left Of Triangle (Front)
	glColor3f(0.0,0.0,1.0);			# Blue
	glVertex3f( 1.0,-1.0, 1.0);

	glColor3f(1.0,0.0,0.0);			# Red
	glVertex3f( 0.0, 1.0, 0.0);		# Top Of Triangle (Right)
	glColor3f(0.0,0.0,1.0);			# Blue
	glVertex3f( 1.0,-1.0, 1.0);		# Left Of Triangle (Right)
	glColor3f(0.0,1.0,0.0);			# Green
	glVertex3f( 1.0,-1.0, -1.0);		# Right 

	glColor3f(1.0,0.0,0.0);			# Red
	glVertex3f( 0.0, 1.0, 0.0);		# Top Of Triangle (Back)
	glColor3f(0.0,1.0,0.0);			# Green
	glVertex3f( 1.0,-1.0, -1.0);		# Left Of Triangle (Back)
	glColor3f(0.0,0.0,1.0);			# Blue
	glVertex3f(-1.0,-1.0, -1.0);		# Right Of 
		
		
	glColor3f(1.0,0.0,0.0);			# Red
	glVertex3f( 0.0, 1.0, 0.0);		# Top Of Triangle (Left)
	glColor3f(0.0,0.0,1.0);			# Blue
	glVertex3f(-1.0,-1.0,-1.0);		# Left Of Triangle (Left)
	glColor3f(0.0,1.0,0.0);			# Green
	glVertex3f(-1.0,-1.0, 1.0);		# Right Of Triangle (Left)
	glEnd();
	self.rtri = self.rtri + 0.2

        glutSwapBuffers()
    def _KeyPressed(self,*args):
        length = len(args)
        for i in range(0,length):
            self._Debug(args[i])
        if args[0] == self.ESCAPE:
            sys.exit()
        
