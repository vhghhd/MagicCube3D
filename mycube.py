from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import copy
import Image

class Cube():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.sx = 0
        self.sy = 0
        self.sz = 0
        self.num = 0
        self.orders = None;
        self.textures = {}
        self.drawtexnum = 0
        self.ambient = [0.2,0.2,0.2,0.1]
        self.diffuse = [1.0,0.8,0.0,0.1]
        self.specular = [1.0,1.0,1.0,1.0]
        self.shine = 50
    def _DrawTexure(self):
        glMaterialfv(GL_FRONT,GL_AMBIENT,self.ambient)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,self.diffuse)
        glMaterialfv(GL_FRONT,GL_SPECULAR,self.specular)
        glMateriali(GL_FRONT,GL_SHININESS,self.shine)
    def ChangeXG(self):
        tmp = self.textures['up']
        self.textures['up'] = self.textures['bt']
        self.textures['bt'] = self.textures['dn']
        self.textures['dn'] = self.textures['ft']
        self.textures['ft'] = tmp
    def ChangeXB(self):
        tmp = self.textures['up']
        self.textures['up'] = self.textures['ft']
        self.textures['ft'] = self.textures['dn']
        self.textures['dn'] = self.textures['bt']
        self.textures['bt'] = tmp
    
        
    def ChangeYG(self):
        tmp = self.textures['ft']
        self.textures['ft'] = self.textures['lt']
        self.textures['lt'] = self.textures['bt']
        self.textures['bt'] = self.textures['rt']
        self.textures['rt'] = tmp
    def ChangeYB(self):
        tmp = self.textures['ft']
        self.textures['ft'] = self.textures['rt']
        self.textures['rt'] = self.textures['bt']
        self.textures['bt'] = self.textures['lt']
        self.textures['lt'] = tmp

        
    def ChangeZG(self):
        tmp = self.textures['up']
        self.textures['up'] = self.textures['rt']
        self.textures['rt'] = self.textures['dn']
        self.textures['dn'] = self.textures['lt']
        self.textures['lt'] = tmp
    def ChangeZB(self):
        tmp = self.textures['up']
        self.textures['up'] = self.textures['lt']
        self.textures['lt'] = self.textures['dn']
        self.textures['dn'] = self.textures['rt']
        self.textures['rt'] = tmp

        
    def SetTextures(self,upt,downt,frontt,backt,leftt,rightt):
        self.textures['up'] = upt
        self.textures['dn'] = downt
        self.textures['ft'] = frontt
        self.textures['bt'] = backt
        self.textures['lt'] = leftt
        self.textures['rt'] = rightt
        
    def SetXYZ(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def SetSXYZ(self,sx,sy,sz):
        self.sx = sx
        self.sy = sy
        self.sz = sz
    def SetNum(self,num):
        self.num = num
    def GetNum(self):
        return self.num
    def SetOrders(self,orders):
        self.orders = orders
    def PrintThing(self):
        print self.x,self.y,self.z
        print self.sx,self.sy,self.sz
        print self.num
    def _DrawCubeFront(self):
        glBindTexture(GL_TEXTURE_2D, int(self.textures['ft']))
        glBegin(GL_QUADS)

        glNormal3f(0.0,0.0,1.0)
        
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-0.5, -0.5,  0.5)
        
        glTexCoord2f(1.0, 0.0)
        glVertex3f( 0.5, -0.5,  0.5)

        glTexCoord2f(1.0, 1.0)
        glVertex3f( 0.5,  0.5,  0.5)
        
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-0.5,  0.5,  0.5)
        glEnd()
        self.drawtexnum += 1
    def _DrawCubeBack(self):
        glBindTexture(GL_TEXTURE_2D, int(self.textures['bt']))
        glBegin(GL_QUADS)

        glNormal3f(0.0,0.0,-1.0)
        
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-0.5, -0.5,  -0.5)
        
        glTexCoord2f(1.0, 1.0)
        glVertex3f( -0.5, 0.5,  -0.5)

        glTexCoord2f(0.0, 1.0)
        glVertex3f( 0.5,  0.5,  -0.5)
        
        glTexCoord2f(0.0, 0.0)
        glVertex3f(0.5,  -0.5,  -0.5)
        glEnd()

    def _DrawCubeUp(self):
        glBindTexture(GL_TEXTURE_2D, int(self.textures['up']))
        glBegin(GL_QUADS)

        glNormal3f(0.0,1.0,0.0)
        
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-0.5, 0.5,  -0.5)
        
        glTexCoord2f(0.0, 0.0)
        glVertex3f( -0.5, 0.5,  0.5)

        glTexCoord2f(1.0, 0.0)
        glVertex3f( 0.5,  0.5,  0.5)
        
        glTexCoord2f(1.0, 1.0)
        glVertex3f(0.5,  0.5,  -0.5)
        glEnd()

    def _DrawCubeDown(self):
        glBindTexture(GL_TEXTURE_2D, int(self.textures['dn']))
        glBegin(GL_QUADS)

        glNormal3f(0.0,-1.0,0.0)
        
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-0.5, -0.5,  -0.5)
        
        glTexCoord2f(0.0, 1.0)
        glVertex3f( 0.5, -0.5,  -0.5)

        glTexCoord2f(0.0, 0.0)
        glVertex3f( 0.5,  -0.5,  0.5)
        
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-0.5,  -0.5,  0.5)
        glEnd()
        
    def _DrawCubeLeft(self):
        glBindTexture(GL_TEXTURE_2D, int(self.textures['lt']))
        glBegin(GL_QUADS)

        glNormal3f(-1.0,0.0,0.0)
        
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-0.5, -0.5,  -0.5)
        
        glTexCoord2f(1.0, 0.0)
        glVertex3f( -0.5, -0.5,  0.5)

        glTexCoord2f(1.0, 1.0)
        glVertex3f( -0.5,  0.5,  0.5)
        
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-0.5,  0.5,  -0.5)
        glEnd()


    def _DrawCubeRight(self):
        glBindTexture(GL_TEXTURE_2D, int(self.textures['rt']))
        glBegin(GL_QUADS)

        glNormal3f(1.0,0.0,0.0)
        
        glTexCoord2f(1.0, 0.0)
        glVertex3f(0.5, -0.5,  -0.5)
        
        glTexCoord2f(1.0, 1.0)
        glVertex3f( 0.5, 0.5,  -0.5)

        glTexCoord2f(0.0, 1.0)
        glVertex3f( 0.5,  0.5,  0.5)
        
        glTexCoord2f(0.0, 0.0)
        glVertex3f(0.5,  -0.5,  0.5)
        glEnd()

        
    def DrawCube(self):
        self._DrawTexure()
        self._DrawCubeFront()
        self._DrawCubeBack()
        self._DrawCubeUp()
        self._DrawCubeDown()
        self._DrawCubeLeft()
        self._DrawCubeRight()

class MagicCube():
    def __init__(self):
        self.cubelist = []
        self.spinning = False
        self.selectlst = []
        self.spinspeed = 10
        self.angle = 0
        self.keyboard = 0
        self.textures = []
        self.texturefiles = ['pic/yellow.bmp','pic/white.bmp',
                             'pic/red.bmp','pic/orange.bmp',
                             'pic/blue.bmp','pic/green.bmp']
        self.gobackflag = True
        self.texchanged = False
        
    def _CreateTexture(self,pos):
        print self.texturefiles[pos],pos,self.textures[pos]
        imagefile = Image.open(self.texturefiles[pos])
        ix = imagefile.size[0]
        iy = imagefile.size[1]
        image = imagefile.tostring("raw", "RGBX", 0, -1)
	
        # Create Texture	
        glBindTexture(GL_TEXTURE_2D, int(self.textures[pos]))   # 2d texture (x and y size)
	
        glPixelStorei(GL_UNPACK_ALIGNMENT,1)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
	glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR);
	glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR);
	glTexEnvf(GL_TEXTURE_ENV,GL_TEXTURE_ENV_MODE,GL_REPLACE);

    def SetGoBackFlag(self):
        self.gobackflag = not self.gobackflag

    def LoadTextures(self):
        print "Load"
        
        print self.textures
        for i in range(0,len(self.texturefiles)):
            self._CreateTexture(i)
        for cube in self.cubelist:
            cube.SetTextures(self.textures[0],self.textures[1],self.textures[2],self.textures[3],self.textures[4],self.textures[5])
        
    def InitCubes(self):
        x = -1.0
        for i in range(0,3):
            y = -1.0
            for j in range(0,3):
                z = -1.0
                for k in range(0,3):
                    cube = Cube()
                    cube.SetXYZ(x,y,z)
                    cube.SetSXYZ(0,0,0)
                    cube.SetOrders(0)
                    cube.SetNum(self._GetCubePos(i,j,k))
                    self.cubelist.append(cube)
                    z += 1.0
                y += 1.0
            x += 1.0

        self.textures = glGenTextures(6)
        #self._PrintCubeThing()
    def _PrintCubeThing(self):
        for cube in self.cubelist:
            cube.PrintThing()
    def DrawCubes(self):
        for cube in self.cubelist:
            glPushMatrix()
            if self.gobackflag:
                glRotatef(cube.sx,1.0,0.0,0.0)
                glRotatef(cube.sz,0.0,0.0,1.0)
                glRotatef(cube.sy,0.0,1.0,0.0)
            else:
                glRotatef(cube.sx,-1.0,0.0,0.0)
                glRotatef(cube.sz,0.0,0.0,-1.0)
                glRotatef(cube.sy,0.0,-1.0,0.0)
            if cube.orders == 'x':
                #print 'x',cube.GetNum()
                glRotatef(90.0,1.0,0.0,0.0)
            elif cube.orders == 'y':
                #print 'y',cube.GetNum()
                glRotatef(90.0,0.0,1.0,0.0)
            elif cube.orders == 'z':
                #print 'z',cube.GetNum()
                glRotatef(90.0,0.0,0.0,1.0)
            glTranslatef(cube.x,cube.y,cube.z)
            cube.DrawCube()
            glPopMatrix()
    def _GetCubePos(self,x,y,z):
        return (x*3+y)*3+z
    def _Select(self):
        self.selectlst = []
        if self.keyboard == 1:
            for i in range(0,3):
                for j in range(0,3):
                    self._Makeorder(self.cubelist[self._GetCubePos(0,i,j)],self._GetCubePos(0,i,j))
        elif self.keyboard == 2:
            for i in range(0,3):
                for j in range(0,3):
                    self._Makeorder(self.cubelist[self._GetCubePos(1,i,j)],self._GetCubePos(1,i,j))
        elif self.keyboard == 3:
            for i in range(0,3):
                for j in range(0,3):
                    self._Makeorder(self.cubelist[self._GetCubePos(2,i,j)],self._GetCubePos(2,i,j))
        elif self.keyboard == 4:
            for i in range(0,3):
                for j in range(0,3):
                    self._Makeorder(self.cubelist[self._GetCubePos(j,0,i)],self._GetCubePos(j,0,i))
        elif self.keyboard == 5:
            for i in range(0,3):
                for j in range(0,3):
                    self._Makeorder(self.cubelist[self._GetCubePos(j,1,i)],self._GetCubePos(j,1,i))
        elif self.keyboard == 6:
            for i in range(0,3):
                for j in range(0,3):
                    self._Makeorder(self.cubelist[self._GetCubePos(j,2,i)],self._GetCubePos(j,2,i))
        elif self.keyboard == 7:
            for i in range(0,3):
                for j in range(0,3):
                    self._Makeorder(self.cubelist[self._GetCubePos(i,j,0)],self._GetCubePos(i,j,0))
        elif self.keyboard == 8:
            for i in range(0,3):
                for j in range(0,3):
                    self._Makeorder(self.cubelist[self._GetCubePos(i,j,1)],self._GetCubePos(i,j,1))
        elif self.keyboard == 9:
            for i in range(0,3):
                for j in range(0,3):
                    self._Makeorder(self.cubelist[self._GetCubePos(i,j,2)],self._GetCubePos(i,j,2))

    def _Makeorder(self,selectcube,selectpos):
        if self.keyboard > 0 and self.keyboard <= 3:
            flag = 'x'
        elif self.keyboard > 3 and self.keyboard <= 6:
            flag = 'y'
        elif self.keyboard > 6 and self.keyboard <= 9:
            flag = 'z'

        selectcube.SetOrders(flag)
        self.selectlst.append(selectpos)
    def _ChangeTex(self,endflag):
        if not self.texchanged:
            for selectpos in self.selectlst:
                if self.cubelist[selectpos].orders == 'x':
                    self.cubelist[selectpos].ChangeXB()
                if self.cubelist[selectpos].orders == 'y':
                    self.cubelist[selectpos].ChangeYB()
                if self.cubelist[selectpos].orders == 'z':
                    self.cubelist[selectpos].ChangeZB()
        elif endflag:
            for selectpos in self.selectlst:
                if self.cubelist[selectpos].orders == 'x':
                    if self.gobackflag:
                        self.cubelist[selectpos].ChangeXG()
                        self.cubelist[selectpos].ChangeXG()
                if self.cubelist[selectpos].orders == 'y':
                    if self.gobackflag:
                        self.cubelist[selectpos].ChangeYG()
                        self.cubelist[selectpos].ChangeYG()
                if self.cubelist[selectpos].orders == 'z':
                    if self.gobackflag:
                        self.cubelist[selectpos].ChangeZG()
                        self.cubelist[selectpos].ChangeZG()
        self.texchanged = True
            
    def _Go(self,param):
        #print "_Go"
        #print self.selectlst
        self._ChangeTex(False)
        for selectpos in self.selectlst:
            if self.keyboard > 0 and self.keyboard <= 3:
                self.cubelist[selectpos].sx += self.spinspeed
            elif self.keyboard > 3 and self.keyboard <= 6:
                self.cubelist[selectpos].sy += self.spinspeed
            elif self.keyboard > 6 and self.keyboard <= 9:
                self.cubelist[selectpos].sz += self.spinspeed

        self.angle += self.spinspeed
        glutPostRedisplay()

        if self.angle == 90:
            self.angle = 0
            self.spinning = False
            self._ChangeTex(True)
            for selectpos in self.selectlst:
                self.cubelist[selectpos].SetSXYZ(0,0,0)
                self.cubelist[selectpos].SetOrders('n')
        else:
            glutTimerFunc(20,self._Go,1)
            
    def _Exchange(self):
        #execlst = self.selectlst
        execlst = copy.deepcopy(self.cubelist)
        
        for cube in self.cubelist:
            cube.SetSXYZ(0,0,0)    

        #self._PrintCubeThing()
        for j in range(0,3):
            for k in range(0,3):
                despos = -1
                srcpos = -1
                if self.keyboard > 0 and self.keyboard <= 3:
                    i = self.keyboard - 1
                    #print "i-1",self._GetCubePos(i,j,k),self._GetCubePos(i,k,2-j)
                    despos = self._GetCubePos(i,j,k)
                    srcpos = self._GetCubePos(i,k,2-j)
                    #self.cubelist[self._GetCubePos(i,j,k)].SetNum(self._GetCubePos(i,k,2-j))
                elif self.keyboard > 3 and self.keyboard <= 6:
                    i = self.keyboard - 4
                    #print "i-2",self._GetCubePos(j,i,k),self._GetCubePos(2-k,i,j)
                    despos = self._GetCubePos(j,i,k)
                    srcpos = self._GetCubePos(2-k,i,j)
                    #self.cubelist[self._GetCubePos(j,i,k)].SetNum(self._GetCubePos(2-k,i,j))
                elif self.keyboard > 6 and self.keyboard <= 9:
                    i = self.keyboard - 7
                    #print "i-3",self._GetCubePos(k,j,i),self._GetCubePos(j,2-k,i)
                    despos = self._GetCubePos(k,j,i)
                    srcpos = self._GetCubePos(j,2-k,i)
                    #self.cubelist[self._GetCubePos(k,j,i)].SetNum(self._GetCubePos(j,2-k,i))
                if despos >= 0 and srcpos >= 0:
                    self.cubelist[despos] = execlst[despos]
                    #self.cubelist[despos].SetNum(srcpos)
        #self._PrintCubeThing()
        
    def CubeTransform(self,keyboard):
        self.keyboard = int(keyboard)
        self.spinning = True
        self.texchanged = False
        self._Select()
        self._Go(1)
        self._Exchange()
