try {
    pip install -r requirements.txt
    Write-Host "Successfully installed dependencies."
    Write-Host "Proceeding to registration:"

    $functionName = "register"
    $username = Read-Host "Enter username"
    $password = Read-Host "Enter password" -AsSecureString

    # converting password into plain text
    $plainPassword = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($password))

    python sqlFile.py $functionName $username $plainPassword
}
catch { 
    Write-Host "An unexpected error occured: $_"
}