from manim import *

class Intro(Scene):
    def construct(self):
        self.play(Write(Text("1. Introducción", font_size=40).shift(UP * 3 + LEFT * 0.5)))
        self.wait(1)
        texto = MarkupText("""
        Este análisis se enfoca en el contenido lírico de los álbumes de Mac Miller. A través de técnicas de minería de texto, se busca explorar los temas y emociones predominantes en sus letras, resaltando diferencias entre distintas etapas creativas.""")
        
        texto.set_color_by_gradient(BLUE, GREEN, YELLOW, ORANGE, RED)
        texto.scale(0.5),(DOWN)
        self.play(FadeIn(texto))
        self.wait(3) #completado (falta añadir nombres)

class CasoDeEstudio(Scene):
    def construct(self):
        self.play(Write(Text("2. Caso de estudio", font_size=40).shift(UP * 3 + LEFT * 0.5)))
        self.wait(1)
        texto = MarkupText("Se examinan dos álbumes: 'Circles' y 'Swimming'. El objetivo es comparar sus letras para encontrar patrones de cambio en el lenguaje, el tono emocional y la estructura lírica.")
        texto.set_color_by_gradient(BLUE, GREEN, YELLOW, ORANGE, RED)
        texto.scale(0.5),(DOWN)
        self.play(FadeIn(texto))
        self.play(texto.animate.shift(UP))
        Circles = ImageMobject("C:/Users/Usuario/my-project/Mac_Miller_-_Circles.png").scale(1.5).next_to(texto, DOWN, buff=0.5).shift(LEFT * 2.5)
        Swimming = ImageMobject("C:/Users/Usuario/my-project/Mac_Miller_-_Swimming.png").scale(1.5).next_to(texto, DOWN, buff=0.5).shift(RIGHT * 2.5)
        self.play(FadeIn(Circles, shift=UP))
        self.play(FadeIn(Swimming, shift=UP))
        self.wait(3) #completado

#decidir si vale la pena mantener esta escena

class ImportarTexto(Scene):
    def construct(self):
        self.play(Write(Text("3. Importar texto", font_size=26).to_corner(UR).shift(DOWN * 2.5 + LEFT * 0.5)))
        self.wait(1)
        texto = MarkupText("Se importa el archivo con las letras para su posterior análisis.")
        texto.set_color_by_gradient(BLUE, GREEN, YELLOW, ORANGE, RED)
        texto.scale(0.15).to_corner(UL).shift(DOWN * 0.5 + RIGHT * 0.5)
        self.play(FadeIn(texto))

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
        ).scale(0.5).next_to(texto, DOWN, buff=0.8)

        self.play(FadeIn(codigo, shift=UP))
        self.wait(3)



class Tokenizacion(Scene):
    def construct(self):
        title = Text("4. Tokenización", font_size=48)
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
        ).scale(0.5).next_to(title, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(FadeIn(codigo, shift=UP))
        self.wait(3)

class NormalizacionTexto(Scene):
    def construct(self):
        title = Text("5. Normalización del texto", font_size=48)
        texto = Paragraph(
            "Después de tokenizar, se eliminan signos de puntuación, números y caracteres especiales.",
            "También se convierten todas las palabras a minúsculas para asegurar consistencia.",
            alignment="center",
            font_size=30
        ).next_to(title, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(FadeIn(texto, shift=UP))
        self.wait(3)

class TokensMasFrecuentes(Scene):
    def construct(self):
        title = Text("6. Tokens más frecuentes", font_size=48)
        texto = Paragraph(
            "Se identificaron las palabras más frecuentes en cada álbum,",
            "permitiendo ver qué términos dominan el discurso lírico.",
            alignment="center",
            font_size=30
        ).next_to(title, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(FadeIn(texto))

        bars = BarChart(
            values=[30, 25, 20, 15, 10],
            bar_names=["love", "life", "swim", "alone", "pain"],
            y_range=[0, 35, 5],
            bar_colors=[BLUE, GREEN, YELLOW, ORANGE, RED],
            bar_label_scale_val=0.4
        ).scale(0.5).next_to(texto, DOWN, buff=0.8)

        self.play(Create(bars))
        self.wait(3)

class NubesPalabras(Scene):
    def construct(self):
        self.play(Write(Text("Nubes de palabras", font_size=40).shift(UP * 3 + LEFT * 0.5)))
        self.wait(1)
        texto = MarkupText("Las nubes de palabras visualizan la frecuencia de términos, donde el tamaño de cada palabra indica su uso en las letras.")
        texto.set_color_by_gradient(BLUE, GREEN, YELLOW, ORANGE, RED)
        texto.scale(0.5),(DOWN)
        self.play(FadeIn(texto))

        word_cloud = VGroup(
            Text("love", font_size=60),
            Text("life", font_size=50),
            Text("swim", font_size=40),
            Text("alone", font_size=30),
            Text("pain", font_size=20)
        ).arrange(DOWN, buff=0.2).scale(0.6).next_to(texto, DOWN, buff=0.6)

        for word in word_cloud:
            self.play(GrowFromCenter(word), run_time=0.4)
        self.wait(3)



class AnalisisSentimiento(Scene):
    def construct(self):
        title = Text("7. Análisis de sentimiento", font_size=48)
        texto = Paragraph(
            "Se evaluó el tono emocional de cada álbum usando diccionarios léxicos",
            "que clasifican palabras como positivas o negativas.",
            alignment="center",
            font_size=30
        ).next_to(title, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(FadeIn(texto))

        bars = BarChart(
            values=[60, 40],
            bar_names=["Positivo", "Negativo"],
            y_range=[0, 100, 20],
            bar_colors=[GREEN, RED],
            bar_label_scale_val=0.5
        ).scale(0.5).next_to(texto, DOWN, buff=0.8)

        self.play(Create(bars))
        self.wait(3)

class Bigramas(Scene):
    def construct(self):
        title = Text("8. Bigramas", font_size=48)
        texto = Paragraph(
            "Se analizaron pares de palabras consecutivas (bigramas)",
            "para identificar estructuras frecuentes en las letras.",
            alignment="center",
            font_size=30
        ).next_to(title, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(FadeIn(texto))

        nodes = ["love", "you", "i", "life", "know"]
        edges = [("i", "love"), ("love", "you"), ("you", "know"), ("know", "life")]
        graph = Graph(
            vertices=nodes,
            edges=edges,
            layout="spring",
            vertex_config={"radius": 0.2},
            edge_config={"stroke_width": 2}
        ).scale(0.6).next_to(texto, DOWN, buff=0.8)

        self.play(Create(graph))
        self.wait(3)

class ComponentesConexas(Scene):
    def construct(self):
        title = Text("8.2.2 Componentes conexas", font_size=48)
        texto = Paragraph(
            "Se identificaron subredes dentro del grafo de bigramas,",
            "revelando grupos de palabras que se relacionan temáticamente.",
            alignment="center",
            font_size=30
        ).next_to(title, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(FadeIn(texto))

        nodes1 = ["live", "gotta", "die", "gonna", "everybody's"]
        edges1 = [("everybody's", "gonna"), ("gonna", "die"), ("gotta", "live")]
        graph1 = Graph(vertices=nodes1, edges=edges1, layout="spring", vertex_config={"radius": 0.15})
        graph1.scale(0.5).to_edge(LEFT)

        nodes2 = nodes1 + ["build", "somethin", "beautiful"]
        edges2 = edges1 + [("gotta", "build"), ("build", "somethin"), ("somethin", "beautiful")]
        graph2 = Graph(vertices=nodes2, edges=edges2, layout="spring", vertex_config={"radius": 0.15})
        graph2.scale(0.5).to_edge(RIGHT)

        self.play(Create(graph1))
        self.play(Create(graph2))
        self.wait(3)

class SkipgramasDefinitivos(Scene):
    def construct(self):
        title = Text("9.5 Skipgramas - Comparativa de umbrales", font_size=42).to_corner(UL).shift(DOWN * 0.3 + RIGHT * 0.3)
        texto = Paragraph(
            "Se comparan redes generadas con diferentes umbrales:",
            "un umbral alto resalta conexiones fuertes, mientras que uno bajo muestra una red más densa.",
            alignment="left",
            font_size=24
        ).scale(0.4).next_to(title, DOWN, aligned_edge=LEFT, buff=0.3)

        self.play(FadeIn(title), run_time=1)
        self.play(FadeIn(texto), run_time=2)

        # Umbral 3 - izquierda
        umbral3_label = Text("Umbral = 3", font_size=26).to_corner(UL).shift(DOWN * 2.2 + RIGHT * 0.5)
        d1 = VGroup(*[Dot(radius=0.05) for _ in range(12)])
        d1.arrange_in_grid(rows=3, cols=4, buff=0.6).scale(0.8).shift(LEFT * 3 + DOWN * 1)
        lines1 = [
            Line(d1[0], d1[1]),
            Line(d1[1], d1[2]),
            Line(d1[3], d1[7]),
            Line(d1[8], d1[9]),
            Line(d1[10], d1[11])
        ]

        # Umbral 1 - derecha
        umbral1_label = Text("Umbral = 1", font_size=26).to_corner(UR).shift(DOWN * 2.2 + LEFT * 0.5)
        d2 = VGroup(*[Dot(radius=0.04) for _ in range(60)])
        d2.arrange_in_grid(rows=6, cols=10, buff=0.22).scale(0.6).shift(RIGHT * 3 + DOWN * 1)
        lines2 = [Line(d2[i], d2[i + 1]) for i in range(0, 59, 2)]

        self.play(FadeIn(umbral3_label), FadeIn(d1), run_time=1)
        self.play(AnimationGroup(*[Create(l) for l in lines1], lag_ratio=0.2, run_time=2))

        self.play(FadeIn(umbral1_label), FadeIn(d2), run_time=1)
        self.play(AnimationGroup(*[Create(l) for l in lines2], lag_ratio=0.05, run_time=2))

        self.wait(3)
