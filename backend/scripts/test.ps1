# powershell -NoExit "conda shell.powershell activate ticket | Out-String | Invoke-Expression"
$a = Get-Location
Set-Location src

$env:PYTHONPATH='.'
$env:ETICKET_MEMORY_MODE='1'
pytest

Set-Location $a