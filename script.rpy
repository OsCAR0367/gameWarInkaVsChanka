# script.rpy - Visual Novel Insirapa (Perú, Incas y Chancas)

init python:
    favor_inca = 0
    favor_chanca = 0
    hizo_ritual_inca = False
    hizo_ritual_chanca = False
    conoce_secreto = False
    herido = False
    amigo_inca = False
    amigo_chanca = False
    respeto_abuela = False
    traiciono = False
    sobrevivio_pueblo = False

define p = Character("Insirapa")
define m = Character("Mama Quilla", color="#b4a7d6")
define c = Character("Capitán Chanca", color="#d99795")
define i = Character("Inca", color="#f7ca18")
define abuela = Character("Abuela", color="#bada55")
define amigo1 = Character("Tupaq", color="#74b9ff")
define amiga2 = Character("Killa", color="#fdcb6e")

label start:
    scene black
    with fade

    p "Me llamo Insirapa. Mi madre es inca y mi padre chanca. En mis venas, la guerra y la esperanza luchan."
    abuela "Hijo mío, el destino te ha puesto entre dos fuegos."
    p "Hoy inicia el festival de la cosecha. ¿A quién ayudarás primero?"

    menu:
        "Ayudar en el ritual inca":
            $ favor_inca += 1
            $ hizo_ritual_inca = True
            jump cap1_ayuda_inca

        "Ayudar en el ritual chanca":
            $ favor_chanca += 1
            $ hizo_ritual_chanca = True
            jump cap1_ayuda_chanca

        "Ir al bosque a solas":
            jump cap1_bosque

label cap1_ayuda_inca:
    scene bg_inca_templo
    i "Bienvenido, Insirapa. Acompáñanos en la ceremonia del Sol. Tu ayuda es valiosa."
    amiga2 "¿Me ayudas a preparar la ofrenda?"
    menu:
        "Ayudar a Killa con la ofrenda":
            $ amigo_inca = True
            p "Trabajo con Killa, aprendiendo sobre los símbolos sagrados y la fe inca."
        "Ir con los ancianos a escuchar historias":
            p "Los sabios incas me enseñan cantos antiguos y secretos del pueblo."
    jump cap1_amistades

label cap1_ayuda_chanca:
    scene bg_chanca_aldea
    c "¡Hijo del valle, acércate al altar de la Luna!"
    amigo1 "¿Me ayudas a buscar plantas medicinales?"
    menu:
        "Ir con Tupaq a recolectar plantas":
            $ amigo_chanca = True
            p "Aprendo sobre hierbas curativas y la magia de la naturaleza con Tupaq."
        "Quedarte en la plaza para la danza guerrera":
            p "Participo en la danza chanca. Siento el ritmo y el espíritu ancestral."
    jump cap1_amistades

label cap1_bosque:
    scene bg_bosque
    abuela "En la soledad, puedes escuchar a los ancestros. Escuchas un susurro antiguo..."
    $ conoce_secreto = True
    p "Algo en el bosque me revela un misterio oculto sobre mi linaje."
    jump cap1_amistades

label cap1_amistades:
    scene bg_fogata
    m "La noche cae y los rumores de guerra crecen. Los tambores no dejan dormir."
    amigo1 "Insirapa, escuché que los incas planean atacar el pueblo chanca."
    amiga2 "Oí que los chancas quieren sabotear el festival inca."
    menu:
        "Advertir a los incas del ataque chanca":
            $ favor_inca += 1
            jump cap2_avisa_inca

        "Advertir a los chancas del ataque inca":
            $ favor_chanca += 1
            jump cap2_avisa_chanca

        "Guardar el secreto y no avisar":
            $ traiciono = True
            jump cap2_guarda_secreto

label cap2_avisa_inca:
    scene bg_inca_templo
    i "Gracias, Insirapa. Tu lealtad nos ha salvado. ¿Vendrás a la ceremonia sagrada esta noche?"
    menu:
        "Asistir a la ceremonia":
            $ respeto_abuela = True
            jump cap2_ritual_inca
        "No asistir, explorar el pueblo":
            jump cap2_explora_inca

label cap2_ritual_inca:
    scene bg_fuego
    i "Recibe la bendición del Inti. Eres parte de nosotros."
    $ hizo_ritual_inca = True
    p "Siento una fuerza recorrer mi cuerpo. Un nuevo poder despierta."
    jump cap3_conflicto

label cap2_explora_inca:
    scene bg_pueblo
    amiga2 "¿Por qué no fuiste a la ceremonia? Algunos te miran con desconfianza."
    p "Mi lugar en este pueblo es incierto."
    jump cap3_conflicto

label cap2_avisa_chanca:
    scene bg_chanca_aldea
    c "Tu aviso llegó justo a tiempo. Los incas fueron detenidos."
    menu:
        "Celebrar con los guerreros chancas":
            $ respeto_abuela = True
            jump cap2_ritual_chanca
        "Quedarte con Tupaq en el bosque":
            jump cap2_bosque_chanca

label cap2_ritual_chanca:
    scene bg_luna
    c "La luna te guía. Te damos la protección de los ancestros."
    $ hizo_ritual_chanca = True
    p "El canto del chamán me conecta con fuerzas antiguas."
    jump cap3_conflicto

label cap2_bosque_chanca:
    scene bg_bosque
    amigo1 "Entre los árboles encuentro paz, lejos de la guerra."
    p "Quizá aquí descubra mi verdadero destino."
    jump cap3_conflicto

label cap2_guarda_secreto:
    scene bg_pueblo_arrasado
    p "No advertí a nadie. El ataque ocurrió y muchos sufrieron."
    $ herido = True
    abuela "Tu silencio tiene consecuencias. Aprende de tu dolor."
    jump cap3_conflicto

label cap3_conflicto:
    scene bg_camino
    abuela "Los dioses te pusieron a prueba. Debes ir al templo escondido. Allí sabrás quién eres."
    menu:
        "Ir solo al templo":
            jump cap3_templo_solo
        "Ir con Tupaq, tu amigo chanca":
            jump cap3_templo_tupaq
        "Ir con Killa, tu amiga inca":
            jump cap3_templo_killa

label cap3_templo_solo:
    scene bg_templo
    p "El camino es peligroso. Un jaguar me ataca."
    menu:
        "Luchar contra el jaguar":
            if herido:
                p "Estoy débil y el jaguar me hiere gravemente, pero logro llegar al templo."
            else:
                p "Lucho con valentía y el jaguar huye. El camino está libre."
            jump cap4_ritual

        "Escapar y buscar otra ruta":
            p "Encuentro un sendero oculto. Llego tarde, pero intacto."
            jump cap4_ritual

label cap3_templo_tupaq:
    scene bg_templo
    amigo1 "Juntos enfrentamos los peligros y llegamos al templo sanos."
    $ amigo_chanca = True
    jump cap4_ritual

label cap3_templo_killa:
    scene bg_templo
    amiga2 "Con Killa supero las pruebas. Su fe me fortalece."
    $ amigo_inca = True
    jump cap4_ritual

label cap4_ritual:
    scene bg_templo_interior
    abuela "Has llegado al lugar de los secretos. Ahora debes elegir: ¿A quién honrarás con el gran ritual?"
    if conoce_secreto:
        menu:
            "Realizar el Ritual de la Unión (incas y chancas)":
                jump final_union
            "Ritual solo para los incas":
                jump final_inca
            "Ritual solo para los chancas":
                jump final_chanca
            "Rechazar el ritual y buscar tu propio camino":
                jump final_solitario
    else:
        menu:
            "Ritual para los incas":
                jump final_inca
            "Ritual para los chancas":
                jump final_chanca
            "No hacer ritual":
                jump final_solitario

# FINALES

label final_union:
    if hizo_ritual_inca and hizo_ritual_chanca and amigo_inca and amigo_chanca:
        scene bg_amanecer
        p "El poder de ambos pueblos fluye en mí. El gran Ritual de la Unión funciona: Incas y Chancas, por fin, firman la paz."
        abuela "Has cambiado el destino del mundo, Insirapa."
    else:
        scene bg_noche
        p "Intenté unirlos, pero la desconfianza es grande. Sin embargo, ahora hay esperanza."
        abuela "Sembraste una semilla que algún día crecerá."
    jump creditos

label final_inca:
    if favor_inca > favor_chanca:
        scene bg_inca_templo
        i "Eres un hijo del Sol. Nuestra gloria es tuya."
        p "Me convierto en líder inca, pero parte de mí extraña mi raíz chanca."
    else:
        scene bg_inca_templo
        i "Aceptamos tu ayuda, pero nunca olvidarás la división."
        p "Siento el peso de la traición."
    jump creditos

label final_chanca:
    if favor_chanca > favor_inca:
        scene bg_chanca_aldea
        c "La sangre chanca es fuerte en ti. Nos guiarás a la victoria."
        p "Encuentro mi hogar entre los chancas, pero nunca olvido mi otra mitad."
    else:
        scene bg_chanca_aldea
        c "La lealtad es frágil como el humo. Eres uno más, pero nunca un hermano verdadero."
        p "Sigo buscando mi lugar en el mundo."
    jump creditos

label final_solitario:
    scene bg_bosque
    p "Rechacé la senda de la guerra y la unión. Busco respuestas en el silencio del bosque, lejos de todos."
    abuela "A veces, el mayor valor es renunciar a elegir. El futuro es incierto."
    jump creditos

label creditos:
    scene black
    with fade
    "FIN - Gracias por descubrir la historia de Insirapa."
    return
