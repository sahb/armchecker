import requests

def print_ascii_art():
    art = """
 ▗▄▖ ▗▄▄▖ ▗▖  ▗▖     ▗▄▄▖▗▖ ▗▖▗▄▄▄▖ ▗▄▄▖▗▖ ▗▖▗▄▄▄▖▗▄▄▖ 
▐▌ ▐▌▐▌ ▐▌▐▛▚▞▜▌    ▐▌   ▐▌ ▐▌▐▌   ▐▌   ▐▌▗▞▘▐▌   ▐▌ ▐▌
▐▛▀▜▌▐▛▀▚▖▐▌  ▐▌    ▐▌   ▐▛▀▜▌▐▛▀▀▘▐▌   ▐▛▚▖ ▐▛▀▀▘▐▛▀▚▖
▐▌ ▐▌▐▌ ▐▌▐▌  ▐▌    ▝▚▄▄▖▐▌ ▐▌▐▙▄▄▖▝▚▄▄▖▐▌ ▐▌▐▙▄▄▖▐▌ ▐▌
                                                       
   """
    print(art)

ubuntu_versions = {
    "16.04": "xenial",
    "18.04": "bionic",
    "20.04": "focal",
    "22.04": "jammy",
    "24.04": "noble"
}

def check_arm64_package(package_name, ubuntu_codename):
    url = f"https://packages.ubuntu.com/{ubuntu_codename}/arm64/{package_name}"
    response = requests.get(url)
    return response.status_code != 404

def choose_ubuntu_version():
    print("Select the Ubuntu version for your search:")
    for i, (version, codename) in enumerate(ubuntu_versions.items(), start=1):
        print(f"{i}. Ubuntu {version} ({codename})")
    choice = int(input("Enter the number of the version: ")) - 1
    return list(ubuntu_versions.values())[choice]

def print_instructions():
    print("\nInstructions to generate the list of installed packages in Ubuntu:")
    print("1. Open your terminal.")
    print("2. Run the following command to generate the list of installed packages:")
    print("   dpkg --get-selections | awk '{print $1}' > installed_packages.txt")
    print("3. The file 'installed_packages.txt' will contain the list of packages.")
    print("4. Use this file as input when running this script.\n")

def main():
    print_ascii_art()

    print_instructions()
    
    packages_file = input("Enter the path to the file with the list of installed packages: ").strip()
    
    ubuntu_codename = choose_ubuntu_version()
    
    with open(packages_file, "r") as infile:
        packages = [package.strip() for package in infile if package.strip()]

    total_packages = len(packages)
    missing_arm64 = []

    print(f"Processing {total_packages} packages...")

    for index, package in enumerate(packages, start=1):
        if not check_arm64_package(package, ubuntu_codename):
            print(f"Missing {package}")
            missing_arm64.append(package)
        
        print(f"Processed {index}/{total_packages} packages", end='\r')

    print(f"\nProcessing complete. {len(missing_arm64)} packages do not have an arm64 version.")
    
    if missing_arm64:
        print("\nPackages without arm64 versions:")
        for package in missing_arm64:
            print(package)

if __name__ == "__main__":
    main()

