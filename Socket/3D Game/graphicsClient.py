import pygame, sys, math
from socket import *






def rotate2d(pos,rad):
    x,y=pos
    s,c = math.sin(rad), math.cos(rad)
    return x*c-y*s,y*c+x*s

class Cam:
    def __init__(self,pos=(0,0,0),rot=(0,0)):
        self.pos = list(pos)
        self.rot = list(rot)

    def events(self,event):
        if event.type == pygame.MOUSEMOTION:
            x,y = event.rel
            x/=200; y/=200
            self.rot[0]+=y; self.rot[1]+=x
    def update(self, dt, key):
        s = dt * 5

        if key[pygame.K_q]: self.pos[1]+=s
        if key[pygame.K_e]: self.pos[1]-=s

        x,y = s*math.sin(self.rot[1]), s*math.cos(self.rot[1])

        if key[pygame.K_w]: self.pos[0]+=x; self.pos[2]+=y
        if key[pygame.K_s]: self.pos[0]-=x; self.pos[2]-=y

        if key[pygame.K_a]: self.pos[0]-=y; self.pos[2]+=x
        if key[pygame.K_d]: self.pos[0]+=y; self.pos[2]-=x
        


class Cube:
    vertices = (-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)
    faces = (0,1,2,3),(4,5,6,7),(0,1,5,4),(2,3,7,6),(0,3,7,4),(1,2,6,5)
    colors = (255,0,0), (255,128,0), (255,255,0), (255,255,255), (0,0,255), (0,255,0)
    
    def __init__(self,pos=(0,0,0)):
        x,y,z = pos
        self.vertices = [(x+X/2,y+Y/2,z+Z/2) for X,Y,Z in self.vertices]
        

pygame.init()
w, h = 1280, 720; cx, cy = w//2, h//2; fov = min(w,h)
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()


cam = Cam((0,0,-5))

pygame.event.get(); pygame.mouse.get_rel()
pygame.mouse.set_visible(0); pygame.event.set_grab(1)

cubes = [Cube((0,0,0)), Cube((-2,0,0)), Cube((2,0,0))]
i = 0
while True:
    # serverstuff
    serverName = "192.168.1.69"
    serverPort = 12000
    
    
    
    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    dt = clock.tick()/1000
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: pygame.quit(); sys.exit()
        cam.events(event)

    screen.fill((0,0,0))
    face_list = [];  face_color = []; depth = []

    for obj in cubes:

        vert_list = []; screen_coords = []
        for x,y,z in obj.vertices:
            x-=cam.pos[0]; y-=cam.pos[1];z-=cam.pos[2]
            x,z = rotate2d((x,z),cam.rot[1])
            y,z = rotate2d((y,z),cam.rot[0])

            vert_list += [(x,y,z)]
        
            f = fov/z
            x,y = x*f,y*f
            screen_coords+=[(cx+int(x),cy+int(y))]     

    

        for f in range(len(obj.faces)):
            face = obj.faces[f]
            on_screen = False
            for i in face:
                x,y = screen_coords[i]
                if vert_list[i][2]>0 and x>0 and x<w and y>0 and y<h: on_screen = True; break
        
            if on_screen:
                coords = [screen_coords[i] for i in face]
                face_list +=[coords]
                face_color +=[obj.colors[f]]

                depth += [sum(sum(vert_list[j][i] for j in face)**2 for i in range(3))]

    order = sorted(range(len(face_list)), key=lambda i: depth[i], reverse=True)

    for i in order:
        try:pygame.draw.polygon(screen, face_color[i], face_list[i])
        except:pass
    pygame.display.flip()

    key = pygame.key.get_pressed()
    cam.update(dt,key)
    sentence = str(cam.pos)
    
    clientSocket.send(sentence.encode())
    pos_new = clientSocket.recv(1024).decode().split()
    
    x = float(pos_new[0].strip("[,"))

    cubes[0] = Cube((-x,1,1))


    clientSocket.close()

