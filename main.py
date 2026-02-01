import pygame
from pygame.locals import *
from OpenGL.GL import *
import config
from shader import create_shader_program
from tefitti import *
from deleteimmogad import passmonga

def main():
    pygame.init()
    display = (config.DISPLAY_WIDTH, config.DISPLAY_HEIGHT)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glClearColor(*config.BACKGROUND_COLOR)

    shader_program = create_shader_program()
    
    VAO_wp, EBO_wp, wp_index_count = tefitti_left_eye()
    VAO_iris, EBO_iris, iris_index_count = tefitti_left_iris()
    VAO_pupil, EBO_pupil, pupil_index_count = tefitti_left_pupil()
    f=0
    index=[]
    vertices=[]
    VAO_byline=None
    EBO_byline=None
    byline_index_count=None
    
    for x in np.arange(-10,10.02,0.02):
        for y in np.arange(10,9.96,-0.02):
            index.extend([f])
            vertices.extend([x,y])
            f+=1
            if x<=8.6 and y>=9.98:
                r=0.353
                g=0.851
                b=0.988
            else:
                r=0.129
                g=0.682
                b=0.392
            if f==3:
                passmonga(vertices,index)
                VAO_byline, EBO_byline, byline_index_count = byline()
    
    
    glUseProgram(shader_program)
    scale_loc=glGetUniformLocation(shader_program,"scale")
    color_loc=glGetUniformLocation(shader_program, "color")
    
    scale=0.095
    

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                    
        glClear(GL_COLOR_BUFFER_BIT)
        
        glUseProgram(shader_program)
        
        glUniform1f(scale_loc,scale)
        
        glUniform3f(color_loc,0.345, 0.812, 0.353)
        glBindVertexArray(VAO_wp)
        glDrawElements(GL_TRIANGLE_FAN, wp_index_count, GL_UNSIGNED_INT, None)

        glUniform3f(color_loc,0.008, 0.302, 0.043)
        glBindVertexArray(VAO_iris)
        glDrawElements(GL_TRIANGLE_FAN, iris_index_count, GL_UNSIGNED_INT, None)

        glUniform3f(color_loc,0.027, 0.086, 0.067)
        glBindVertexArray(VAO_pupil)
        glDrawElements(GL_TRIANGLE_FAN, pupil_index_count, GL_UNSIGNED_INT, None)
        
        glUniform3f(color_loc,0,0,0)
        glBindVertexArray(VAO_byline)
        glDrawElements(GL_TRIANGLES, byline_index_count, GL_UNSIGNED_INT, None)
        
        glBindVertexArray(0)
        pygame.display.flip()
        clock.tick(config.FPS)
    
    glDeleteVertexArrays(1, [VAO_wp])
    glDeleteBuffers(1, [EBO_wp])

    glDeleteVertexArrays(1, [VAO_iris])
    glDeleteBuffers(1, [EBO_iris])

    glDeleteVertexArrays(1, [VAO_pupil])
    glDeleteBuffers(1, [EBO_pupil])
    
    glDeleteVertexArrays(1, [VAO_byline])
    glDeleteBuffers(1, [EBO_byline])
    
    glDeleteProgram(shader_program)
    pygame.quit()

if __name__ == "__main__":
    main()
