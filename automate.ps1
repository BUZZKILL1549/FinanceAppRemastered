try {
    # Execute the MySQL command and capture output and errors
    $output = Get-Content initializeDatabase.sql | mysql -u root -p school_app 2>&1

    # Check the last exit code; if it's not 0, an error occurred
    if ($LASTEXITCODE -ne 0) {
        if ($output -match "ERROR 1007") {
            Write-Output "Custom Message: The database 'school_app' already exists. Please check your database setup."
        }
        elseif ($output -match "ERROR 1049") {
            Write-Output "Custom Message: Unknown database. The specified database does not exist."
        }
        elseif ($output -match "ERROR 1064") {
            Write-Output "Custom Message: SQL syntax error. Check the SQL statements in your script."
        }
        else {
            Write-Output "An unexpected error occurred: $output"
        }
    }
    else {
        Write-Output "Database initialized successfully."
    }
}
catch {
    Write-Output "Failed to execute MySQL command: $_"
}

try {
    pip install -r requirements.txt
}
catch {
    Write-Output "An unexpected error occured: $_"
}