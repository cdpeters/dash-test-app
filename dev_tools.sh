Cyan='\033[0;36m'
BCyan='\033[1;36m'
BWhite='\033[1;37m'
Color_Off='\033[0m'

echo -e "${Cyan}=================== ${BCyan}DEV TOOLS${Cyan} ===================${Color_Off}"
echo
echo -e "${Cyan}Running ${BCyan}black${Cyan} code formatter:${Color_Off}"

black .

echo
echo -e "${Cyan}Running ${BCyan}isort${Cyan} import formatter:${Color_Off}"

isort .

echo
echo -e "${Cyan}Running ${BCyan}flake8${Cyan} code linter:${Color_Off}"

interrogate .

echo
echo -e "${Cyan}Running ${BCyan}flake8${Cyan} code linter:${Color_Off}"

flake8 .

echo
echo -e "${Cyan}============== ${BCyan}DEV TOOLS COMPLETED${Cyan} ==============${Color_Off}"
