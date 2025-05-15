@echo off
setlocal
cd /d %~dp0

echo === [1] Gerando HTML ===
call make.bat html
start build\html\index.html

echo.
echo === [2] Gerando LaTeX (.tex) ===
sphinx-build -b latex source build/latex

echo.
echo === [3] Gerando PDF com pdflatex ===
if exist build\latex\manualdeestruturasorganizacionais.tex (
    cd build\latex
    echo Executando pdflatex 3x...
    pdflatex manualdeestruturasorganizacionais.tex
    pdflatex manualdeestruturasorganizacionais.tex
    pdflatex manualdeestruturasorganizacionais.tex
    echo PDF gerado com sucesso!
    start manualdeestruturasorganizacionais.pdf
    cd ../..
) else (
    echo ERRO: Arquivo manualdeestruturasorganizacionais.tex NAO encontrado!
)

echo.
echo === Processo concluído ===
pause
endlocal
