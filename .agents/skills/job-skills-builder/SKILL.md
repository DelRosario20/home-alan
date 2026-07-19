---
name: job-skills-builder
description: >-
  Habilidad especializada para expandir el módulo "JOBS SKILLS" en base a la información de bases/, contrastar soluciones (SQL, DAX, Python) y auditar bajo C-04.
---

# Job Skills Builder

## Overview
Esta habilidad especializada asiste al agente en el desarrollo, expansión y auditoría de contenido técnico para el módulo **JOBS SKILLS** de la aplicación **Aula Modular**, integrando las demandas reales del mercado (SQL, Power BI, Python, Analítica de Experiencia de Cliente e IA Conversacional) y garantizando el cumplimiento de los estándares semánticos y metodológicos del proyecto.

## Dependencies
* Ninguna dependencia externa de skills del sistema.

## Quick Start
Usa esta habilidad para:
1. Leer y estructurar información técnica de `bases/` para generar actividades de estudio.
2. Generar casos prácticos de simulación y contraste de soluciones técnicas para el portafolio del usuario.
3. Emitir reportes de validación independiente de contenido de acuerdo a la regla C-04.

## Workflow

### 1. Ingesta de Información de Origen (Bases)
- **Fuente de verdad**: Antes de escribir contenido nuevo para el módulo, lee exhaustivamente los manuales y guías almacenados por el usuario en el directorio `bases/`.
- Extrae la terminología clave para poblar el glosario núcleo (`coreGlossary`) y las especificaciones conceptuales básicas de cada lección.

### 2. Estructuración en Tiers y Formatos de Actividad
Genera contenido organizado rigurosamente bajo los siguientes niveles de profundidad y prioridad:
- **Tier 1 (Núcleo - SQL y Power BI)**:
  - SQL: Queries complejas (joins, agregaciones, subconsultas, CTEs) sobre bases de datos simuladas de transacciones de negocio.
  - Power BI: Ejercicios de relaciones (1 a muchos, muchos a muchos, dirección de filtrado), fórmulas DAX avanzadas (CALCULATE, FILTER, variables) y principios de storytelling visual.
- **Tier 2 (Complementario - Python)**: Pandas para manipulación de datos, limpieza de logs de chat y reportes estructurados.
- **Tier 3 (Específico - IA Conversacional/CX)**: Detección de tópicos, análisis de sentimiento, tasa de contención y resolución.
- **Tier 4 (Transversal - Excel y KPIs)**: Fórmulas financieras (márgenes, pricing, forecast) y analítica general.

Cada unidad del Tier 1 y Tier 3 debe incluir actividades tipo `identification` que modelen escenarios reales de trabajo o entrevistas.

### 3. Contraste de Soluciones Técnicas (Portafolio)
Dado que Power BI y otros entornos de datos no se integran de forma nativa en la ejecución del repositorio:
- Genera enunciados claros y datasets de prueba sintéticos (en Markdown, CSV o JSON).
- Proporciona la solución técnica ideal detalladamente (por ejemplo, el query SQL esperado con su lógica y plan de ejecución conceptual, o la fórmula DAX idónea) para que el usuario la ejecute en su entorno local y la contraste.

### 4. Cumplimiento de Calidad Semántica (Regla C-04)
Para cada lote de contenido nuevo generado:
- Valida la forma exacta contra el contrato de Zod importando `moduleContentSchema` de [module.schema.ts](file:///c:/Users/USER/Documents/app-estudio/src/schema/module.schema.ts).
- Crea un archivo de auditoría independiente en la carpeta `docs/lotes/` siguiendo la nomenclatura `LOTE-XXX.md`.
- Documenta detalladamente la muestra del contenido evaluado, los distractores plausibles identificados, la precisión factual contra las fuentes en `bases/` y la declaración explícita de independencia (el generador no aprueba su propio gate).

## Common Mistakes
* **Falta de Trazabilidad**: Omitir la fuente o locator en el campo `source` de la actividad. Cada ítem debe citar el manual o documentación técnica utilizada.
* **Simplificación**: Crear preguntas teóricas genéricas tipo test de opción múltiple para destrezas que requieren análisis práctico (como SQL o DAX). Usa actividades de tipo `identification` con casos de uso elaborados.
* **Falta de Coherencia de ID**: Reutilizar identificadores de actividades u objetivos de aprendizaje ya existentes en el módulo o en módulos hermanos.
