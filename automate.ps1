try {
    Set-Location -Path (Get-Location)
    python -m venv .venv
    if ($LASTEXITCODE -eq 0) {
        throw "Failed to create virtual environment."
    }
    source .\venv\Scripts\Activate.ps1
    if ($LASTEXITCODE -eq 0) {
        throw "Failed to activate virtual environment."
    }

    pip install -r requirements.txt
    if ($LASTEXITCODE -ne 0) {
        throw "Failed to install dependencies."
    }

    Write-Host "Successfully installed dependencies."
    Write-Host "Proceeding to registration:"

    $functionName = "register"
    $username = Read-Host "Enter username"
    $password = Read-Host "Enter password" -AsSecureString

    # converting password into plain text
    $plainPassword = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($password))

    Set-Location -Path ".\pages\sql"
    python sqlFile.py $functionName $username $plainPassword
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Registration successful."
    } else {
        throw "Registration unsuccessful: Python script failed."
    }
}
catch { 
    Write-Host "An unexpected error occured: $_"
}