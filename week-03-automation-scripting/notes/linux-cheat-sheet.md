# Week 3 Mastery: The 23 Essential Linux Commands for DevOps

This cheat sheet compiles the **23 essential Linux command-line utilities** specified in the DevOps 2026 Roadmap. As a DevOps engineer, navigating the Linux operating system, manipulating files, analyzing system performance, and troubleshooting remote servers directly from the CLI are critical daily operations.

Use this reference to complete your **Week 3 Labs** and save it directly into your `week-03-linux-os-and-shell-scripting/notes/` directory!

---

## 📂 Category 1: Directory & File Operations

### 1. `cd` (Change Directory)
*   **Purpose**: Navigate between directories in the filesystem.
*   **Common Flags / Syntax**:
    *   `cd ~` or `cd`: Go to the current user's home directory.
    *   `cd ..`: Move up one directory level (parent directory).
    *   `cd -`: Switch to the previous working directory.
*   **DevOps Real-World Example**: Navigate to the system configurations directory to inspect server settings:
    ```bash
    cd /etc/nginx/sites-available
    ```

### 2. `ls` (List)
*   **Purpose**: List directory contents.
*   **Common Flags**:
    *   `-l`: Long listing format (shows permissions, owner, size, and modification date).
    *   `-a`: Show hidden files (those starting with `.`, such as `.env` or `.git`).
    *   `-h`: Human-readable file sizes (e.g., 1K, 234M, 2G).
*   **DevOps Real-World Example**: List all files including hidden configuration profiles in long format:
    ```bash
    ls -lah
    ```

### 3. `mkdir` (Make Directory)
*   **Purpose**: Create one or more directories.
*   **Common Flags**:
    *   `-p`: Parent flag. Create nested directory structures without raising an error if parent directories do not exist yet.
*   **DevOps Real-World Example**: Create a deep workspace structure for a new microservice:
    ```bash
    mkdir -p src/app/static/images
    ```

### 4. `touch` (Touch File)
*   **Purpose**: Create an empty file instantly, or update the timestamp of an existing file.
*   **DevOps Real-World Example**: Initialize an empty environment configuration file or trigger a configuration refresh:
    ```bash
    touch .env.production
    ```

### 5. `cp` (Copy)
*   **Purpose**: Copy files or directories from a source to a destination.
*   **Common Flags**:
    *   `-r`: Recursive copy (required for copying directories and their contents).
    *   `-p`: Preserve file attributes (permissions, ownership, timestamps).
*   **DevOps Real-World Example**: Back up an active server configuration before applying modifications:
    ```bash
    cp -p /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak
    ```

### 6. `mv` (Move / Rename)
*   **Purpose**: Move files or directories, or rename them if the destination path remains the same.
*   **DevOps Real-World Example**: Archive a rotation log or rename a draft script:
    ```bash
    mv deploy_draft.sh deploy.sh
    ```

### 7. `rm` (Remove)
*   **Purpose**: Delete files or directories.
*   **Common Flags**:
    *   `-r`: Recursive deletion (required for directories).
    *   `-f`: Force deletion (suppresses confirmation prompts and ignores non-existent files).
*   **⚠️ Caution**: `rm -rf` is irreversible. Always verify your current path first using `pwd`.
*   **DevOps Real-World Example**: Clean up localized build assets:
    ```bash
    rm -rf ./dist/
    ```

### 8. `cat` (Concatenate)
*   **Purpose**: Display, combine, or write file content to the terminal output.
*   **DevOps Real-World Example**: Quickly inspect a Kubernetes pod log configuration or a system service file:
    ```bash
    cat /etc/systemd/system/app.service
    ```

---

## 🔍 Category 2: Search, Filtering & File Discovery

### 9. `grep` (Global Regular Expression Print)
*   **Purpose**: Search text within files using patterns or regular expressions.
*   **Common Flags**:
    *   `-i`: Case-insensitive search.
    *   `-r` or `-R`: Recursive search through directories.
    *   `-n`: Show line numbers of matching text.
    *   `-E`: Interpret pattern as an extended regular expression (ERE).
*   **DevOps Real-World Example**: Scan application logs to find and debug runtime errors:
    ```bash
    grep -rn "ERROR" /var/log/nginx/
    ```

### 10. `find` (Find Files)
*   **Purpose**: Search the directory tree for files based on attributes (name, size, type, modification time).
*   **Common Flags**:
    *   `-name`: Search by exact filename pattern.
    *   `-type`: Restrict search to files (`f`) or directories (`d`).
    *   `-mtime`: Search based on file modification time (in days).
*   **DevOps Real-World Example**: Locate all temporary log files modified within the last 7 days:
    ```bash
    find /var/log -type f -name "*.log" -mtime -7
    ```

---

## 🔐 Category 3: System Environment & Permissions

### 11. `printenv` (Print Environment)
*   **Purpose**: Print all or specific environment variables configured in the active shell shell.
*   **DevOps Real-World Example**: Verify the active target deployment environment:
    ```bash
    printenv NODE_ENV
    ```

### 12. `chmod` (Change Mode)
*   **Purpose**: Modify filesystem access permissions (Read `r`=4, Write `w`=2, Execute `x`=1) for User (`u`), Group (`g`), and Others (`o`).
*   **Common Targets**:
    *   `+x`: Make a file executable.
    *   `755`: Owner has full access (rwx); group/others have read and execute access (r-x).
    *   `600`: Owner has read/write (rw-); group/others have zero access (useful for SSH private keys).
*   **DevOps Real-World Example**: Set correct permissions on a newly written automation script and private SSH key:
    ```bash
    chmod +x deploy.sh
    chmod 600 id_rsa
    ```

---

## ⚡ Category 4: Process Management & Resource Monitoring

### 13. `ps` (Process Status)
*   **Purpose**: Display a snapshot listing of currently active system processes.
*   **Common Flags**:
    *   `aux`: Shows processes running for all users (`a`), including terminal-detached background processes (`x`), with detailed username and resource metrics (`u`).
*   **DevOps Real-World Example**: Search the process tree for an active Node.js runner process:
    ```bash
    ps aux | grep node
    ```

### 14. `kill` (Kill Process)
*   **Purpose**: Send termination signals to active processes using their Process ID (PID).
*   **Common Signals**:
    *   `-15` (SIGTERM): Ask the process to terminate gracefully (default).
    *   `-9` (SIGKILL): Force immediate process termination (use only if unresponsive).
*   **DevOps Real-World Example**: Force-stop a hung application process running on PID 4321:
    ```bash
    kill -9 4321
    ```

### 15. `top` (Table of Processes)
*   **Purpose**: Provide an interactive, real-time dynamic monitor of CPU usage, memory consumption, swap space, and processes.
*   **Key Controls**: Press `q` to quit, `M` to sort by memory, and `P` to sort by CPU usage.
*   **DevOps Real-World Example**: Monitor live resource usage on an active server host during a load-testing run:
    ```bash
    top
    ```

### 16. `df` (Disk Free)
*   **Purpose**: Display disk partition utilization and available file system space.
*   **Common Flags**:
    *   `-h`: Display sizes in easy-to-read human format (GB, MB).
*   **DevOps Real-World Example**: Check if a server partition is full (which often halts databases or logging engines):
    ```bash
    df -h
    ```

### 17. `du` (Disk Usage)
*   **Purpose**: Estimate and list the disk space used by specific files or folders recursively.
*   **Common Flags**:
    *   `-sh`: Display a human-readable total size summary of the target directory without listing individual nested files.
*   **DevOps Real-World Example**: Identify which specific application directory is consuming the most disk space:
    ```bash
    du -sh /var/log/*
    ```

---

## 📦 Category 5: Archiving & Compression

### 18. `tar` (Tape Archive)
*   **Purpose**: Package multiple files or folders into a single consolidated archive file (often called a tarball).
*   **Common Flags**:
    *   `-c`: Create a new archive.
    *   `-x`: Extract an existing archive.
    *   `-z`: Filter the archive through gzip compression.
    *   `-v`: Verbose (display processed files in terminal).
    *   `-f`: Specify the target filename of the archive.
*   **DevOps Real-World Example**: Create a compressed backup of directory data:
    ```bash
    tar -czvf backup.tar.gz /var/www/html/
    ```

### 19. `gzip` (GNU Zip)
*   **Purpose**: Compress files to reduce disk footprint (replaces them with a `.gz` extension) or expand them (`gunzip`).
*   **DevOps Real-World Example**: Compress historical database dumps:
    ```bash
    gzip database_dump.sql
    ```

---

## 🌐 Category 6: Networking, APIs & Remote Access

### 20. `ssh` (Secure Shell)
*   **Purpose**: Establish a secure, encrypted command-line connection to a remote server.
*   **Common Flags**:
    *   `-i`: Specify a private key file path for public-key authentication.
*   **DevOps Real-World Example**: Securely log into an active production host:
    ```bash
    ssh -i ~/.ssh/id_rsa admin@192.168.1.50
    ```

### 21. `scp` (Secure Copy)
*   **Purpose**: Securely copy files between local and remote hosts using SSH encryption.
*   **Common Flags**:
    *   `-r`: Recursively copy directories.
    *   `-i`: Specify the private key file path.
*   **DevOps Real-World Example**: Upload local production configurations to a remote server directory:
    ```bash
    scp -i ~/.ssh/prod_key.pem ./nginx.conf ubuntu@10.0.0.12:/etc/nginx/
    ```

### 22. `wget` (World Wide Web Get)
*   **Purpose**: Download files non-interactively from remote web links over HTTP, HTTPS, or FTP protocols.
*   **Common Flags**:
    *   `-O`: Rename the downloaded file to a specified filename.
*   **DevOps Real-World Example**: Download an application source binary:
    ```bash
    wget https://github.com/prometheus/prometheus/releases/download/v2.45.0/prometheus-2.45.0.linux-amd64.tar.gz
    ```

### 23. `curl` (Client URL)
*   **Purpose**: Transfer data to or from a network server using APIs or protocols (HTTP, HTTPS, FTP, etc.). Extremely powerful for testing endpoints.
*   **Common Flags**:
    *   `-I`: Fetch and display response headers only.
    *   `-X`: Specify HTTP request method (GET, POST, PUT, DELETE).
    *   `-H`: Append custom headers to the request.
    *   `-d`: Send specific request body data.
*   **DevOps Real-World Example**: Test if an Nginx web server or application endpoint is up and returning successful response headers:
    ```bash
    curl -I https://localhost:8080/health
    ```

---

## 🚀 DevOps Command Integration Challenge (Week 3 Preparation)
Test your muscle memory by combining multiple commands from this sheet to perform a common debugging task:

**Mission**: Write a single-line command chain that searches inside all Nginx error logs modified in the last 2 days, looks for "Permission denied" errors, and counts the matching instances.

**The Solution**:
```bash
find /var/log/nginx -type f -mtime -2 -name "*.log" -exec grep -i "Permission denied" {} + | wc -l
```
