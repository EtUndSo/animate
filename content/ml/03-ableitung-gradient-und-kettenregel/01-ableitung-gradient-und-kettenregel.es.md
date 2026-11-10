---
title: Visión general: Derivada, gradiente y regla de la cadena
kurz: Visión general
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Derivada, gradiente y regla de la cadena
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Capítulo 3: Derivada, gradiente y regla de la cadena
nachschlagen: ja
order: 15230100
summary: Cómo responde un número a sus entradas: de la recta tangente al modo inverso
tags: 
lang: es
---

## De qué trata

Un número depende a menudo de muchos otros números. El precio que la suma ponderada del [capítulo 1](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) predice para una vivienda depende de cada peso y de cada característica. La longitud de un vector de error depende de cada una de sus componentes. El resultado de un cálculo largo depende de cada valor con el que empieza. Este capítulo pregunta: ¿cuánto y en qué sentido cambia un número así cuando se modifica un poco una de sus entradas? Y si son miles de entradas: ¿en qué dirección hay que desplazarlas todas a la vez para que el número crezca o disminuya lo más rápido posible?

A ello se suma una pregunta práctica. A menudo, el número surge de una larga cadena de pasos de cálculo sencillos. Se podría modificar un poco cada entrada por separado y mirar qué sale al final. Con un millón de entradas, eso supondría repetir el cálculo entero un millón de veces. ¿Se puede hacer más rápido? ¿Y cómo se comprueba si una fórmula para estas sensibilidades, que uno mismo ha deducido o programado, es realmente correcta?

La utilidad: con las respuestas se sabe de qué perillas de ajuste depende más un resultado y cómo repercuten en él los pequeños errores de medida de las entradas. Se puede sustituir una función complicada, cerca de un punto, por otra mucho más sencilla y estimar lo grande que es el error que se comete. Y se pueden calcular las sensibilidades incluso cuando el número surge de un cálculo muy largo con muchísimas entradas. Estas herramientas las necesita casi todo método que aprende a partir de datos.

**Cómo trabajar con este capítulo.** Las secciones se apoyan unas en otras y cada término nuevo tiene su propia subsección con un ejemplo. Los recuadros desplegables contienen el contexto (por qué funciona un método y de dónde viene), deducciones y demostraciones; no hacen falta para seguir leyendo. Intenta primero los ejercicios (de ★ a ★★★) por tu cuenta y ejecuta de verdad los programas; la solución se despliega justo debajo de cada ejercicio.
