import requests

# ASCII art para "nuvoteq"
def print_ascii_art():
    art = """
 ▗▄▖ ▗▄▄▖ ▗▖  ▗▖     ▗▄▄▖▗▖ ▗▖▗▄▄▄▖ ▗▄▄▖▗▖ ▗▖▗▄▄▄▖▗▄▄▖ 
▐▌ ▐▌▐▌ ▐▌▐▛▚▞▜▌    ▐▌   ▐▌ ▐▌▐▌   ▐▌   ▐▌▗▞▘▐▌   ▐▌ ▐▌
▐▛▀▜▌▐▛▀▚▖▐▌  ▐▌    ▐▌   ▐▛▀▜▌▐▛▀▀▘▐▌   ▐▛▚▖ ▐▛▀▀▘▐▛▀▚▖
▐▌ ▐▌▐▌ ▐▌▐▌  ▐▌    ▝▚▄▄▖▐▌ ▐▌▐▙▄▄▖▝▚▄▄▖▐▌ ▐▌▐▙▄▄▖▐▌ ▐▌
                                                       
   """
    print(art)

# Lista de versões do Ubuntu e seus codinomes
ubuntu_versions = {
    "16.04": "xenial",
    "18.04": "bionic",
    "20.04": "focal",
    "22.04": "jammy",
    "24.04": "noble"
}

# Função para verificar se o pacote tem versão arm64 na versão selecionada
def check_arm64_package(package_name, ubuntu_codename):
    url = f"https://packages.ubuntu.com/{ubuntu_codename}/arm64/{package_name}"
    response = requests.get(url)
    return response.status_code != 404

# Função para exibir as versões e pedir a escolha do usuário
def choose_ubuntu_version():
    print("Select the Ubuntu version for your search:")
    for i, (version, codename) in enumerate(ubuntu_versions.items(), start=1):
        print(f"{i}. Ubuntu {version} ({codename})")
    choice = int(input("Enter the number of the version: ")) - 1
    return list(ubuntu_versions.values())[choice]

# Instruções para gerar o arquivo de pacotes
def print_instructions():
    print("\nInstructions to generate the list of installed packages in Ubuntu:")
    print("1. Open your terminal.")
    print("2. Run the following command to generate the list of installed packages:")
    print("   dpkg --get-selections | awk '{print $1}' > installed_packages.txt")
    print("3. The file 'installed_packages.txt' will contain the list of packages.")
    print("4. Use this file as input when running this script.\n")

# Função principal
def main():
    # Exibe a arte ASCII
    print_ascii_art()

    # Exibe instruções
    print_instructions()
    
    # Solicita o caminho do arquivo com a lista de pacotes
    packages_file = input("Enter the path to the file with the list of installed packages: ").strip()
    
    # Solicita a versão do Ubuntu
    ubuntu_codename = choose_ubuntu_version()
    
    # Abre o arquivo para ler os pacotes e processar
    with open(packages_file, "r") as infile:
        packages = [package.strip() for package in infile if package.strip()]

    total_packages = len(packages)
    missing_arm64 = []

    print(f"Processing {total_packages} packages...")

    # Verifica cada pacote
    for index, package in enumerate(packages, start=1):
        if not check_arm64_package(package, ubuntu_codename):
            print(f"Missing {package}")
            missing_arm64.append(package)
        
        # Exibe o progresso
        print(f"Processed {index}/{total_packages} packages", end='\r')

    print(f"\nProcessing complete. {len(missing_arm64)} packages do not have an arm64 version.")
    
    # Exibe os pacotes que não têm versão arm64
    if missing_arm64:
        print("\nPackages without arm64 versions:")
        for package in missing_arm64:
            print(package)

# Executa o script
if __name__ == "__main__":
    main()

