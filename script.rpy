# ========================================
# RUTA DE DERROTA: DIPLOMACIA INGENUA
# ========================================

label final_diplomacia_ingenua:
    scene bg chanca_camp with fade
    show war_red with fade
    
    narrator "Decides enviar embajadores para negociar con los chankas. Los emisarios regresan con sus cabezas cortadas como respuesta."
    
    show uscovilca fierce
    
    uscovilca "¡No vine aquí a hablar! ¡Vine a conquistar!"
    
    narrator ""
    narrator "{color=#8B0000}{b}LECCIÓN HISTÓRICA{/b}{/color}"
    narrator "Los chankas eran guerreros que buscaban gloria en batalla, no diplomáticos. Tu error fue malinterpretar completamente sus intenciones. Uscovilca había planeado esta guerra durante años específicamente para destruir el poder inca."
    narrator ""
    narrator "{color=#CD853F}{b}ANÁLISIS{/b}{/color}"
    narrator "Tu error principal fue diplomacia ingenua ante enemigos irreconciliables. Un líder debe saber cuándo es imposible negociar."
    
    scene black with fade
    "FINAL: EL DIPLOMÁTICO INGENUO - Perdiste tiempo crucial en negociaciones imposibles."
    
    jump reiniciar

# ========================================
# EL ASCENSO DE PACHACUTEC
# La Guerra que Forjó el Imperio Inca (1430-1438 d.C.)
# ========================================

# === TRANSICIONES DEFINIDAS ===
define flash = Fade(0.1, 0.0, 0.5, color="#ffffff")
define golden_flash = Fade(0.2, 0.0, 0.8, color="#FFD700")
define war_flash = Fade(0.3, 0.0, 0.5, color="#8B0000")
define mystical_fade = Fade(0.5, 0.2, 0.8, color="#9370DB")

# === IMÁGENES DEL JUEGO ===
image black = Solid("#000000")
image white = Solid("#ffffff")
image golden_light = Solid("#FFD700", xsize=1920, ysize=1080)
image war_red = Solid("#8B0000", xsize=1920, ysize=1080)
image mystical_glow = Solid("#9370DB", xsize=1920, ysize=1080)

# Fondos históricos
image bg cusco_palace = Solid("#8B4513")
image bg cusco_plaza = Solid("#DAA520")
image bg yahuar_pampa = Solid("#A0522D")
image bg coricancha = Solid("#FFD700")
image bg andean_mountains = Solid("#708090")
image bg chanca_camp = Solid("#654321")
image bg royal_chamber = Solid("#CD853F")
image bg war_council = Solid("#8B7355")
image bg ritual_site = Solid("#9370DB")
image bg calca_refuge = Solid("#696969")
image bg battlefield_dawn = Solid("#FF6347")
image bg victory_plaza = Solid("#32CD32")

# Personajes históricos
image cusi neutral = Solid("#4169E1", xsize=300, ysize=600)
image cusi determined = Solid("#0000CD", xsize=300, ysize=600)
image cusi warrior = Solid("#191970", xsize=300, ysize=600)
image cusi inca = Solid("#4B0082", xsize=300, ysize=600)

image viracocha worried = Solid("#8B4513", xsize=300, ysize=600)
image viracocha fleeing = Solid("#696969", xsize=300, ysize=600)

image urco arrogant = Solid("#CD853F", xsize=300, ysize=600)
image urco coward = Solid("#A0522D", xsize=300, ysize=600)

image uscovilca fierce = Solid("#8B0000", xsize=300, ysize=600)
image uscovilca commanding = Solid("#DC143C", xsize=300, ysize=600)

image willaq_umu ceremonial = Solid("#4B0082", xsize=300, ysize=600)
image apo_mayta_loyal = Solid("#2F4F4F", xsize=300, ysize=600)
image noble_advisor = Solid("#8B7D6B", xsize=300, ysize=600)

# === PERSONAJES HISTÓRICOS ===
define cusi = Character("Cusi Yupanqui", 
                       color="#4169E1",
                       what_prefix='"',
                       what_suffix='"')

define viracocha = Character("Inca Viracocha", 
                           color="#8B4513",
                           what_prefix='"',
                           what_suffix='"')

define urco = Character("Príncipe Urco", 
                      color="#CD853F",
                      what_prefix='"',
                      what_suffix='"')

define uscovilca = Character("Uscovilca - Líder Chanca", 
                           color="#8B0000",
                           what_prefix='"',
                           what_suffix='"')

define willaq_umu = Character("Willaq Umu - Sumo Sacerdote", 
                            color="#4B0082",
                            what_prefix='"',
                            what_suffix='"')

define apo_mayta = Character("Apo Mayta - General Leal", 
                           color="#2F4F4F",
                           what_prefix='"',
                           what_suffix='"')

define advisor = Character("Consejero Real", 
                         color="#8B7D6B",
                         what_prefix='"',
                         what_suffix='"')

define narrator = Character(None, color="#8B4513")

# === VARIABLES DEL JUEGO ===
default puntos_liderazgo = 0
default apoyo_popular = 0
default alianzas_etnias = 0
default poder_ritual = 0
default estrategia_militar = 0
default legitimidad_real = 0

# Variables de decisiones críticas para el final
default defendio_cusco = False
default pidio_ayuda_aliados = False
default realizo_rituales_completos = False
default uso_estrategia_correcta = False
default lidero_personalmente = False

# Variables para finales educativos
default error_principal = ""
default leccion_aprendida = ""

# ========================================
# PRÓLOGO: LA AMENAZA SE ACERCA
# ========================================

label start:
    scene black with fade
    
    narrator ""
    narrator "{color=#FFD700}{b}CONTEXTO HISTÓRICO{/b}{/color}"
    narrator "Año 1430 d.C. - Cusco, corazón del mundo andino. Los chasquis llegan con noticias terribles: Un ejército de 40,000 guerreros chankas marcha hacia Cusco. Su líder, Uscovilca, ha jurado beber chicha de los cráneos incas. El terror se extiende por la ciudad sagrada."
    
    scene bg cusco_plaza with fade
    show golden_light with mystical_fade
    
    narrator ""
    narrator "{color=#4169E1}{b}TU IDENTIDAD{/b}{/color}"
    narrator "Eres Cusi Yupanqui, hijo menor del Inca Viracocha. No eres el heredero designado, pero el destino te llamará a grandeza. Lo que decidas determinará si serás recordado como un príncipe obediente... o como Pachacutec, el transformador del mundo."
    
    show viracocha worried
    
    viracocha "¡Los chankas vienen como una tormenta de guerra!"
    viracocha "Son demasiados. Debemos huir a Calca inmediatamente."
    
    show urco arrogant at right
    
    urco "Mi padre tiene razón. Yo soy el heredero y ordeno la retirada."
    urco "Cusi, nos acompañarás. No hay honor en una muerte inútil."
    
    scene bg royal_chamber with dissolve
    
    jump primera_decision

# ========================================
# PRIMERA DECISIÓN: HUIR O RESISTIR
# ========================================

label primera_decision:
    scene bg royal_chamber with fade
    
    show cusi neutral
    
    narrator "Tu padre y hermano esperan tu respuesta."
    narrator "La decisión que tomes marcará el rumbo de la historia andina."
    
    menu:
        "¿Qué decides, Cusi Yupanqui?"
        
        "Seguir el consejo de mi padre y buscar refugio seguro":
            $ apoyo_popular -= 3
            $ legitimidad_real -= 2
            $ error_principal = "huir_de_cusco"
            cusi "Padre, tu experiencia y sabiduría me guían. Busquemos refugio."
            jump final_huida
            
        "Proponer quedarse a defender el Cusco":
            $ defendio_cusco = True
            $ puntos_liderazgo += 3
            $ apoyo_popular += 2
            $ legitimidad_real += 2
            cusi "Propongo que la corte se retire, pero yo me quedo con quien quiera resistir."
            cusi "Alguien debe defender la ciudad sagrada de nuestros ancestros."
            jump resistencia_cusco
            
        "Sugerir negociar primero antes de tomar decisiones drásticas":
            $ error_principal = "diplomacia_ingenua"
            $ legitimidad_real -= 1
            cusi "Quizás podamos evitar el derramamiento de sangre con diplomacia."
            jump final_diplomacia_ingenua

# ========================================
# RUTA DE DERROTA: HUIDA A CALCA
# ========================================

label final_huida:
    scene bg calca_refuge with fade
    show war_red with fade
    
    narrator "Acompañas a tu padre y hermano en la huida hacia Calca."
    narrator "Detrás de ustedes, Cusco arde bajo las antorchas chankas."
    
    show viracocha fleeing
    
    viracocha "Salvamos nuestras vidas, Cusi. Eso es lo importante."
    
    scene bg cusco_plaza with dissolve
    show war_red with war_flash
    
    narrator "{b}CONSECUENCIAS DE LA HUIDA:{/b} Cusco cae sin resistencia, miles de cusqueños son masacrados, el Coricancha es profanado, las etnias aliadas pierden fe en el liderazgo inca, Uscovilca se proclama señor de los Andes."
    
    narrator ""
    narrator "{color=#8B0000}{b}LECCIÓN HISTÓRICA{/b}{/color}"
    narrator "En el mundo andino, un líder que abandona su capital pierde legitimidad para siempre. La huida de Viracocha y Urco los deslegitimó ante todo el imperio. El pueblo necesita ver valor en sus gobernantes."
    narrator ""
    narrator "{color=#CD853F}{b}ANÁLISIS{/b}{/color}"
    narrator "Tu error principal fue huir cuando debías liderar. Un inca que salva su vida pero pierde su capital, no es digno del trono."
    
    scene black with fade
    
    "FINAL: EL PRÍNCIPE COBARDE"
    "Has perdido la oportunidad de convertirte en Pachacutec."
    "¿Quieres intentar nuevamente con honor?"
    
    jump reiniciar

# ========================================
# RESISTENCIA EN CUSCO
# ========================================

label resistencia_cusco:
    scene bg cusco_plaza with fade
    show golden_light with mystical_fade
    
    show viracocha worried
    
    viracocha "¡Cusi! ¿Te has vuelto loco? ¡Son cuarenta mil guerreros!"
    
    show cusi determined
    
    cusi "Padre, los dioses nos miran desde las montañas sagradas."
    cusi "No puedo traicionar la confianza del pueblo que ve en mí un líder."
    
    show urco arrogant at right
    
    urco "Entonces muere como un necio, hermano menor."
    urco "Yo seré un heredero vivo, no un mártir muerto."
    
    narrator "Tu padre y hermano parten hacia Calca con una pequeña corte."
    narrator "Pero tu decisión de quedarte inspira a los nobles leales."
    
    show apo_mayta_loyal
    
    general "Príncipe Cusi, si usted resiste, nosotros también."
    general "Cusco merece una defensa digna de su gloria."
    
    show noble_advisor
    
    advisor "Los canchis y ayarmacas respetan su valor, mi señor."
    advisor "Quizás respondan a un llamado de auxilio."
    
    $ apoyo_popular += 1
    
    jump segunda_decision

# ========================================
# SEGUNDA DECISIÓN: BUSCAR ALIANZAS
# ========================================

label segunda_decision:
    scene bg war_council with fade
    
    show cusi determined
    
    narrator "Has tomado la decisión heroica de resistir."
    narrator "Pero Cusco tiene apenas 8,000 guerreros contra 40,000 chankas."
    narrator "La valentía sola no será suficiente."
    
    show advisor
    
    advisor "Príncipe, nuestros chasquis están listos para partir."
    advisor "¿Enviamos mensajes pidiendo refuerzos a las etnias aliadas?"
    
    menu:
        "¿Cuál es tu estrategia de alianzas?"
        
        "Enviar mensajeros discretos a líderes locales de confianza":
            $ pidio_ayuda_aliados = True
            $ alianzas_etnias += 4
            $ puntos_liderazgo += 3
            cusi "Enviemos chasquis a los curacas que han mostrado lealtad tradicional."
            cusi "Los canchis y ayarmacas comprenderán la gravedad de la situación."
            jump alianzas_exitosas
            
        "Concentrar fuerzas cusqueñas y confiar en la superioridad espiritual":
            $ error_principal = "orgullo_excesivo"
            $ alianzas_etnias -= 2
            cusi "Los descendientes directos de Inti no necesitan ayuda externa."
            cusi "Nuestro linaje divino compensará cualquier desventaja numérica."
            jump final_orgullo
            
        "Ofrecer tributos especiales a cambio de mercenarios neutrales":
            $ error_principal = "estrategia_equivocada"
            $ legitimidad_real -= 2
            cusi "Podríamos contratar guerreros de etnias neutrales con oro y textiles."
            jump final_corrupcion

# ========================================
# RUTA DE DERROTA: ORGULLO EXCESIVO
# ========================================

label final_orgullo:
    scene bg yahuar_pampa with fade
    show war_red with war_flash
    
    narrator "Decides confiar solo en el valor cusqueño."
    narrator "Tu orgullo inca rechaza la ayuda de 'pueblos menores'."
    
    show general_loyal
    
    apo_mayta "Príncipe, con todo respeto, necesitamos refuerzos urgentemente."
    
    show cusi neutral
    
    cusi "No. Los descendientes de Manco Capac no mendigan ayuda."
    
    scene bg yahuar_pampa with dissolve
    show war_red with war_flash
    
    narrator "La batalla es breve y sangrienta."
    narrator "8,000 valientes cusqueños contra 40,000 chankas enfurecidos."
    narrator "El resultado es una masacre heroica pero inútil."
    
    narrator ""
    narrator "{color=#8B0000}{b}LECCIÓN HISTÓRICA{/b}{/color}"
    narrator "Pachacutec histórico pidió ayuda a todas las etnias disponibles. El orgullo desmedido arruina a los grandes líderes."
    narrator ""
    narrator "{color=#CD853F}{b}ANÁLISIS{/b}{/color}"
    narrator "Tu error fue orgullo que impidió alianzas necesarias. La grandeza no está en luchar solo, sino en saber cuándo pedir ayuda."
    
    scene black with fade
    
    "FINAL: EL HÉROE ORGULLOSO"
    "Tu valor era incuestionable, pero tu estrategia fue desastrosa."
    
    jump reiniciar

# ========================================
# RUTA DE DERROTA: ESTRATEGIA EQUIVOCADA
# ========================================

label final_corrupcion:
    scene bg chanca_camp with fade
    show war_red with fade
    
    narrator "Intentas corromper a los jefes chankas con oro."
    narrator "Pero los líderes guerreros chankas rechazan tus sobornos con desprecio."
    
    show uscovilca fierce
    
    uscovilca "¿El cachorro de Viracocha cree que nos comprará con oro?"
    uscovilca "¡Los chankas peleamos por honor, no por metal!"
    
    narrator "Tus emisarios regresan humillados y con las manos vacías."
    narrator "El tiempo perdido en esta estrategia equivocada es crucial."
    
    scene bg cusco_plaza with dissolve
    
    show cusi neutral
    
    cusi "Mi estrategia fue... mal interpretada por los chankas."
    
    show general_loyal
    
    general "Príncipe, las tropas están desmoralizadas."
    general "Creen que tenemos tanto miedo que intentamos comprar la paz."
    
    narrator "CONSECUENCIAS DE LA ESTRATEGIA EQUIVOCADA:"
    narrator "• Pierdes tiempo valioso de preparación"
    narrator "• Tu propia gente pierde respeto hacia ti"
    narrator "• Los chankas se sienten más confiados"
    narrator "• No tienes aliados cuando llega la batalla"
    
    narrator "LECCIÓN HISTÓRICA:"
    narrator "Los chankas eran guerreros orgullosos que vinieron a conquistar."
    narrator "No había negociación posible, solo resistencia heroica."
    narrator "Un líder debe entender la mentalidad de sus enemigos."
    
    narrator "ANÁLISIS DE TU DERROTA:"
    narrator "Tu error principal fue: MALINTERPRETAR LA NATURALEZA DEL CONFLICTO"
    narrator "Los chankas querían gloria militar, no oro."
    narrator "Perdiste tiempo crucial en una estrategia imposible."
    
    scene black with fade
    
    "FINAL: EL ESTRATEGA CONFUNDIDO"
    "Tu intención era inteligente, pero mal dirigida."
    
    jump reiniciar

# ========================================
# ALIANZAS EXITOSAS
# ========================================

label alianzas_exitosas:
    scene bg andean_mountains with fade
    show golden_light with mystical_fade
    
    narrator "Tu llamado resuena a través de todos los ayllus aliados."
    narrator "Los tambores de guerra suenan desde las montañas circundantes."
    
    show general_loyal
    
    apo_mayta "¡Príncipe! ¡Los refuerzos llegan desde todos los suyus!"
    apo_mayta "Los canchis traen 3,000 guerreros experimentados."
    apo_mayta "Los ayarmacas envían 2,000 hombres y provisiones para semanas."
    
    show cusi warrior
    
    cusi "Excelente. Ahora tenemos 13,000 guerreros motivados."
    cusi "Seguimos superados, pero tenemos esperanza real de victoria."
    
    narrator "DECISIÓN HISTÓRICA CORRECTA:"
    narrator "El verdadero Pachacutec pidió ayuda a todas las etnias aliadas."
    narrator "Esta cooperación fue clave para su victoria sobre los chankas."
    narrator "Un líder sabio usa toda la fuerza disponible."
    
    $ apoyo_popular += 2
    $ legitimidad_real += 2
    
    jump tercera_decision

# ========================================
# TERCERA DECISIÓN: RITUALES DE GUERRA
# ========================================

label tercera_decision:
    scene bg coricancha with fade
    show mystical_glow with mystical_fade
    
    narrator "Con las alianzas aseguradas, enfrentas otra decisión crucial."
    narrator "Los sacerdotes insisten en realizar rituales antes de la batalla."
    
    show willaq_umu ceremonial
    
    willaq_umu "Príncipe Cusi, los dioses deben bendecir nuestra causa."
    willaq_umu "Propongo el gran ritual de invocación a los apus de todas las montañas."
    willaq_umu "También consultar a las momias de los Incas ancestrales."
    
    show cusi determined
    
    cusi "Los rituales son sagrados, pero la guerra también requiere preparación física."
    
    menu:
        "¿Cómo manejas los preparativos espirituales?"
        
        "Realizar ceremonias completas según la tradición ancestral":
            $ realizo_rituales_completos = True
            $ poder_ritual += 4
            $ apoyo_popular += 3
            $ puntos_liderazgo += 2
            cusi "Los ancestros y dioses deben estar completamente de nuestro lado."
            cusi "No podemos arriesgar su descontento en momento tan crítico."
            jump rituales_completos
            
        "Hacer ceremonias esenciales pero enfocar tiempo en estrategia":
            $ poder_ritual += 1
            $ error_principal = "rituales_insuficientes"
            cusi "Haremos lo indispensable para no ofender a los dioses."
            jump final_rituales_basicos
            
        "Priorizar preparativos militares sobre ceremonias religiosas":
            $ error_principal = "desprecio_espiritual"
            $ apoyo_popular -= 3
            $ poder_ritual -= 2
            cusi "Los dioses comprenden que actuamos con urgencia práctica."
            jump final_sin_rituales

# ========================================
# RUTA DE DERROTA: RITUALES INSUFICIENTES
# ========================================

label final_rituales_basicos:
    scene bg coricancha with fade
    
    narrator "Realizas solo rituales básicos para ahorrar tiempo."
    narrator "Pero en el mundo andino, lo espiritual y lo militar están unidos."
    
    show willaq_umu ceremonial
    
    willaq_umu "Príncipe, los guerreros esperan la bendición completa de los ancestros."
    
    scene bg yahuar_pampa with dissolve
    
    narrator "En la batalla, tus fuerzas luchan bien pero sin inspiración total."
    narrator "Los rituales incompletos dejan dudas en la mente de los guerreros."
    narrator "La victoria es posible, pero no decisiva."
    
    narrator "CONSECUENCIAS DE RITUALES INSUFICIENTES:"
    narrator "• Los guerreros luchan sin convicción total"
    narrator "• Las etnias aliadas dudan de tu legitimidad espiritual"
    narrator "• La batalla se vuelve más sangrienta de lo necesario"
    narrator "• No inspiras el fervor necesario para una victoria total"
    
    narrator "LECCIÓN HISTÓRICA:"
    narrator "En el mundo andino prehispánico, los rituales eran esenciales para la moral."
    narrator "Los guerreros necesitaban sentir que los dioses estaban de su lado."
    narrator "Pachacutec realizó rituales completos antes de enfrentar a los chankas."
    
    narrator "ANÁLISIS DE TU DERROTA:"
    narrator "Tu error principal fue: SUBESTIMAR LA IMPORTANCIA ESPIRITUAL"
    narrator "El liderazgo inca requería conexión total con lo sagrado."
    narrator "No puedes ser pragmático con las creencias fundamentales de tu pueblo."
    
    scene black with fade
    
    "FINAL: EL LÍDER INCOMPLETO"
    "Tu estrategia militar era correcta, pero te faltó el aspecto espiritual."
    
    jump reiniciar

# ========================================
# RUTA DE DERROTA: DESPRECIO ESPIRITUAL
# ========================================

label final_sin_rituales:
    scene bg war_council with fade
    
    narrator "Decides ignorar completamente los rituales para concentrarte en táctica."
    narrator "Esta decisión horroriza a tus propios seguidores."
    
    show willaq_umu ceremonial
    
    willaq_umu "Príncipe... esto va contra todo lo que representa el Tawantinsuyu."
    willaq_umu "Los guerreros se sentirán abandonados por los dioses."
    
    show cusi neutral
    
    cusi "Los mapas y las estrategias vencen batallas, no las ceremonias."
    
    narrator "CONSECUENCIAS DEL DESPRECIO ESPIRITUAL:"
    narrator "• Los sacerdotes retiran su apoyo totalmente"
    narrator "• Los guerreros se sienten malditos antes de la batalla"
    narrator "• Las etnias aliadas dudan de tu legitimidad como inca"
    narrator "• El pueblo te ve como arrogante y desconectado"
    
    scene bg yahuar_pampa with dissolve
    
    narrator "En la batalla, tus estrategias son brillantes pero..."
    narrator "Los guerreros luchan sin alma, sintiéndose abandonados por los dioses."
    narrator "Las etnias aliadas se retiran durante el combate."
    
    narrator "LECCIÓN HISTÓRICA:"
    narrator "Un inca sin conexión espiritual no es verdaderamente inca."
    narrator "El liderazgo andino requería equilibrio entre lo práctico y lo sagrado."
    narrator "Pachacutec era tanto guerrero como sacerdote."
    
    narrator "ANÁLISIS DE TU DERROTA:"
    narrator "Tu error principal fue: ROMPER CON LA IDENTIDAD CULTURAL INCA"
    narrator "Intentaste ser un líder 'moderno' en una sociedad tradicional."
    narrator "Perdiste el alma de tu propia cultura."
    
    scene black with fade
    
    "FINAL: EL ESTRATEGA SIN ALMA"
    "Tu intelecto era brillante, pero perdiste el corazón de tu pueblo."
    
    jump reiniciar

# ========================================
# RITUALES COMPLETOS
# ========================================

label rituales_completos:
    scene bg ritual_site with fade
    show mystical_glow with mystical_fade
    
    narrator "Decides realizar los rituales ancestrales completos."
    narrator "Durante tres días sagrados, Cusco se transforma en centro ceremonial."
    
    show willaq_umu ceremonial
    
    willaq_umu "Invocamos a Inti, el Sol, padre de todos los incas."
    willaq_umu "Llamamos a los apus de las montañas sagradas circundantes."
    willaq_umu "Consultamos a las momias de los ancestros reales."
    
    narrator "RITUAL DEL PRIMER DÍA: INVOCACIÓN SOLAR"
    narrator "Al amanecer, realizas ofrendas de oro, coca y mullu al Sol."
    narrator "Pides que Inti ilumine el camino hacia la victoria de su pueblo."
    
    narrator "RITUAL DEL SEGUNDO DÍA: COMUNICACIÓN CON APUS"
    narrator "En las montañas alrededor de Cusco, colocas ofrendas sagradas."
    narrator "Los espíritus de montaña responden con vientos favorables y señales."
    
    narrator "RITUAL DEL TERCER DÍA: CONSULTA A ANCESTROS"
    narrator "Las momias de Incas pasados son traídas al Coricancha."
    narrator "Sus 'consejos' espirituales fortalecen tu legitimidad como líder."
    
    show cusi warrior
    
    cusi "Siento la fuerza de todos mis ancestros corriendo por mis venas."
    cusi "Los dioses han hablado: ¡Cusco no caerá mientras yo viva!"
    
    narrator "Los guerreros ven las señales divinas y su valor se multiplica."
    narrator "Incluso las etnias aliadas se sienten inspiradas por tu conexión espiritual."
    
    $ apoyo_popular += 2
    
    jump cuarta_decision

# ========================================
# CUARTA DECISIÓN: ESTRATEGIA MILITAR
# ========================================

label cuarta_decision:
    scene bg war_council with fade
    
    narrator "Con alianzas sólidas y rituales completados, llega la decisión militar crucial."
    narrator "¿Cómo enfrentarás a los 40,000 guerreros chankas?"
    
    show apo_mayta_loyal
    
    apo_mayta "Príncipe, nuestros exploradores reportan la posición enemiga."
    apo_mayta "Los chankas avanzan por la llanura de Yahuar Pampa."
    apo_mayta "Podemos elegir dónde y cómo enfrentarlos."
    
    show cusi warrior
    
    cusi "Esta decisión determinará si el Tawantinsuyu sobrevive o perece."
    
    menu:
        "¿Cuál será tu estrategia militar?"
        
        "Usar las ventajas del terreno montañoso para emboscadas":
            $ uso_estrategia_correcta = True
            $ estrategia_militar += 4
            $ puntos_liderazgo += 3
            cusi "Aprovechemos lo que conocemos mejor: nuestras montañas sagradas."
            cusi "El terreno puede compensar su ventaja en números."
            jump estrategia_emboscada
            
        "Enfrentar directamente su fuerza con nuestro valor demostrado":
            $ error_principal = "estrategia_valiente_pero_ingenua"
            $ estrategia_militar += 1
            cusi "Demostraremos que el valor inca supera cualquier número."
            jump final_batalla_frontal
            
        "Fortificar posiciones defensivas y resistir el asedio":
            $ error_principal = "estrategia_pasiva"
            $ estrategia_militar -= 2
            cusi "Haremos de Cusco una fortaleza inexpugnable."
            jump final_defensa_pasiva

# ========================================
# RUTA DE DERROTA: BATALLA FRONTAL
# ========================================

label final_batalla_frontal:
    scene bg yahuar_pampa with fade
    show war_red with war_flash
    
    narrator "Decides enfrentar a los chankas en batalla frontal."
    narrator "Es valiente, pero estratégicamente ingenuo."
    
    show cusi warrior
    
    cusi "¡Guerreros! ¡Hoy demostraremos que el valor inca es superior!"
    
    scene bg yahuar_pampa with dissolve
    
    narrator "13,000 incas y aliados contra 40,000 chankas en campo abierto."
    narrator "A pesar del valor sobrehumano, los números son abrumadores."
    narrator "La batalla se convierte en una carnicería heroica pero inútil."
    
    narrator "CONSECUENCIAS DE LA BATALLA FRONTAL:"
    narrator "• Tus fuerzas son gradualmente abrumadas por la superioridad numérica"
    narrator "• Miles de guerreros leales mueren innecesariamente"
    narrator "• No aprovechaste las ventajas tácticas disponibles"
    narrator "• Los chankas sufren bajas pero mantienen la ventaja"
    
    narrator "LECCIÓN HISTÓRICA:"
    narrator "Pachacutec histórico evitó la batalla frontal directa."
    narrator "Usó el terreno montañoso para neutralizar la ventaja numérica chanka."
    narrator "El valor sin estrategia es valentía desperdiciada."
    
    narrator "ANÁLISIS DE TU DERROTA:"
    narrator "Tu error principal fue: VALOR SIN ESTRATEGIA INTELIGENTE"
    narrator "Un gran líder combina coraje con inteligencia táctica."
    narrator "La batalla frontal favorecía obviamente al ejército más numeroso."
    
    scene black with fade
    
    "FINAL: EL HÉROE VALIENTE PERO INGENUO"
    "Tu coraje era admirable, pero te faltó astucia militar."
    
    jump reiniciar

# ========================================
# RUTA DE DERROTA: DEFENSA PASIVA
# ========================================

label final_defensa_pasiva:
    scene bg cusco_plaza with fade
    show war_red with fade
    
    narrator "Decides fortificar Cusco y esperar un asedio prolongado."
    narrator "Es una estrategia aparentemente defensiva pero con fallas críticas."
    
    show general_loyal
    
    general "Las defensas están listas, príncipe."
    general "Pero un asedio largo favorece a quien controla los suministros externos."
    
    narrator "PROBLEMAS DE LA DEFENSA PASIVA:"
    narrator "• Los chankas cortan todas las rutas de suministro"
    narrator "• Un asedio prolongado desmoraliza a la población civil"
    narrator "• Las etnias aliadas deben regresar a defender sus propios territorios"
    narrator "• Cusco sufre hambre y enfermedades"
    
    scene bg cusco_plaza with dissolve
    show war_red with war_flash
    
    narrator "Después de cuatro meses de asedio brutal..."
    narrator "Los suministros se agotan, las enfermedades se extienden."
    narrator "Las etnias aliadas se han retirado a sus territorios."
    narrator "Cusco cae por hambre y pestilencia, no por falta de valor."
    
    narrator "LECCIÓN HISTÓRICA:"
    narrator "Los asedios favorecen al atacante que controla el campo abierto."
    narrator "Pachacutec buscó una batalla decisiva rápida, no una guerra de desgaste."
    narrator "Defender una ciudad no es lo mismo que defender un imperio."
    
    narrator "ANÁLISIS DE TU DERROTA:"
    narrator "Tu error principal fue: ESTRATEGIA DEFENSIVA PASIVA"
    narrator "Permitiste que el enemigo dictara los términos del conflicto."
    narrator "Un líder debe buscar la iniciativa, no solo reaccionar."
    
    scene black with fade
    
    "FINAL: EL DEFENSOR PASIVO"
    "Tu cautela se convirtió en el camino hacia la derrota."
    
    jump reiniciar

# ========================================
# ESTRATEGIA DE EMBOSCADA (CAMINO CORRECTO)
# ========================================

label estrategia_emboscada:
    scene bg andean_mountains with fade
    show mystical_glow with mystical_fade
    
    narrator "Eliges la estrategia más inteligente: usar el terreno montañoso."
    narrator "Esta decisión neutralizará la ventaja numérica chanka."
    
    show cusi warrior
    
    cusi "General, posicionaremos nuestras fuerzas en los pasos de montaña."
    cusi "Cuando los chankas entren en los valles, los atacaremos desde arriba."
    
    show apo_mayta_loyal
    
    apo_mayta "Estrategia brillante, príncipe. El terreno trabajará para nosotros."
    
    narrator "VENTAJAS DE LA EMBOSCADA MONTAÑOSA:"
    narrator "• Los chankas no pueden usar toda su fuerza simultáneamente"
    narrator "• Las piedras lanzadas desde arriba causan pánico y confusión"
    narrator "• Los caminos estrechos impiden las maniobras enemigas"
    narrator "• Tus fuerzas tienen posiciones defensivas superiores"
    
    narrator "PREPARATIVOS ESTRATÉGICOS:"
    narrator "• Colocas guerreros en las cumbres circundantes"
    narrator "• Preparas avalanchas de piedras en puntos clave"
    narrator "• Estableces rutas de escape y reagrupamiento"
    narrator "• Coordinas señales de humo entre las posiciones"
    
    $ estrategia_militar += 2
    
    jump quinta_decision

# ========================================
# QUINTA DECISIÓN: LIDERAZGO PERSONAL
# ========================================

label quinta_decision:
    scene bg battlefield_dawn with fade
    show golden_light with mystical_fade
    
    narrator "El amanecer de la batalla decisiva ha llegado."
    narrator "Todas tus decisiones previas te han llevado a este momento crucial."
    narrator "Ahora debes decidir cómo liderar personalmente en el combate."
    
    show cusi warrior
    
    cusi "Este es el momento que definirá mi destino para siempre."
    cusi "¿Seré recordado como Cusi Yupanqui... o como Pachacutec?"
    
    menu:
        "¿Cómo lideras en el momento decisivo de la batalla?"
        
        "Inspirar personalmente liderando desde la primera línea":
            $ lidero_personalmente = True
            $ puntos_liderazgo += 4
            $ apoyo_popular += 3
            cusi "¡Guerreros! ¡Hoy escribiremos leyendas o moriremos con honor!"
            jump liderazgo_heroico
            
        "Dirigir estratégicamente desde posición de comando óptima":
            $ error_principal = "liderazgo_distante"
            $ estrategia_militar += 1
            $ puntos_liderazgo -= 2
            cusi "Coordinaré desde donde pueda visualizar mejor todo el campo."
            jump final_liderazgo_distante
            
        "Proponer duelo de honor con Uscovilca para evitar masacre":
            $ error_principal = "apuesta_desesperada"
            cusi "¡Uscovilca! ¡Resolvamos esto entre líderes!"
            jump final_duelo_uscovilca

# ========================================
# RUTA DE DERROTA: LIDERAZGO DISTANTE
# ========================================

label final_liderazgo_distante:
    scene bg war_council with fade
    
    narrator "Decides dirigir desde una posición estratégica alejada."
    narrator "Es tácticamente inteligente pero emocionalmente equivocado."
    
    show apo_mayta_loyal
    
    apo_mayta "Príncipe, las tropas necesitan ver su valor personal."
    apo_mayta "En el mundo andino, un líder debe inspirar con ejemplo."
    
    scene bg yahuar_pampa with dissolve
    
    narrator "Tus órdenes son precisas y tus estrategias son correctas."
    narrator "Pero los guerreros luchan sin la inspiración de verte arriesgar tu vida."
    narrator "La batalla es competente pero no heroica."
    
    narrator "CONSECUENCIAS DEL LIDERAZGO DISTANTE:"
    narrator "• Los guerreros luchan competentemente pero sin pasión extrema"
    narrator "• Te falta el elemento mítico que inspira leyendas"
    narrator "• Los chankas no sienten el terror de enfrentar un líder sobrehumano"
    narrator "• La victoria es posible pero no decisiva"
    
    narrator "LECCIÓN HISTÓRICA:"
    narrator "Pachacutec lideró desde el frente de la batalla."
    narrator "Su valor personal inspiró a sus guerreros a logros sobrehumanos."
    narrator "En el mundo andino, el liderazgo requería ejemplo físico directo."
    
    narrator "ANÁLISIS DE TU DERROTA:"
    narrator "Tu error principal fue: LIDERAZGO SIN INSPIRACIÓN PERSONAL"
    narrator "Un comandante competente no es lo mismo que un líder legendario."
    narrator "Te faltó el elemento carismático que transforma soldados en héroes."
    
    scene black with fade
    
    "FINAL: EL COMANDANTE COMPETENTE"
    "Tu estrategia era correcta, pero te faltó inspirar con ejemplo personal."
    
    jump reiniciar

# ========================================
# RUTA DE DERROTA: DUELO CON USCOVILCA
# ========================================

label final_duelo_uscovilca:
    scene bg yahuar_pampa with fade
    show war_red with war_flash
    
    narrator "Desafías a Uscovilca a un duelo personal para decidir la guerra."
    narrator "Es dramático pero estratégicamente arriesgado."
    
    show uscovilca fierce
    
    uscovilca "¿El cachorro de Viracocha quiere medirse conmigo?"
    uscovilca "¡Acepto! Cuando mueras, tus guerreros se rendirán."
    
    narrator "El duelo es épico y sangriento."
    narrator "Ambos líderes son guerreros excepcionales."
    narrator "Pero apostar todo en un solo combate es demasiado arriesgado."
    
    menu duelo_resultado:
        "El resultado del duelo:"
        
        "Logras vencer a Uscovilca heroicamente":
            narrator "Vences a Uscovilca en combate épico."
            narrator "Pero estás gravemente herido y no puedes liderar el resto de la batalla."
            narrator "Sin tu liderazgo directo, la victoria se vuelve incierta."
            
        "El duelo termina con ambos líderes heridos":
            narrator "Tanto tú como Uscovilca quedan gravemente heridos."
            narrator "La batalla principal continúa sin liderazgo claro en ningún bando."
            narrator "El resultado se vuelve caótico e impredecible."
    
    narrator "CONSECUENCIAS DEL DUELO:"
    narrator "• Arriesgaste todo el liderazgo en un solo combate"
    narrator "• Aunque seas un gran guerrero, podrías haber perdido"
    narrator "• Incluso ganando, quedas incapacitado para liderar el resto"
    narrator "• Es más dramático que efectivo estratégicamente"
    
    narrator "LECCIÓN HISTÓRICA:"
    narrator "Pachacutec lideró toda la batalla, no arriesgó todo en un duelo."
    narrator "Un líder sabio no apuesta el destino de su pueblo en su habilidad personal."
    narrator "El liderazgo estratégico es más valioso que el heroísmo individual."
    
    narrator "ANÁLISIS DE TU DERROTA:"
    narrator "Tu error principal fue: APUESTA DESESPERADA EN LUGAR DE LIDERAZGO SÓLIDO"
    narrator "Confundiste drama personal con estrategia efectiva."
    narrator "Un líder debe pensar en su pueblo, no solo en su gloria personal."
    
    scene black with fade
    
    "FINAL: EL DUELISTA DRAMÁTICO"
    "Tu valor individual era impresionante, pero te faltó visión estratégica."
    
    jump reiniciar

# ========================================
# LIDERAZGO HEROICO (CAMINO CORRECTO)
# ========================================

label liderazgo_heroico:
    scene bg yahuar_pampa with fade
    show war_red with war_flash
    
    narrator "Decides liderar desde el frente, arriesgando tu vida por tu pueblo."
    narrator "Esta decisión te convierte en leyenda viviente ante tus guerreros."
    
    show cusi inca
    
    cusi "¡Por Inti! ¡Por Cusco! ¡Por el Tawantinsuyu que construiremos!"
    
    narrator "Cargas al frente de tus 13,000 guerreros."
    narrator "Tu valor personal electriza a todas las tropas aliadas."
    narrator "Incluso los chankas dudan al ver tu determinación sobrehumana."
    
    narrator "EFECTOS DEL LIDERAZGO HEROICO:"
    narrator "• La moral de tus tropas se dispara al máximo"
    narrator "• Los guerreros aliados luchan como nunca antes"
    narrator "• Los chankas comienzan a retroceder psicológicamente"
    narrator "• Te conviertes en símbolo viviente de resistencia"
    
    jump momento_legendario

# ========================================
# MOMENTO LEGENDARIO: LAS PIEDRAS VIVIENTES
# ========================================

label momento_legendario:
    scene bg yahuar_pampa with fade
    show mystical_glow with mystical_fade
    
    narrator "En el momento más intenso de la batalla, sucede algo extraordinario..."
    narrator "Las crónicas registran un evento que cambió el curso de la historia."
    
    show cusi inca
    
    cusi "¡Hermanos de piedra! ¡Apus sagrados! ¡Ayudadme en esta hora suprema!"
    
    narrator "Según las crónicas históricas, las piedras del campo se alzaron para ayudar."
    narrator "Los historiadores modernos interpretan esto como:"
    narrator "• Refuerzos inesperados llegando al momento crucial"
    narrator "• Deslaves causados por los rituales realizados en las montañas"
    narrator "• El efecto psicológico del liderazgo inspirador magnificado"
    narrator "• La transformación del mito en realidad a través de la fe"
    
    show uscovilca commanding
    
    uscovilca "¡Las mismas montañas luchan contra nosotros!"
    uscovilca "¡Este Cusi Yupanqui tiene el favor de dioses terribles!"
    
    narrator "El pánico se extiende entre las filas chankas como fuego en paja seca."
    narrator "Tu liderazgo inspirador se ha convertido en ventaja psicológica decisiva."
    narrator "Los 40,000 chankas comienzan a retroceder ante 13,000 incas inspirados."
    
    jump verificacion_victoria

# ========================================
# VERIFICACIÓN FINAL PARA VICTORIA
# ========================================

label verificacion_victoria:
    scene bg yahuar_pampa with fade
    
    narrator "VERIFICACIÓN DE DECISIONES CRÍTICAS:"
    
    # Aquí verificamos si el jugador tomó TODAS las decisiones correctas
    if defendio_cusco and pidio_ayuda_aliados and realizo_rituales_completos and uso_estrategia_correcta and lidero_personalmente:
        jump victoria_total_pachacutec
    else:
        # Si falta alguna decisión crítica, explicamos qué faltó
        jump explicar_fallas

# ========================================
# EXPLICACIÓN DE FALLAS (PARA FINALES EDUCATIVOS)
# ========================================

label explicar_fallas:
    scene bg yahuar_pampa with fade
    
    narrator "Has tomado varias decisiones correctas, pero no todas las necesarias."
    narrator "Para convertirte en Pachacutec, necesitabas perfección en TODOS los aspectos."
    
    narrator "DECISIONES CORRECTAS QUE TOMASTE:"
    
    if defendio_cusco:
        narrator "✓ Te quedaste a defender Cusco (CORRECTO)"
    else:
        narrator "✗ No defendiste Cusco cuando era necesario"
    
    if pidio_ayuda_aliados:
        narrator "✓ Pediste ayuda a las etnias aliadas (CORRECTO)"
    else:
        narrator "✗ No conseguiste las alianzas necesarias"
    
    if realizo_rituales_completos:
        narrator "✓ Realizaste todos los rituales ancestrales (CORRECTO)"
    else:
        narrator "✗ No completaste los rituales espirituales necesarios"
    
    if uso_estrategia_correcta:
        narrator "✓ Usaste estrategia de emboscada montañosa (CORRECTO)"
    else:
        narrator "✗ No elegiste la estrategia militar óptima"
    
    if lidero_personalmente:
        narrator "✓ Lideraste personalmente desde el frente (CORRECTO)"
    else:
        narrator "✗ No inspiraste con liderazgo personal heroico"
    
    narrator "LECCIÓN FINAL:"
    narrator "Convertirse en Pachacutec requería excelencia en TODAS las áreas:"
    narrator "• Valor personal para quedarse cuando otros huyen"
    narrator "• Humildad estratégica para pedir ayuda necesaria"
    narrator "• Respeto espiritual por las tradiciones ancestrales"
    narrator "• Inteligencia militar para usar ventajas tácticas"
    narrator "• Liderazgo inspirador que transforma soldados en héroes"
    
    scene black with fade
    
    "FINAL: LÍDER COMPETENTE PERO NO LEGENDARIO"
    "Fuiste un buen líder, pero Pachacutec era excepcional en todo."
    
    jump reiniciar

# ========================================
# VICTORIA TOTAL: NACIMIENTO DE PACHACUTEC
# ========================================

label victoria_total_pachacutec:
    scene bg victory_plaza with fade
    show golden_light with golden_flash
    
    narrator "¡VICTORIA TOTAL Y ABSOLUTA!"
    narrator "Tu liderazgo excepcional ha logrado lo imposible."
    
    show cusi inca
    
    cusi "¡La victoria es nuestra! ¡Cusco está a salvo para siempre!"
    
    narrator "RESULTADOS DE LA BATALLA LEGENDARIA:"
    narrator "• Los 40,000 chankas son completamente derrotados"
    narrator "• Uscovilca muere en el campo de batalla"
    narrator "• Todas las etnias aliadas te reconocen como verdadero líder"
    narrator "• El pueblo de Cusco te aclama como salvador del mundo"
    
    scene bg cusco_plaza with dissolve
    show golden_light with mystical_fade
    
    narrator "Días después, en la plaza sagrada de Cusco..."
    
    show willaq_umu ceremonial
    
    willaq_umu "Cusi Yupanqui, por tu valor y sabiduría excepcionales..."
    willaq_umu "Por haber salvado el Tawantinsuyu de la destrucción total..."
    willaq_umu "El pueblo, los nobles y los dioses te proclamamos nuevo Inca."
    willaq_umu "Desde hoy serás conocido como PACHACUTEC - 'El que transforma el mundo'."
    
    show cusi inca
    
    cusi "Acepto este honor sagrado, no para mi gloria personal, sino para el Tawantinsuyu."
    cusi "Construiremos un imperio que perdure mil años y alcance los cuatro confines del mundo."
    
    narrator "ANÁLISIS DE TU VICTORIA PERFECTA:"
    narrator "✓ Mostraste valor supremo al quedarte en Cusco"
    narrator "✓ Fuiste inteligente al conseguir todas las alianzas posibles"
    narrator "✓ Respetaste completamente las tradiciones rituales ancestrales"
    narrator "✓ Usaste la estrategia militar más efectiva disponible"
    narrator "✓ Inspiraste con liderazgo personal heroico y legendario"
    
    narrator "TODAS LAS DECISIONES CRÍTICAS EXITOSAS:"
    narrator "• Defendiste Cusco cuando tu familia huyó"
    narrator "• Pediste ayuda a canchis, ayarmacas y otros aliados"
    narrator "• Realizaste todos los rituales tradicionales de guerra"
    narrator "• Usaste emboscada montañosa para neutralizar ventaja numérica"
    narrator "• Lideraste desde el frente inspirando a tus guerreros"
    
    narrator ""
    narrator "{color=#FFD700}{b}LEGADO HISTÓRICO REAL{/b}{/color}"
    narrator "El Pachacutec histórico siguió exactamente este patrón de decisiones. Su victoria sobre los chankas fundó el verdadero Imperio Inca. Construyó Machu Picchu, reorganizó el estado, expandió el territorio, creó el sistema de mitmas, estableció el quechua como lengua oficial. Es considerado el verdadero fundador del Imperio del Tawantinsuyu."
    
    narrator ""
    narrator "{color=#FFD700}{b}TUS LOGROS COMO PACHACUTEC{/b}{/color}"
    narrator "• Fundaste el Imperio Inca que duró hasta la llegada española • Expandiste el territorio desde Ecuador hasta Chile • Construiste Machu Picchu como refugio real sagrado • Reorganizaste completamente la administración del estado • Estableciste el sistema de ayllus y la reciprocidad andina • Creaste la red de caminos que conectó todo el imperio"
    
    scene black with fade
    show golden_light with golden_flash
    
    narrator ""
    narrator "{color=#FFD700}{b}¡FELICIDADES!{/b}{/color}"
    narrator "{color=#FFD700}HAS LOGRADO CONVERTIRTE EN PACHACUTEC{/color}"
    narrator "{color=#FFD700}EL TRANSFORMADOR DEL MUNDO ANDINO{/color}"
    narrator "{color=#FFD700}EL MÁS GRANDE DE TODOS LOS INCAS{/color}"
    
    narrator ""
    narrator "Has completado exitosamente 'EL ASCENSO DE PACHACUTEC'. Aprendiste que el liderazgo legendario requiere: Valor, Sabiduría, Espiritualidad, Estrategia e Inspiración."
    narrator ""
    narrator "La historia de Pachacutec nos recuerda que una persona con las decisiones correctas puede cambiar el curso de la historia."
    narrator ""
    narrator "{color=#FFD700}¡Gracias por revivir esta leyenda andina!{/color}"
    
    return

# ========================================
# FUNCIÓN DE REINICIO
# ========================================

label reiniciar:
    scene black with fade
    
    narrator "¿Has aprendido las lecciones de la historia?"
    narrator "El camino hacia convertirse en Pachacutec requiere perfección en todas las decisiones."
    narrator ""
    narrator "Cada elección que hiciste tenía consecuencias históricas reales."
    narrator "El verdadero Cusi Yupanqui tuvo que tomar TODAS las decisiones correctas."
    narrator ""
    narrator "¿Quieres intentar nuevamente el camino hacia la grandeza?"
    
    menu final_menu:
        "¿Qué deseas hacer?"
        
        "Intentar nuevamente con el conocimiento aprendido":
            # Reset completo de todas las variables
            $ puntos_liderazgo = 0
            $ apoyo_popular = 0
            $ alianzas_etnias = 0
            $ poder_ritual = 0
            $ estrategia_militar = 0
            $ legitimidad_real = 0
            $ defendio_cusco = False
            $ pidio_ayuda_aliados = False
            $ realizo_rituales_completos = False
            $ uso_estrategia_correcta = False
            $ lidero_personalmente = False
            $ error_principal = ""
            $ leccion_aprendida = ""
            jump start
            
        "Finalizar la experiencia histórica":
            narrator "Gracias por aprender sobre la historia real de Pachacutec."
            narrator "Su legado transformó el mundo andino para siempre."
            narrator "La historia nos enseña que el liderazgo excepcional es posible."
            return

# ========================================
# FIN DEL JUEGO
# ========================================