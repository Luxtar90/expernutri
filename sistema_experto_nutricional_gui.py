import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.pdfgen import canvas

# Base de Conocimiento: Planes alimenticios detallados
planes = {
    "salud": {
        "1": """Plan Salud - Ligero:
        Lunes: Desayuno - Avena con frutas. Almuerzo - Ensalada de quinoa. Cena - Sopa de verduras.
        Martes: Desayuno - Yogur con nueces. Almuerzo - Pechuga de pollo a la plancha. Cena - Ensalada mixta.
        Miércoles: Desayuno - Smoothie verde. Almuerzo - Pescado al vapor. Cena - Crema de espinacas.
        Jueves: Desayuno - Tostadas integrales con aguacate. Almuerzo - Ensalada de lentejas. Cena - Sopa minestrone.
        Viernes: Desayuno - Fruta fresca y té verde. Almuerzo - Arroz integral con verduras. Cena - Ensalada de espinacas.
        Sábado: Desayuno - Pan integral con tomate. Almuerzo - Tortilla de espinacas. Cena - Verduras al vapor.
        Domingo: Desayuno - Batido de frutas. Almuerzo - Ensalada de garbanzos. Cena - Caldo de pollo.""",
        "2": """Plan Salud - Moderado:
        Lunes: Desayuno - Batido de proteínas. Almuerzo - Ensalada de pollo. Cena - Sopa de verduras.
        Martes: Desayuno - Yogur griego con miel. Almuerzo - Tacos de pescado. Cena - Sopa de tomate.
        Miércoles: Desayuno - Smoothie de frutas. Almuerzo - Ensalada de pasta integral. Cena - Ensalada caprese.
        Jueves: Desayuno - Pan integral con aguacate. Almuerzo - Ensalada de quinoa. Cena - Sopa de zanahoria.
        Viernes: Desayuno - Omelette de claras. Almuerzo - Pollo al horno con vegetales. Cena - Ensalada César.
        Sábado: Desayuno - Pan integral con aguacate. Almuerzo - Tacos vegetarianos. Cena - Crema de champiñones.
        Domingo: Desayuno - Batido de frutas. Almuerzo - Ensalada de atún. Cena - Caldo de pollo.""",
        "3": """Plan Salud - Intensivo:
        Lunes: Desayuno - Tostadas integrales con aguacate. Almuerzo - Ensalada de pollo con quinoa. Cena - Sopa de lentejas.
        Martes: Desayuno - Smoothie de proteínas. Almuerzo - Pescado a la plancha con espárragos. Cena - Sopa de verduras.
        Miércoles: Desayuno - Avena con nueces. Almuerzo - Ensalada de garbanzos. Cena - Sopa de zanahoria.
        Jueves: Desayuno - Yogur con granola. Almuerzo - Pollo al vapor con vegetales. Cena - Crema de calabaza.
        Viernes: Desayuno - Smoothie verde. Almuerzo - Salmón a la parrilla con ensalada. Cena - Ensalada de espinacas.
        Sábado: Desayuno - Batido de frutas. Almuerzo - Ensalada de quinoa y pollo. Cena - Crema de espinacas.
        Domingo: Desayuno - Avena con frutas. Almuerzo - Tacos de pollo. Cena - Caldo de pollo.""",
    },
    "estetico": {
        "1": """Plan Estético - Ligero:
        Lunes: Desayuno - Tostadas integrales con aguacate. Almuerzo - Ensalada de pollo. Cena - Sopa de verduras.
        Martes: Desayuno - Smoothie de frutas. Almuerzo - Pescado al vapor. Cena - Ensalada de espinacas.
        Miércoles: Desayuno - Yogur con nueces. Almuerzo - Pechuga de pollo a la plancha. Cena - Sopa de tomate.
        Jueves: Desayuno - Pan integral con tomate. Almuerzo - Ensalada de quinoa. Cena - Crema de champiñones.
        Viernes: Desayuno - Smoothie verde. Almuerzo - Pollo al horno con vegetales. Cena - Sopa de zanahoria.
        Sábado: Desayuno - Avena con frutas. Almuerzo - Ensalada de lentejas. Cena - Sopa de calabaza.
        Domingo: Desayuno - Yogur griego con miel. Almuerzo - Tacos de pescado. Cena - Caldo de pollo.""",
        "2": """Plan Estético - Moderado:
        Lunes: Desayuno - Batido de proteínas. Almuerzo - Ensalada de pollo. Cena - Crema de espinacas.
        Martes: Desayuno - Yogur con nueces. Almuerzo - Pescado a la plancha con ensalada. Cena - Sopa de tomate.
        Miércoles: Desayuno - Tostadas integrales con aguacate. Almuerzo - Ensalada de garbanzos. Cena - Sopa de lentejas.
        Jueves: Desayuno - Smoothie de frutas. Almuerzo - Pollo al horno con vegetales. Cena - Sopa de zanahoria.
        Viernes: Desayuno - Pan integral con tomate. Almuerzo - Ensalada de quinoa. Cena - Sopa de calabaza.
        Sábado: Desayuno - Avena con frutas. Almuerzo - Tacos de pollo. Cena - Crema de champiñones.
        Domingo: Desayuno - Yogur griego con miel. Almuerzo - Salmón a la parrilla. Cena - Caldo de pollo.""",
        "3": """Plan Estético - Intensivo:
        Lunes: Desayuno - Batido de proteínas. Almuerzo - Pollo al horno con vegetales. Cena - Sopa de verduras.
        Martes: Desayuno - Smoothie de frutas. Almuerzo - Pescado a la parrilla. Cena - Ensalada de espinacas.
        Miércoles: Desayuno - Yogur con nueces. Almuerzo - Tacos de pollo. Cena - Sopa de zanahoria.
        Jueves: Desayuno - Avena con frutas. Almuerzo - Ensalada de quinoa. Cena - Sopa de lentejas.
        Viernes: Desayuno - Tostadas integrales con aguacate. Almuerzo - Ensalada de garbanzos. Cena - Sopa de calabaza.
        Sábado: Desayuno - Batido de proteínas. Almuerzo - Pollo al vapor con vegetales. Cena - Crema de espinacas.
        Domingo: Desayuno - Smoothie verde. Almuerzo - Salmón a la plancha. Cena - Caldo de pollo.""",
    }
}

def exportar_a_pdf(plan, nombre, peso_actual, peso_ideal, horas_ejercicio):
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if file_path:
        doc = SimpleDocTemplate(file_path, pagesize=A4)
        styles = getSampleStyleSheet()
        story = []

        # Título del documento
        title = Paragraph("Plan Alimenticio Recomendado", styles['Title'])
        story.append(title)
        story.append(Spacer(1, 12))

        # Datos del usuario
        datos_usuario = [
            ['Nombre:', nombre],
            ['Peso Actual:', f'{peso_actual} kg'],
            ['Peso Ideal:', f'{peso_ideal} kg'],
            ['Horas de Ejercicio por Día:', f'{horas_ejercicio} horas'],
        ]
        tabla_datos = Table(datos_usuario)
        tabla_datos.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        story.append(tabla_datos)
        story.append(Spacer(1, 12))

        # Contenido del plan
        plan_lines = plan.splitlines()
        for line in plan_lines:
            para = Paragraph(line.strip(), styles['BodyText'])
            story.append(para)
            story.append(Spacer(1, 12))

        # Marca de agua
        marca_agua = Paragraph("Trabajo hecho por Luiggi Arteaga", styles['Normal'])
        story.append(marca_agua)
        story.append(Spacer(1, 12))

        # Generar el PDF
        doc.build(story)
        messagebox.showinfo("Exportación Exitosa", f"El plan ha sido exportado a {file_path}")

def recomendar_plan():
    if not validar_entradas():
        return

    nombre = entry_nombre.get()
    objetivo = var_objetivo.get()
    horas_ejercicio = int(entry_horas_ejercicio.get())
    peso_actual = float(entry_peso_actual.get())
    peso_ideal = float(entry_peso_ideal.get())
    
    if objetivo == "salud":
        if horas_ejercicio <= 1:
            plan_recomendado = planes["salud"]["1"]
        elif horas_ejercicio <= 2:
            plan_recomendado = planes["salud"]["2"]
        else:
            plan_recomendado = planes["salud"]["3"]
    elif objetivo == "estetico":
        if horas_ejercicio <= 1:
            plan_recomendado = planes["estetico"]["1"]
        elif horas_ejercicio <= 2:
            plan_recomendado = planes["estetico"]["2"]
        else:
            plan_recomendado = planes["estetico"]["3"]

    exportar = messagebox.askyesno("Recomendación de Plan", f"{plan_recomendado}\n\n¿Deseas exportar este plan a PDF?")
    if exportar:
        exportar_a_pdf(plan_recomendado, nombre, peso_actual, peso_ideal, horas_ejercicio)

def validar_entradas():
    try:
        nombre = entry_nombre.get()
        peso_actual = float(entry_peso_actual.get())
        horas_ejercicio = int(entry_horas_ejercicio.get())
        peso_ideal = float(entry_peso_ideal.get())
        if not nombre or peso_actual <= 0 or horas_ejercicio < 0 or peso_ideal <= 0:
            raise ValueError
        return True
    except ValueError:
        messagebox.showerror("Error de Entrada", "Por favor, ingresa valores válidos.")
        return False

def iniciar_preguntas():
    pantalla_inicio.pack_forget()
    frame_preguntas.pack()

def mostrar_tutorial():
    tutorial_texto = """Bienvenido al Sistema Experto Nutricional.

    Paso 1: Ingrese su peso actual, las horas de ejercicio por día y su peso ideal.
    Paso 2: Seleccione si busca resultados estéticos o de salud.
    Paso 3: Indique si está dispuesto a comprometerse para conseguir sus objetivos.
    Paso 4: Haga clic en 'Obtener Recomendación' para recibir un plan alimenticio.
    Paso 5: Puede exportar el plan a PDF si lo desea.

    ¡Esperamos que disfrute de la aplicación y logre sus objetivos de salud y bienestar!"""
    messagebox.showinfo("Tutorial de Inicio", tutorial_texto)

def salir():
    root.quit()

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema Experto Nutricional Avanzado")

# Pantalla de inicio
pantalla_inicio = tk.Frame(root)
pantalla_inicio.pack(fill="both", expand=True)

tk.Label(pantalla_inicio, text="Sistema Experto Nutricional", font=("Helvetica", 18)).pack(pady=20)
tk.Label(pantalla_inicio, text="""Bienvenido al Sistema Experto Nutricional.
Este sistema te ayudará a obtener un plan alimenticio basado en tus datos y objetivos.

Instrucciones:
1. Ingresa tu nombre, peso actual, horas de ejercicio por día y tu peso ideal.
2. Selecciona si buscas resultados estéticos o de salud.
3. Indica si estás dispuesto a comprometerte para conseguir tus objetivos.
4. Haz clic en 'Obtener Recomendación' para recibir un plan alimenticio.
5. Puedes exportar el plan a PDF si lo deseas.

¡Comienza cuando estés listo!""", justify="left").pack(pady=10)
ttk.Button(pantalla_inicio, text="Comenzar", command=iniciar_preguntas).pack(pady=20)

# Frame para las preguntas
frame_preguntas = tk.Frame(root)

tk.Label(frame_preguntas, text="¿Cuál es tu nombre?").grid(row=0, column=0, pady=5)
entry_nombre = ttk.Entry(frame_preguntas)
entry_nombre.grid(row=0, column=1, pady=5)

tk.Label(frame_preguntas, text="¿Cuál es tu peso actual (kg)?").grid(row=1, column=0, pady=5)
entry_peso_actual = ttk.Entry(frame_preguntas)
entry_peso_actual.grid(row=1, column=1, pady=5)

tk.Label(frame_preguntas, text="¿Cuántas horas haces ejercicio al día?").grid(row=2, column=0, pady=5)
entry_horas_ejercicio = ttk.Entry(frame_preguntas)
entry_horas_ejercicio.grid(row=2, column=1, pady=5)

tk.Label(frame_preguntas, text="¿Cuál sería tu peso ideal (kg)?").grid(row=3, column=0, pady=5)
entry_peso_ideal = ttk.Entry(frame_preguntas)
entry_peso_ideal.grid(row=3, column=1, pady=5)

tk.Label(frame_preguntas, text="¿Con este tratamiento buscas resultados estéticos o de salud?").grid(row=4, column=0, pady=5)
var_objetivo = tk.StringVar(value="salud")
ttk.Radiobutton(frame_preguntas, text="Salud", variable=var_objetivo, value="salud").grid(row=4, column=1, pady=5, sticky="w")
ttk.Radiobutton(frame_preguntas, text="Estético", variable=var_objetivo, value="estetico").grid(row=4, column=2, pady=5, sticky="w")

tk.Label(frame_preguntas, text="¿Estás dispuesto a comprometerte para conseguir tus objetivos?").grid(row=5, column=0, pady=5)
var_compromiso = tk.StringVar(value="si")
ttk.Radiobutton(frame_preguntas, text="Sí", variable=var_compromiso, value="si").grid(row=5, column=1, pady=5, sticky="w")
ttk.Radiobutton(frame_preguntas, text="No", variable=var_compromiso, value="no").grid(row=5, column=2, pady=5, sticky="w")

# Botón para obtener la recomendación
ttk.Button(frame_preguntas, text="Obtener Recomendación", command=recomendar_plan).grid(row=6, column=0, columnspan=3, pady=10)

# Botón para salir
ttk.Button(frame_preguntas, text="Salir", command=salir).grid(row=7, column=0, columnspan=3, pady=10)

# Marca de agua en la interfaz gráfica
tk.Label(frame_preguntas, text="Trabajo hecho por Luiggi Arteaga", font=("Helvetica", 10), fg="gray").grid(row=8, column=0, columnspan=3, pady=20)

# Iniciar la ventana principal
root.mainloop()
