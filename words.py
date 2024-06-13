level_words: list[list[dict[str, str]]] = [
    [
        {"word": "montana", "hint": "Gran elevacion natural del terreno"},
        {"word": "oceano", "hint": "Gran extension de agua salada"},
        {"word": "piano", "hint": "Instrumento musical con teclas"},
        {"word": "tortuga", "hint": "Reptil con caparazon"},
        {"word": "guitarra", "hint": "Instrumento musical de cuerdas"},
        {"word": "planeta", "hint": "Cuerpo celeste que gira alrededor de una estrella"},
        {"word": "chocolate", "hint": "Dulce hecho de cacao"},
        {"word": "futbol", "hint": "Deporte jugado con una pelota y dos equipos"},
        {"word": "murcielago", "hint": "Unico mamifero que puede volar"},
        {"word": "martillo", "hint": "Herramienta usada para clavar"}
    ],
    [
        {"word": "tren", "hint": "Medio de transporte sobre rieles"},
        {"word": "montana rusa", "hint": "Atraccion de parque con muchas curvas y caidas"},
        {"word": "termometro", "hint": "Instrumento para medir la temperatura"},
        {"word": "escalera", "hint": "Objeto para subir o bajar niveles"},
        {"word": "pintura", "hint": "Arte de aplicar pigmentos en una superficie"},
        {"word": "leon", "hint": "Rey de la selva"},
        {"word": "estrella", "hint": "Cuerpo celeste que brilla en el cielo"},
        {"word": "cometa", "hint": "Objeto celeste que orbita alrededor del sol"},
        {"word": "flor", "hint": "Parte de la planta que produce semillas"},
        {"word": "astronauta", "hint": "Persona que viaja al espacio"}
    ],
    [
        {"word": "cocodrilo", "hint": "Reptil grande con mandibulas fuertes"},
        {"word": "tornado", "hint": "Fenomeno meteorologico con fuertes vientos giratorios"},
        {"word": "cangrejo", "hint": "Animal marino con caparazon duro y pinzas"},
        {"word": "astronomia", "hint": "Ciencia que estudia los astros"},
        {"word": "diamante", "hint": "Piedra preciosa muy dura"},
        {"word": "bumeran", "hint": "Objeto que regresa al lanzador"},
        {"word": "telescopio", "hint": "Instrumento para observar objetos lejanos"},
        {"word": "esqueleto", "hint": "Conjunto de huesos de un cuerpo"},
        {"word": "helice", "hint": "Parte giratoria de un avion o barco"},
        {"word": "frigorifico", "hint": "Electrodomestico para conservar alimentos frios"}
    ],
    [
        {"word": "psicologia", "hint": "Ciencia que estudia la mente y el comportamiento"},
        {"word": "matematicas", "hint": "Ciencia de los numeros y las formas"},
        {"word": "holograma", "hint": "Imagen tridimensional creada con laser"},
        {"word": "transistor", "hint": "Componente electronico para amplificar o conmutar senales"},
        {"word": "microondas", "hint": "Electrodomestico para calentar alimentos rapidamente"},
        {"word": "satelite", "hint": "Objeto que orbita alrededor de un planeta"},
        {"word": "electron", "hint": "Particula subatomica con carga negativa"},
        {"word": "radiactividad", "hint": "Emision de particulas por descomposicion nuclear"},
        {"word": "algoritmo", "hint": "Conjunto de instrucciones para resolver un problema"},
        {"word": "centrifuga", "hint": "Maquina que separa sustancias de diferente densidad"}
    ],
    [
        {"word": "filantropia", "hint": "Accion de ayudar a los demas sin esperar nada a cambio"},
        {"word": "optica", "hint": "Rama de la fisica que estudia la luz"},
        {"word": "paleontologia", "hint": "Ciencia que estudia los fosiles"},
        {"word": "morfologia", "hint": "Estudio de la forma y estructura de los organismos"},
        {"word": "navegacion", "hint": "Accion de dirigir una nave o vehiculo"},
        {"word": "biodegradable", "hint": "Que puede ser descompuesto por organismos vivos"},
        {"word": "astronomia", "hint": "Ciencia que estudia los cuerpos celestes"},
        {"word": "energia", "hint": "Capacidad de realizar trabajo"},
        {"word": "reciclaje", "hint": "Proceso de convertir residuos en nuevos productos"},
        {"word": "biomecanica", "hint": "Estudio de las estructuras biologicas desde la mecanica"}
    ],
    [
        {"word": "conductividad", "hint": "Propiedad de algunos materiales de conducir electricidad"},
        {"word": "termodinamica", "hint": "Rama de la fisica que estudia el calor y la energia"},
        {"word": "antropologia", "hint": "Ciencia que estudia al ser humano en su aspecto biologico y cultural"},
        {"word": "cosmologia", "hint": "Estudio del origen y evolucion del universo"},
        {"word": "geofisica", "hint": "Ciencia que estudia la Tierra a traves de metodos fisicos"},
        {"word": "microbiologia", "hint": "Estudio de los microorganismos"},
        {"word": "neurociencia", "hint": "Estudio del sistema nervioso"},
        {"word": "paleontologia", "hint": "Ciencia que estudia los fosiles"},
        {"word": "fisica cuantica", "hint": "Rama de la fisica que estudia los fenomenos a escala subatomica"},
        {"word": "genetica", "hint": "Ciencia que estudia la herencia y la variacion de los seres vivos"}
    ],
    [
        {"word": "hipotermia", "hint": "Condicion medica por una baja extrema de temperatura corporal"},
        {"word": "electromagnetismo", "hint": "Rama de la fisica que estudia los fenomenos electricos y magneticos"},
        {"word": "cristalografia", "hint": "Ciencia que estudia la estructura y propiedades de los cristales"},
        {"word": "bioluminiscencia", "hint": "Emision de luz por parte de organismos vivos"},
        {"word": "transubstanciacion", "hint": "Doctrina religiosa sobre el cuerpo y la sangre de Cristo"},
        {"word": "neurotransmisor", "hint": "Sustancia quimica que transmite senales entre neuronas"},
        {"word": "nanotecnologia", "hint": "Ciencia y tecnologia que manipula la materia a escala nanometrica"},
        {"word": "anticonstitucional", "hint": "Algo que va en contra de la constitucion"},
        {"word": "esternocleidomastoideo", "hint": "Musculo del cuello"},
        {"word": "fenomenologia", "hint": "Estudio de las estructuras desde una perspectiva en primera persona"}
    ],
    [
        {"word": "inmunodeficiencia", "hint": "Estado en el que el sistema inmunitario no funciona correctamente"},
        {"word": "heterocromia", "hint": "Condicion de tener ojos de diferentes colores"},
        {"word": "electroencefalograma", "hint": "Prueba medica para registrar la actividad electrica del cerebro"},
        {"word": "otorrinolaringologia", "hint": "Especialidad que trata enfermedades en oidos, nariz y garganta"},
        {"word": "cardiovascular", "hint": "Relativo al corazon y los vasos sanguineos"},
        {"word": "paralelepipedo", "hint": "Figura geometrica de seis caras rectangulares"},
        {"word": "desoxirribonucleico", "hint": "Compuesto quimico que contiene la informacion genetica"},
        {"word": "magnetohidrodinamica", "hint": "Estudio de la dinamica de fluidos conductores en campos magneticos"},
        {"word": "hipertrigliceridemia", "hint": "Niveles elevados de trigliceridos en la sangre"},
        {"word": "antropocentrismo", "hint": "Doctrina que coloca al ser humano en el centro del universo"}
    ],
    [
        {"word": "espectrofotometria", "hint": "Tecnica para medir la cantidad de luz que una sustancia absorbe"},
        {"word": "neuropsicologia", "hint": "Ciencia que estudia las relaciones entre el cerebro y la conducta"},
        {"word": "biocompatibilidad", "hint": "Capacidad de un material para integrarse con tejidos biologicos"},
        {"word": "electroquimica", "hint": "Rama de la quimica que involucra el movimiento de electrones"},
        {"word": "cicloalifatico", "hint": "Compuesto organico con una estructura de anillo no aromatico"},
        {"word": "termorregulacion", "hint": "Capacidad de un organismo para mantener su temperatura corporal"},
        {"word": "fotovoltaico", "hint": "Relativo a la conversion de luz en electricidad"},
        {"word": "supercalifragilisticoespialidoso", "hint": "Palabra inventada para describir algo extraordinario"},
        {"word": "caracteristicamente", "hint": "De manera que muestra una caracteristica particular"},
        {"word": "desoxigenacion", "hint": "Proceso de eliminar oxigeno de un compuesto"}
    ],
    [
        {"word": "desoxirribonucleotido", "hint": "Unidad basica del ADN compuesta por una base"},
        {"word": "hipertermia", "hint": "Elevacion peligrosa de la temperatura corporal"},
        {"word": "cristaloluminiscencia", "hint": "Emision de luz por parte de ciertos cristales"},
        {"word": "microspectrofotometria", "hint": "Tecnica que combina la microscopia y la espectrofotometria"},
        {"word": "heteropolimero", "hint": "Polimero compuesto de diferentes tipos de monomeros"},
        {"word": "bioelectromagnetismo", "hint": "Estudio de los fenomenos electromagneticos en organismos vivos"},
        {"word": "radioinmunoensayo", "hint": "Tecnica para medir sustancias en el cuerpo usando radioisotopos"},
        {"word": "fotosensibilizacion", "hint": "Aumento de la sensibilidad a la luz"},
        {"word": "fotobiomodulacion", "hint": "Uso de la luz para modificar procesos biologicos"},
        {"word": "antropomorfizacion", "hint": "Atribuir caracteristicas humanas a animales o cosas inanimadas"}
    ]
]
