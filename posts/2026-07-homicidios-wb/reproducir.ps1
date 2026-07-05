$ErrorActionPreference = "Stop"
$Here = Split-Path -Parent $MyInvocation.MyCommand.Path

function Invoke-Checked {
    param([scriptblock]$Command, [string]$Stage)
    & $Command
    if ($LASTEXITCODE -ne 0) {
        throw "Falló la etapa '$Stage' (código $LASTEXITCODE)."
    }
}

Invoke-Checked { python "$Here/scripts/01_descarga.py" } "descarga"
Invoke-Checked { python "$Here/scripts/02_analisis.py" } "análisis"
Invoke-Checked { python -m unittest discover -s "$Here/tests" -v } "pruebas"
Invoke-Checked { python "$Here/scripts/03_verificar.py" } "verificación"
Invoke-Checked { quarto render "$Here/index.qmd" } "render"

Write-Output "Cadena reproducible completada. El contenido sigue pendiente de revisión y aprobación editorial."
