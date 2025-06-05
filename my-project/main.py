from manim import *

class Intro(Scene):
    def construct(self):
        self.play(Write(Text("1. Introducción")))
        self.wait(1)
        texto = MarkupText("""
        Este análisis se enfoca en el contenido lírico de los álbumes de Mac Miller.
        A través de técnicas de minería de texto, se busca explorar los temas y emociones
        predominantes en sus letras, resaltando diferencias entre distintas etapas creativas.
        """)
        texto.scale(0.5).next_to(Text("1. Introducción"), DOWN)
        self.play(FadeIn(texto))
        self.wait(3)

class CasoDeEstudio(Scene):
    def construct(self):
        self.play(Write(Text("2. Caso de estudio")))
        self.wait(1)
        texto = MarkupText("""
        Se examinan tres álbumes: 'Swimming', 'Circles' y 'The Divine Feminine'.
        El objetivo es comparar sus letras para encontrar patrones de cambio
        en el lenguaje, el tono emocional y la estructura lírica.
        """)
        texto.scale(0.5).next_to(Text("2. Caso de estudio"), DOWN)
        self.play(FadeIn(texto))
        self.wait(3)

class ImportarTexto(Scene):
    def construct(self):
        self.play(Write(Text("3. Importar texto")))
        self.wait(1)
        codigo = Code(
            code="""
library(readr)
library(dplyr)
raw_lyrics <- read_csv('lyrics.csv')
""",
            language="r",
            background="window",
            font="Monospace",
            tab_width=4
        )
        self.play(FadeIn(codigo.scale(0.5)))
        self.wait(3)

class Tokenizacion(Scene):
    def construct(self):
        self.play(Write(Text("4. Tokenización")))
        self.wait(1)
        codigo = Code(
            code="""
library(tidytext)
lyrics_tokens <- raw_lyrics %>%
  unnest_tokens(word, lyrics)
""",
            language="r",
            background="window",
            font="Monospace",
            tab_width=4
        )
        self.play(FadeIn(codigo.scale(0.5)))
        self.wait(3)

class NormalizacionTexto(Scene):
    def construct(self):
        self.play(Write(Text("5. Normalización del texto")))
        self.wait(1)
        texto = MarkupText("""
        Después de tokenizar, se eliminan signos de puntuación, números y caracteres especiales.
        También se convierten todas las palabras a minúsculas para asegurar consistencia.
        """)
        texto.scale(0.5).next_to(Text("5. Normalización del texto"), DOWN)
        self.play(FadeIn(texto))
        self.wait(3)

class TokensMasFrecuentes(Scene):
    def construct(self):
        texto = MarkupText("""
        Se contabilizaron las palabras más frecuentes en las letras de cada álbum,
        excluyendo palabras vacías. Esto permite observar qué términos tienen mayor
        peso lírico en el conjunto.
        """).scale(0.5).to_edge(UP)
        self.play(FadeIn(texto))
        self.play(Write(Text("6. Tokens más frecuentes")))
        bars = BarChart(
            values=[30, 25, 20, 15, 10],
            bar_names=["love", "life", "swim", "alone", "pain"],
            y_range=[0, 35, 5],
            bar_colors=[BLUE, GREEN, YELLOW, ORANGE, RED]
        )
        self.play(Create(bars))
        self.wait(2)

class AnalisisSentimiento(Scene):
    def construct(self):
        texto = MarkupText("""
        Se utilizó un diccionario léxico para clasificar las palabras como positivas o negativas,
        midiendo así la polaridad general de cada álbum.
        """).scale(0.5).to_edge(UP)
        self.play(FadeIn(texto))
        self.play(Write(Text("7. Análisis de sentimiento")))
        bars = BarChart(
            values=[60, 40],
            bar_names=["Positivo", "Negativo"],
            y_range=[0, 100, 20],
            bar_colors=[GREEN, RED]
        )
        self.play(Create(bars))
        self.wait(2)

class Bigramas(Scene):
    def construct(self):
        texto = MarkupText("""
        Los bigramas permiten observar asociaciones directas entre pares de palabras
        consecutivas, mostrando patrones de expresión lírica.
        """).scale(0.5).to_edge(UP)
        self.play(FadeIn(texto))
        self.play(Write(Text("8. Bigramas")))
        nodes = ["love", "you", "i", "life", "know"]
        edges = [("i", "love"), ("love", "you"), ("you", "know"), ("know", "life")]
        graph = Graph(
            vertices=nodes,
            edges=edges,
            layout="spring",
            vertex_config={"radius": 0.2},
            edge_config={"stroke_width": 2}
        )
        self.play(Create(graph))
        self.wait(2)

class ComponentesConexas(Scene):
    def construct(self):
        texto = MarkupText("""
        Se identificaron subredes dentro del grafo de bigramas. Algunas palabras
        tienden a formar grupos separados, indicando temas o emociones específicas.
        """).scale(0.5).to_edge(UP)
        self.play(FadeIn(texto))
        self.play(Write(Text("8.2.2 Componentes conexas")))
        nodes = ["pain", "alone", "swim", "cry"]
        edges = [("pain", "alone"), ("swim", "cry")]
        graph = Graph(
            vertices=nodes,
            edges=edges,
            layout="spring",
            vertex_config={"radius": 0.2, "fill_color": PURPLE},
            edge_config={"stroke_color": GRAY}
        )
        self.play(Create(graph))
        self.wait(2)

class Skipgrams(Scene):
    def construct(self):
        texto = MarkupText("""
        Los skip-grams permiten encontrar relaciones más distantes entre palabras,
        útiles para identificar conexiones semánticas indirectas.
        """).scale(0.5).to_edge(UP)
        self.play(FadeIn(texto))
        self.play(Write(Text("9. Skip-grams")))
        nodes = ["swim", "deep", "ocean", "feel"]
        edges = [("swim", "ocean"), ("deep", "feel")]
        graph = Graph(
            vertices=nodes,
            edges=edges,
            layout="spring",
            vertex_config={"radius": 0.2},
            edge_config={"stroke_width": 2}
        )
        self.play(Create(graph))
        self.wait(2)

class SkipgramasDefinitivos(Scene):
    def construct(self):
        self.play(Write(Text("9.5 Skipgramas Definitivos con todos los álbumes y su comparativa")))
        bars = BarChart(
            values=[25, 20, 15],
            bar_names=["Circles", "Swimming", "Divine Feminine"],
            y_range=[0, 30, 5],
            bar_colors=[BLUE, GREEN, ORANGE]
        )
        self.play(Create(bars))
        self.wait(2)

class RemoverUnigramas(Scene):
    def construct(self):
        self.play(Write(Text("9.5.3 Remover unigramas")))
        self.wait(1)

class OmitirStopWords(Scene):
    def construct(self):
        self.play(Write(Text("9.5.4 Omitir stop words")))
        self.wait(1)

class DefinirRedes(Scene):
    def construct(self):
        self.play(Write(Text("9.5.5 Definir las redes")))
        self.wait(1)

class Comparacion(Scene):
    def construct(self):
        self.play(Write(Text("10. Comparación")))
        self.wait(1)

class RedesComparativas(Scene):
    def construct(self):
        self.play(Write(Text("10.1 Redes Comparativas")))
        nodes = ["dream", "wake", "life", "die"]
        edges = [("dream", "wake"), ("life", "die")]
        graph = Graph(
            vertices=nodes,
            edges=edges,
            layout="spring",
            vertex_config={"radius": 0.2},
            edge_config={"stroke_color": YELLOW}
        )
        self.play(Create(graph))
        self.wait(2)

class PalabrasImportantes(Scene):
    def construct(self):
        self.play(Write(Text("10.2 Palabras más importantes")))
        bars = BarChart(
            values=[12, 11, 9],
            bar_names=["night", "dream", "love"],
            y_range=[0, 15, 3],
            bar_colors=[RED, BLUE, GREEN]
        )
        self.play(Create(bars))
        self.wait(2)

class Agrupamiento(Scene):
    def construct(self):
        self.play(Write(Text("10.3 Agrupamiento")))
        nodes = ["lonely", "alone", "cry", "tears"]
        edges = [("lonely", "alone"), ("cry", "tears"), ("alone", "cry")]
        graph = Graph(
            vertices=nodes,
            edges=edges,
            layout="circular",
            vertex_config={"radius": 0.2, "fill_color": PINK},
            edge_config={"stroke_color": DARK_GRAY}
        )
        self.play(Create(graph))
        self.wait(2)
