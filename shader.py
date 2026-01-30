from OpenGL.GL import *

vertex_shader_src = """
#version 330 core
layout (location = 0) in vec2 aPos;

uniform float scale;

void main()
{
    gl_Position = vec4(aPos * scale, 0.0, 1.0);
}
"""

wpote_shader_src = """
#version 330 core

out vec4 FragColor;

uniform vec3 color;
void main()
{
    //FragColor = vec4(0, 0.6, 0, 1.0); // Green color
    FragColor = vec4(color, 0.4);
}
"""

def compile_shader(shader_type, source):
    shader = glCreateShader(shader_type)
    glShaderSource(shader, source)
    glCompileShader(shader)

    if glGetShaderiv(shader, GL_COMPILE_STATUS) != GL_TRUE:
        raise RuntimeError(glGetShaderInfoLog(shader).decode())

    return shader

def create_shader_program():
    vertex_shader = compile_shader(GL_VERTEX_SHADER, vertex_shader_src)
    wpote_shader = compile_shader(GL_FRAGMENT_SHADER, wpote_shader_src)

    shader_program = glCreateProgram()
    glAttachShader(shader_program, vertex_shader)
    glAttachShader(shader_program, wpote_shader)
    glLinkProgram(shader_program)

    if glGetProgramiv(shader_program, GL_LINK_STATUS) != GL_TRUE:
        raise RuntimeError(glGetProgramInfoLog(shader_program).decode())

    glDeleteShader(vertex_shader)
    glDeleteShader(wpote_shader)

    return shader_program
