# XCode Command Line Tools

>xcode-select --install

# Install Homebrew

>ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
>echo PATH=/usr/local/bin:/usr/local/sbin:$PATH >> ~/.bash_profile
>source ~/.bash_profile
>brew tap homebrew/versions

# Install nmap

>brew install nmap

# Install libxml2

>brew install libxml2

# Install PostgreSQL

>brew install postgresql --without-ossp-uuid

# ruby 2.1.X

>brew install homebrew/versions/ruby21


# Initialize the database

>initdb /usr/local/var/postgres
>mkdir -p ~/Library/LaunchAgents
>cp /usr/local/Cellar/postgresql/9.4.0/homebrew.mxcl.postgresql.plist ~/Library/LaunchAgents/
>launchctl load -w ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist
>echo "alias pg_start='pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start'"
>echo "alias pg_stop='pg_ctl -D /usr/local/var/postgres stop'"

# Create the db for the metasploit framework

>createuser msf -P -h localhost
>createdb -O msf msf -h localhost

# Clone the Git Metasploit

>git clone https://github.com/rapid7/metasploit-framework.git /usr/local/share/metasploit-framework

# settings Env

>echo 'alias msfconsole="/usr/local/share/metasploit-framework && ./msfconsole && cd -"' >> ~/.zshrc
>echo 'alias msfbinscan="/usr/local/share/metasploit-framework && ./msfbinscan && cd -"' >> ~/.zshrc
>echo 'alias msfd="/usr/local/share/metasploit-framework && ./msfd && cd -"' >> ~/.zshrc
>echo 'alias msfelfscan="/usr/local/share/metasploit-framework && ./msfelfscan && cd -"' >> ~/.zshrc
>echo 'alias msfmachscan="/usr/local/share/metasploit-framework && ./msfmachscan && cd -"' >> ~/.zshrc
>echo 'alias msfpescan="/usr/local/share/metasploit-framework && ./msfpescan && cd -"' >> ~/.zshrc
>echo 'alias msfrop="/usr/local/share/metasploit-framework && ./msfrop && cd -"' >> ~/.zshrc
>echo 'alias msfrpc="/usr/local/share/metasploit-framework && ./msfrpc && cd -"' >> ~/.zshrc
>echo 'alias msfrpcd="/usr/local/share/metasploit-framework && ./msfrpcd && cd -"' >> ~/.zshrc
>echo 'alias msfupdate="/usr/local/share/metasploit-framework && ./msfupdate && cd -"' >> ~/.zshrc
>echo 'alias msfvenom="/usr/local/share/metasploit-framework && ./msfvenom && cd -"' >> ~/.zshrc
>sudo chmod go+w /etc/profile
>sudo echo export MSF_DATABASE_CONFIG=/usr/local/share/metasploit-framework/config/database.yml >> /etc/profile
>cd /usr/local/share/metasploit-framework
>bundle install

# Create the Database Configuration

>vim /usr/local/share/metasploit-framework/config/database.yml
Paste the following text:

production:
 adapter: postgresql
 database: msf
 username: msf
 password: <your password>
 host: 127.0.0.1
 port: 5432
 pool: 75
 timeout: 5

# update your environment

>source /etc/profile
>source ~/.bash_profile

> msfconsole
