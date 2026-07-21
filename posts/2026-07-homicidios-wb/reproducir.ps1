$ErrorActionPreference = "Stop"
$Here = Split-Path -Parent $MyInvocation.MyCommand.Path
$Root = (Resolve-Path "$Here/../..").Path

function Invoke-Checked {
    param([scriptblock]$Command, [string]$Stage)
    & $Command
    if ($LASTEXITCODE -ne 0) {
        throw "Falló la etapa '$Stage' (código $LASTEXITCODE)."
    }
}

Invoke-Checked { python "$Here/scripts/01_descarga.py" } "descarga"
Invoke-Checked { python "$Here/scripts/02_analisis.py" } "análisis"
Invoke-Checked { python "$Here/scripts/04_investigacion.py" } "investigación"
Invoke-Checked { python -m unittest discover -s "$Here/tests" -v } "pruebas"
Invoke-Checked { python "$Here/scripts/03_verificar.py" } "verificación"
Invoke-Checked { python "$Here/qa/verificar_rutas.py" } "rutas cruzadas"

# Sincronización deliberada: paper/ es un proyecto Quarto independiente y
# mantiene copias de las figuras y del .bib. Estas copias NO se editan a mano;
# este paso las refresca desde sus fuentes canónicas (outputs/ para figuras,
# projects/ para la bibliografía) para eliminar cualquier drift.
Copy-Item "$Here/outputs/figura_regimen.png", "$Here/outputs/figura_robustez.png", "$Here/outputs/figura_variaciones.png" "$Root/paper/assets/" -Force
Copy-Item "$Root/projects/referencias-homicidios.bib" "$Root/paper/referencias-homicidios.bib" -Force

Invoke-Checked { quarto render "$Root/paper/research-homicidios-ecuador.qmd" } "paper PDF"
Invoke-Checked { quarto render "$Root" } "sitio completo"

Write-Output "Cadena reproducible completada. El contenido sigue pendiente de revisión y aprobación editorial."
