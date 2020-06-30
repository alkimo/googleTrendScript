import argparse

def initParse():
    # Initiate the parser
    parser = argparse.ArgumentParser()

    # Add long and short argument
    parser.add_argument("-a", help="Primeiro valor de pesquisa")
    parser.add_argument("-b", help="Segundo valor de pesquisa")
    parser.add_argument("-c", help="Terceiro valor de pesquisa")
    parser.add_argument("-d", help="Quarto valor de pesquisa")
    parser.add_argument("-e", help="Quinto valor de pesquisa")

    parser.add_argument("--geo", "-g", help="Área geográfica")
    parser.add_argument("--timeframe", "-time", help="Intervalo temporal")
    parser.add_argument("--cat", "-k", help="Categoria")
    parser.add_argument("--gprop", "-gp", help="Serviço do google a fazer a pesquisa")

    # Read arguments from the command line
    args = parser.parse_args()

    if(args.a == None):
        args.a = "Corona"

    if(args.geo == None):
        args.geo = "US"

    if(args.timeframe == None):
        args.timeframe = "2020-05-10 2020-05-25"

    if(args.cat == None):
        args.cat = 0
    
    if(args.gprop != None):
        args.gprop = ''

    return args