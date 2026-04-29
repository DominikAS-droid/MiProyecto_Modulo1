import libreria_clases_proyecto1 as lcp
import libreria_funciones_proyecto1 as lfp
import numpy as np
import pandas as pd
import streamlit as st


def mostrar_home():
    st.title("Proyecto 1")
    st.subheader("Modulo 1 - Python Fundamentals")

    c1, c2, c3 = st.columns([1, 3, 1])
    with c2:
        st.image("dmc.png", width="stretch")

    st.markdown("---")
    c1, c2 = st.columns([1, 1])
    with c1:
        st.write("**Nombres:** Aarom Leandro")
        st.write("**Carrera:** Ingenieria de Software")

    with c2:
        st.write("**Apellidos:** Giron Flores")
        st.write("**Año:** 2026")

    st.markdown("---")
    st.markdown("### Descripcion")
    st.write(
        "El proyecto consiste en desarrollar una aplicacion interactiva en Streamlit para poner en practica lo aprendido en este modulo."
    )

    st.markdown("---")
    st.markdown("### Tecnologias Utilizadas")
    st.write("Python, Streamlit, Pandas, Numpy")


def mostrar_ejercicio_1():
    st.title("Ejercicio 1")
    st.subheader("Registro de Movimientos Financieros")
    st.markdown(
        "Esta aplicación permite llevar un control de ingresos y gastos, calculando el saldo final y el estado del flujo de caja."
    )

    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    with st.form("Registro de Movimiento", clear_on_submit=True):
        operaciones = ["-- Seleccione --", "Ingreso", "Gasto"]

        tipo = st.selectbox("Elegir la operacion:", list(operaciones))
        concepto = st.text_input("Ingrese la fuente / fin:")
        valor = st.number_input("Ingrese el monto:", step=10.0)

        btn_agregar_1 = st.form_submit_button("Registrar Movimiento")

    if btn_agregar_1:
        if tipo == "-- Seleccione --":
            st.error("Debe seleccionar un tipo de operacion (Ingreso o Gasto).")
        elif not concepto:
            st.warning("La fuente / fin no puede estar vacio.")
        elif valor <= 0:
            st.warning("El monto debe ser mayor a 0.0")
        else:
            st.session_state.movimientos.append(
                {"Fuente / fin": concepto, "Operacion": tipo, "Monto": valor}
                # En caso de usar lista de listas y no lista de diccionarios
                # [concepto, tipo, valor]
            )
            st.success("Movimiento agregado")

    if st.session_state.movimientos:
        df = pd.DataFrame(st.session_state.movimientos)
        # En caso de usar lista de lista y no lista de diccionarios
        # df.columns = ["Fuente / Fin", "Operacion", "Monto"]

        st.subheader("Movimientos")
        st.dataframe(df, width="stretch")

        total_ingresos = df[df["Operacion"] == "Ingreso"]["Monto"].sum()
        total_gastos = df[df["Operacion"] == "Gasto"]["Monto"].sum()
        saldo_final = total_ingresos - total_gastos

        c1, c2, c3 = st.columns([1, 1, 1])
        c1.metric("Ingresos", f"${total_ingresos:,.2f}")
        c2.metric("Gastos", f"${total_gastos:,.2f}")
        c3.metric(
            "Saldo Final",
            f"${saldo_final:,.2f}",
            delta=f"{saldo_final:,.2f}",
            delta_color="normal",
        )

        if saldo_final >= 0:
            st.success(f"El flujo de caja está **A FAVOR**.")
        else:
            st.error(f"El flujo de caja está **EN CONTRA**.")


def mostrar_ejercicio_2():
    st.title("Ejercicio 2")
    st.subheader("Registro de Productos para Inventario")
    st.markdown(
        "Esta aplicación permite llevar un control de productos ingresados al inventario, calculando el total invertido y la ganancia estimada por su venta."
    )

    if "inventario" not in st.session_state:
        st.session_state.inventario = np.empty((0, 5))

    inventario = {
        "-- Seleccione --": ["-- Seleccione --"],
        "Lácteos": [
            "Leche Entera",
            "Yogur Natural",
            "Queso Crema",
            "Mantequilla",
            "Gelatina",
        ],
        "Congelados": [
            "Pizza Congelada",
            "Nuggets de Pollo",
            "Papas Fritas",
            "Helado de Vainilla",
            "Mezcla de Vegetales",
        ],
        "Limpieza": [
            "Detergente Líquido",
            "Desinfectante",
            "Jabón de Trastes",
            "Limpiador de Vidrios",
            "Cloro",
        ],
        "Mascotas": [
            "Croquetas Perro",
            "Alimento Gato",
            "Arena Sanitaria",
            "Juguete Mordedor",
            "Shampoo Mascotas",
        ],
        "Abarrotes": [
            "Arroz",
            "Frijoles",
            "Aceite Vegetal",
            "Pasta Espagueti",
            "Azúcar",
        ],
        "Bebidas": [
            "Agua Mineral",
            "Refresco de Cola",
            "Jugo de Naranja",
            "Té Frío",
            "Cerveza",
        ],
        "Cuidado Personal": [
            "Shampoo",
            "Pasta de Dientes",
            "Desodorante",
            "Jabón de Barra",
            "Crema Corporal",
        ],
        "Panadería": [
            "Pan de Caja",
            "Bolillo",
            "Donas",
            "Galletas",
            "Pastel de Chocolate",
        ],
    }

    todos_los_productos = []
    for lista in inventario.values():
        todos_los_productos.extend(lista)

    producto_seleccionado = st.selectbox("Selecciona un producto:", todos_los_productos)

    categoria_encontrada = ""
    for cat, productos in inventario.items():
        if producto_seleccionado in productos:
            categoria_encontrada = cat
            break

    with st.form("Registro de Inventario", clear_on_submit=True):
        st.text_input("Categoría detectada:", value=categoria_encontrada, disabled=True)

        costo_unitario = st.number_input("Ingrese el costo unitario:", step=1.5)
        previo_venta_unitario = st.number_input(
            "Ingrese el precio de venta unitario:", step=2.5
        )
        cantidad = st.number_input("Ingrese la cantidad:", step=5)

        btn_agregar_2 = st.form_submit_button("Guardar Movimiento")

    if btn_agregar_2:
        if producto_seleccionado == "-- Seleccione --":
            st.error("Debe seleccionar un producto para ser ingresado.")
        elif not costo_unitario:
            st.warning("El costo unitario no puede estar vacio.")
        elif not previo_venta_unitario:
            st.warning("El precio de venta unitario no puede estar vacio.")
        elif cantidad <= 0:
            st.warning("La cantidad debe ser mayor a 0.0")
        elif costo_unitario >= previo_venta_unitario:
            st.warning(
                "El costo unitario no puede ser mayor o igual al precio de venta unitario."
            )
        else:
            nueva_fila = np.array(
                [
                    [
                        producto_seleccionado,
                        categoria_encontrada,
                        costo_unitario,
                        previo_venta_unitario,
                        cantidad,
                    ]
                ]
            )
            st.session_state.inventario = np.vstack(
                [st.session_state.inventario, nueva_fila]
            )
            st.success("Producto registrado en el inventario")

    if len(st.session_state.inventario) > 0:
        columnas = pd.Index(
            ["Producto", "Categoría", "Costo Unitario", "Precio Venta", "Cantidad"]
        )
        df = pd.DataFrame(st.session_state.inventario, columns=columnas)

        df["Costo Unitario"] = pd.to_numeric(df["Costo Unitario"])
        df["Precio Venta"] = pd.to_numeric(df["Precio Venta"])
        df["Cantidad"] = pd.to_numeric(df["Cantidad"])

        st.subheader("Inventario")
        st.dataframe(df, width="stretch")

        total_inversion = (df["Costo Unitario"] * df["Cantidad"]).sum()
        total_esperado = (df["Precio Venta"] * df["Cantidad"]).sum()
        total_ganancia = total_esperado - total_inversion

        c1, c2, c3 = st.columns([1, 1, 1])
        c1.metric("Total Inversion", f"${total_inversion:,.2f}")
        c2.metric("Total Esperado", f"${total_esperado:,.2f}")
        c3.metric(
            "Total Ganancia",
            f"${total_ganancia:,.2f}",
            delta=f"{total_ganancia:,.2f}",
            delta_color="normal",
        )


def mostrar_ejercicio_3():
    st.title("Ejercicio 3")
    st.subheader("Calculo del Punto de Equilibrio")
    st.markdown(
        "Esta aplicación permite calcular el punto de equilibrio para cada producto fabricado por una empresa."
    )

    if "equilibrios" not in st.session_state:
        st.session_state.equilibrios = []

    with st.form("Punto de Equilibrio", clear_on_submit=True):
        nombre_proyecto = st.text_input("Nombre del producto:")
        costos_fijos = st.number_input("Costos fijos totales:", step=100.0)
        precio_unitario = st.number_input("Precio de venta unitario:", step=2.5)
        costo_variable_unitario = st.number_input("Costo variable unitario:", step=1.5)

        btn_calcular = st.form_submit_button("Calcular y registrar")

    if btn_calcular:
        if not nombre_proyecto:
            st.error("El nombre del producto no puede estar vacio.")
        elif costos_fijos <= 0:
            st.warning("Los costos fijos no pueden ser menores o iguales a 0.0")
        elif precio_unitario <= 0:
            st.warning("El precio unitario no puede ser menor o igual a 0.0")
        elif costo_variable_unitario <= 0:
            st.warning("El costo variable unitario no puede ser menor o igual a 0.0")
        elif precio_unitario <= costo_variable_unitario:
            st.error(
                "El precio de venta unitario debe ser mayor al costo variable unitario para tener margen."
            )
        else:
            resultados = lfp.calcular_punto_equilibrio(
                costos_fijos, precio_unitario, costo_variable_unitario
            )

            if resultados:
                registro = {
                    "Producto": nombre_proyecto,
                    "Costos Fijos": costos_fijos,
                    "Precio Unitario.": precio_unitario,
                    "CV Unitario.": costo_variable_unitario,
                    "Margen Cont.": resultados["margen_contribucion_unitario"],
                    "PE Unidades": resultados["punto_equilibrio_unidades"],
                    "PE Ventas": resultados["punto_equilibrio_ventas"],
                }
                st.session_state.equilibrios.append(registro)
                st.success("Cálculo realizado con éxito")

    # Mostrar resultados en tabla y métricas
    if st.session_state.equilibrios:
        df = pd.DataFrame(st.session_state.equilibrios)

        st.subheader("Historial de Cálculos")
        st.dataframe(df, width="stretch")

        ultimo = st.session_state.equilibrios[-1]

        st.subheader(f"Análisis del último registro: {ultimo['Producto']}")

        c1, c2, c3 = st.columns(3)
        c1.metric("Margen de Contribución", f"${ultimo['Margen Cont.']:,.2f}")
        c2.metric("P.E. Unidades", f"{ultimo['PE Unidades']:,} u.")
        c3.metric("P.E. Ventas", f"${ultimo['PE Ventas']:,.2f}")


def mostrar_ejercicio_4():
    st.title("Ejercicio 4")
    st.write("Aplicacion financiera para calculo de VPN, ROI y payback simple.")

    if "lista_proyectos" not in st.session_state:
        st.session_state.lista_proyectos = []

    tab_crear, tab_ver, tab_editar_borrar = st.tabs(
        ["Registrar", "Visualizar", "Gestionar"]
    )

    with tab_crear:
        with st.form("Proyecto Inversion", clear_on_submit=True):
            nombre = st.text_input("Nombre del Proyecto")
            inv_inicial = st.number_input(
                "Inversión Inicial", min_value=0.0, step=500.0
            )
            tasa = st.number_input(
                "Tasa de Descuento",
                min_value=0.0,
                max_value=100.0,
                value=0.0,
                step=1.5,
            )
            flujos_str = st.text_input(
                "Flujos de caja",
                placeholder="Ej: 1200, 1500, 1800",
            )

            btn_proyecto = st.form_submit_button("Registrar")

            if btn_proyecto:
                if nombre and flujos_str:
                    try:
                        flujos = [float(f.strip()) for f in flujos_str.split(",")]
                        nuevo_proyecto = lcp.ProyectoInversion(
                            nombre, inv_inicial, flujos, tasa
                        )

                        resumen_calculado = nuevo_proyecto.resumen()

                        registro = {
                            "obj": nuevo_proyecto,
                            "datos": resumen_calculado,
                            "config": {
                                "inv": inv_inicial,
                                "tasa": tasa,
                                "flujos": flujos_str,
                            },
                        }
                        st.session_state.lista_proyectos.append(registro)
                        st.success(f"Proyecto '{nombre}' registrado!")
                    except ValueError:
                        st.error(
                            "Asegúrate de que los flujos sean números separados por comas."
                        )

    with tab_ver:
        st.subheader("Historial de Proyectos")
        if st.session_state.lista_proyectos:
            df_mostrar = pd.DataFrame(
                [p["datos"] for p in st.session_state.lista_proyectos]
            )

            st.dataframe(
                df_mostrar,
                column_config={
                    "proyecto": "Nombre del Proyecto",
                    "vpn": "VPN ($)",
                    "roi_pct": "ROI (%)",
                    "payback_anios": "Payback (Años)",
                    "decision": "Estado",
                },
                width="stretch",
            )
        else:
            st.info("No hay proyectos registrados aún.")

    with tab_editar_borrar:
        if st.session_state.lista_proyectos:
            nombres = [p["datos"]["proyecto"] for p in st.session_state.lista_proyectos]
            seleccion = st.selectbox("Selecciona un proyecto", nombres)

            idx = nombres.index(seleccion)
            proyecto_seleccionado = st.session_state.lista_proyectos[idx]

            col1, col2 = st.columns(2)
            with col1:
                st.write("**Actualizar Gasto/Datos**")
                nueva_tasa = st.number_input(
                    "Nueva Tasa (%)",
                    value=float(proyecto_seleccionado["config"]["tasa"]),
                    key=f"upd_tasa_{seleccion}",
                )
                nuevos_flujos = st.text_input(
                    "Nuevos Flujos",
                    value=proyecto_seleccionado["config"]["flujos"],
                    key=f"upd_flujos_{seleccion}",
                )

                if st.button("Guardar Cambios"):
                    try:
                        flujos_list = [
                            float(f.strip()) for f in nuevos_flujos.split(",")
                        ]
                        updated_proyecto = lcp.ProyectoInversion(
                            seleccion,
                            proyecto_seleccionado["config"]["inv"],
                            flujos_list,
                            nueva_tasa,
                        )
                        st.session_state.lista_proyectos[idx]["datos"] = (
                            updated_proyecto.resumen()
                        )
                        st.session_state.lista_proyectos[idx]["config"]["tasa"] = (
                            nueva_tasa
                        )
                        st.session_state.lista_proyectos[idx]["config"]["flujos"] = (
                            nuevos_flujos
                        )
                        st.success("Proyecto actualizado.")
                        st.rerun()

                    except ValueError:
                        st.error(
                            "Asegúrate de que los flujos estén separados por comas y sean números."
                        )

            with col2:
                st.write("**Eliminar Registro**")
                st.warning("Esta acción no se puede deshacer.")
                if st.button("Eliminar definitivamente"):
                    st.session_state.lista_proyectos.pop(idx)
                    st.rerun()
        else:
            st.info("Nada que gestionar.")


paginas = {
    "Home": mostrar_home,
    "Ejercicio 1": mostrar_ejercicio_1,
    "Ejercicio 2": mostrar_ejercicio_2,
    "Ejercicio 3": mostrar_ejercicio_3,
    "Ejercicio 4": mostrar_ejercicio_4,
}

st.sidebar.title("Menu")
navegacion = st.sidebar.selectbox("Dirigir a:", list(paginas.keys()))
paginas[navegacion]()
