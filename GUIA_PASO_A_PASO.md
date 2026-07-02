# Guía paso a paso — De carpeta local a sitio publicado

> Todos los comandos se ejecutan en la terminal de Positron (o PowerShell), parado en `Documents\home-alan`. Este archivo es solo para ti; puedes borrarlo cuando el sitio esté publicado (o mantenerlo, no estorba).

## Paso 0 — Requisitos (una sola vez)

1. **Quarto CLI:** descarga desde https://quarto.org/docs/get-started/ e instala. Verifica: `quarto --version`
2. **Git:** verifica con `git --version`. Configura si es primera vez:
   ```bash
   git config --global user.name "Alan Del Rosario"
   git config --global user.email "delrosarioaj@outlook.com"
   ```
3. **Paquetes R** (para renderizar el post demo): en R ejecuta `install.packages(c("ggplot2", "readr", "rmarkdown", "knitr"))`

## Paso 1 — Probar el sitio localmente

```bash
cd Documents\home-alan
quarto preview
```

Se abre el navegador con el sitio. Cada cambio que guardes se refleja al instante. `Ctrl+C` en la terminal para detener.

## Paso 2 — Git init (el ÚNICO git init de esta carpeta)

```bash
git init
git add .
git commit -m "Sitio inicial: estructura Quarto + primer post (homicidios, Banco Mundial)"
```

Nota: `git add .` NO subirá `_site/`, `.Renviron`, `CLAUDE.md`, etc. — el `.gitignore` ya los excluye.

## Paso 3 — Crear el repo en GitHub y conectarlo

1. En github.com → New repository → nombre: `home-alan` → **público** → SIN readme (ya tenemos uno) → Create.
2. Conecta y sube:
   ```bash
   git remote add origin https://github.com/DelRosario20/home-alan.git
   git branch -M main
   git push -u origin main
   ```

## Paso 4 — Publicar en GitHub Pages

```bash
quarto publish gh-pages
```

Confirma con `Y`. Quarto renderiza, crea la rama `gh-pages` y activa Pages automáticamente. En ~2 minutos el sitio vive en:

**https://delrosario20.github.io/home-alan/**

## Paso 5 — Ciclo de trabajo diario (de aquí en adelante)

```
editar archivos → quarto preview (revisar) →
git add . → git commit -m "mensaje descriptivo" → git push →
quarto publish gh-pages (solo cuando quieras actualizar lo publicado)
```

El push guarda el código fuente; el publish actualiza el sitio visible. Son dos cosas separadas a propósito: puedes hacer commits de avances sin publicar.

## Pendientes de esta Fase 0

- [ ] Copiar tu `cv.pdf` a la raíz de esta carpeta (el enlace "CV" de la barra superior ya lo espera)
- [ ] Reemplazar `perfil.jpg` (placeholder gris) por tu foto real, con el mismo nombre de archivo
- [/] Ejecutar Pasos 1–4 (Pasos 1 y 2 completados; Pasos 3 y 4 pendientes de configurar el remoto en GitHub)
- [ ] Poner el link del sitio en tu perfil de GitHub y LinkedIn

## Si algo falla — dónde mirar

| Síntoma | Causa probable |
|---|---|
| `quarto: command not found` | Quarto no instalado o terminal sin reiniciar tras instalar |
| Error al renderizar el post | Falta un paquete R (`ggplot2`, `readr`, `knitr`, `rmarkdown`) |
| Push rechazado | El remote no coincide: revisa `git remote -v` |
| El sitio no aparece | Espera 2–3 min; revisa Settings → Pages en el repo |
| Cambié algo y no se ve en la web | Hiciste push pero no `quarto publish gh-pages` |
