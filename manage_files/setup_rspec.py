#!/usr/bin/env python3
import os

def banner():
    print('''
   _____ ______    ____  __   ____  _____ ____  ____________   _____ ______________  ______  
  / ___//  _/ /   / /\ \/ /  / __ \/ ___// __ \/ ____/ ____/  / ___// ____/_  __/ / / / __ \ 
  \__ \ / // /   / /  \  /  / /_/ /\__ \/ /_/ / __/ / /       \__ \/ __/   / / / / / / /_/ / 
 ___/ // // /___/ /___/ /  / _, _/___/ / ____/ /___/ /___    ___/ / /___  / / / /_/ / ____/  
/____/___/_____/_____/_/  /_/ |_|/____/_/   /_____/\____/   /____/_____/ /_/  \____/_/       
                                                                                                                                                          
''')

def main():
    banner()
    directories = [ 'lib', 'scripts', 'bin' ]

    for dir in directories:
        os.makedirs(dir)

    if len(directories) > 1 and os.path.isdir(directories[1]):
        file_name    = os.path.basename(__file__)
        current_path = os.getcwd()
        file         = os.path.join(current_path, file_name)
        dest_path    = os.path.join(current_path, directories[1], file_name)

        if os.path.exists(file_name):
            os.rename(file_name, dest_path)

    with open('.ruby-version', 'w') as arquivo:
        arquivo.write('3.2.0\n')

    with open('Gemfile', 'w') as arquivo:
        arquivo.write("source 'https://rubygems.org'\n\nruby '~> 3.2'\n\ngem 'rspec', '~> 3.12'\n")

def run():
    command = ['bundle install', 'rspec --init']

    for cmd in command:
        os.system(cmd)

if __name__ == "__main__":
    main()
    run()