@echo off
set suds_cli=suds.exe
if NOT "%1" == "" (
	set suds_cli=%1
)

if "%2" == "serve" (
	goto :serve
)
if "%2" == "clean" (
	rd /s /q _sdm
	goto :eof
)

:: Get first doc-space file in the root folder
for /f %%F in ('dir /a-d /b *.yml') do (
	set docspace_config=%%~fF
	goto :start
)
goto :eof

:start
echo.
echo Doc space file: %docspace_config%
echo. 
for /d %%D in (*) do (
	if NOT "%%D" == "_sdm" if NOT "%%D" == ".git" (
		call :compile_docleaf %%~fD
	)
)
if "%2" == "compile" (
	goto :eof
)
goto :serve

:compile_docleaf
:: Process first doc-space file in the sub-folder
for /f %%F in ('dir /a-d /b %~1\*.yml') do (
	echo INPUT %~1
	%suds_cli% compile -c %~1\%%F
	goto :eof
)
exit /b

:: serve
:serve
%suds_cli% serve -c %docspace_config%