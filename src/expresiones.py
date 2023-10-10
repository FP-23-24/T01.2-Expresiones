from collections import namedtuple

# Definición del tipo Persona:
# nombre: Nombre de la persona.
# edad: Edad de la persona en años.
# tiene_licencia: Booleano que indica si la persona tiene licencia de conducir.
# hobbies: Conjunto de hobbies o actividades que le gustan a la persona.
# paises_visitados: Conjunto de países que la persona ha visitado.
# libros_leidos: Lista de libros que la persona ha leído en orden de lectura.
Persona = namedtuple('Persona', ['nombre', 'edad', 'tiene_licencia', 'hobbies', 'paises_visitados', 'libros_leidos'])

juan = Persona('Juan', 20, True, {'fútbol', 'cine'}, {'España', 'Chile'}, ['Don Quijote', 'El Principito'])
maria = Persona('Maria', 15, False, {'lectura', 'música', 'cine'}, {'Francia', 'Chile'}, ['El Principito', '1984'])
pedro = Persona('Pedro', 17, True, {'fútbol', 'natación'}, {'México'}, ['Cien Años de Soledad', 'Moby Dick', '1984'])


print("¿Juan tiene más de 18 años?:",
    #TODO
)

print("¿Maria tiene licencia de conducir?:",
    #TODO
)

print("¿Juan ha visitado Chile?:",
    #TODO
)

print("¿A María le gustan el cine y la música?:",
    #TODO
)

print("¿'El Principito' es el último libro que ha leído Maria?:",
    #TODO
)

print("Ni Juan ni Pedro tienen licencia de conducir:",
    #TODO
)

print("¿Maria ha leído al menos 2 libros?:",
    #TODO
)

print("¿María no ha visitado México, pero Pedro sí?:",
    #TODO
)

print("¿Juan ha leído más libros que María pero menos que Pedro?:",
    #TODO
)

print("¿Pedro no ha visitado Chile y tampoco le gusta el cine?:",
    #TODO
)

print("¿El último libro que María ha leído es '1984' y Juan no lo ha leído aún?:",
    #TODO
)

print("¿Pedro ha visitado más países que Juan o ha leído más libros que María?:",
    #TODO
)

print("¿María tiene licencia de conducir o ha leído 'Moby Dick', pero no ambas cosas?",
    #TODO
)

print("¿Juan ha visitado España o Francia, pero no ambos?",
    #TODO
)