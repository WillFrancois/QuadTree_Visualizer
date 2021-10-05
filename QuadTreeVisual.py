import pygame
import sys
import QuadTree

rect_list = []
quadtree = QuadTree.QuadTree(0, 0, 700, 700, 2, rect_list)
rect_list.append(quadtree)
point_list = []
checking = False

pygame.init()
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("QuadTree Visualization")

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        #Keeping the mouse position for multiple checks
        mouse_pos = pygame.mouse.get_pos()

        #Quit Visualizer
        if event.type == pygame.QUIT:
            sys.exit()
        
        #Mouse Button inputs
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Handle point additions
            if pygame.mouse.get_pressed()[0] == True:
                quadtree.insert(QuadTree.Point(mouse_pos[0], mouse_pos[1]))
                point_list.append(QuadTree.Point(mouse_pos[0], mouse_pos[1]))
            if pygame.mouse.get_pressed()[2] == True:
                checking = not checking

    #Render rectangles
    for i in rect_list:
        pygame.draw.rect(screen,(255,255,255), pygame.rect.Rect(i.x,i.y,i.w,i.h))
        #Border drawing in Pygame is not very fun.
        pygame.draw.rect(screen,(0,0,0), pygame.rect.Rect(i.x,i.y,i.w,1))
        pygame.draw.rect(screen,(0,0,0), pygame.rect.Rect(i.x,i.y,1,i.h))
        pygame.draw.rect(screen,(0,0,0), pygame.rect.Rect(i.x+i.w-1,i.y,1,i.h))
        pygame.draw.rect(screen,(0,0,0), pygame.rect.Rect(i.x,i.y+i.h-1,i.w,1))
        

    #Render points
    if(len(point_list) > 0):
        for j in (point_list):
            pygame.draw.circle(screen, (0,0,0), (j.x, j.y), 5)

    #Check for collisions when checking
    if checking:
        colliding_points, colliding_quads = quadtree.query(rect_list, mouse_pos[0]-50, mouse_pos[1]-50, 100, 100)
        for i in colliding_points:
            pygame.draw.circle(screen, (0,255,0), (i.x, i.y), 5)
        for i in colliding_quads:
            pygame.draw.rect(screen,(0,255,0), pygame.rect.Rect(i.x,i.y,i.w,1))
            pygame.draw.rect(screen,(0,255,0), pygame.rect.Rect(i.x,i.y,1,i.h))
            pygame.draw.rect(screen,(0,255,0), pygame.rect.Rect(i.x+i.w-1,i.y,1,i.h))
            pygame.draw.rect(screen,(0,255,0), pygame.rect.Rect(i.x,i.y+i.h-1,i.w,1))

    pygame.display.update()