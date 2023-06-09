# powershell -NoExit "conda shell.powershell activate ticket | Out-String | Invoke-Expression"
$a = Get-Location
Set-Location src

$env:ETICKET_MEMORY_MODE='1'
uvicorn api:app --reload

Set-Location $a