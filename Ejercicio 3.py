import re
import os
from collections import Counter

ejemplos = {
    "emails.txt": [
        "juan123@gmail.com",
        "_marta@outlook.com",
        "pepe@dominio.org",
        "luis.lopez@yahoo.ar",
        "ana-92@live.net"
    ],
    "urls.txt": [
        "https://www.google.com",
        "http://facebook.com",
        "www.youtube.com",
        "twitter.com/",
        "https://invalido.com.pe"
    ],
    "ips.txt": [
        "192.168.1.1",
        "256.100.50.0",
        "10.0.0.256",
        "8.8.8.8",
        "127.0.0.1"
    ],
    "texto.txt": [
        "Hola universidad de mendoza, carrera ingenieria en informatica automatas y gramaticas"
    ]
}


def crear_archivos():
    for nombre, lineas in ejemplos.items():
        if not os.path.exists(nombre):
            with open(nombre, 'w') as f:
                f.write('\n'.join(lineas))
            print(f"✅ Archivo creado: {nombre}")


def analizar_emails(archivo):
    print("📧 Analizando Emails:")
    dominios = ['gmail', 'outlook', 'yahoo', 'hotmail', 'live']
    paises = ['com', 'net', 'org', 'edu', 'ar']
    regex = re.compile(
        r'^[a-zA-Z][\w\.-]*@(' + '|'.join(dominios) + r')\.(' + '|'.join(paises) + r')$'
    )
    with open(archivo, 'r') as f:
        for linea in f:
            email = linea.strip()
            if regex.match(email):
                print(f"✅ Válido: {email}")
            else:
                print(f"❌ Inválido: {email}")
    print()


def analizar_urls(archivo):
    print("🌐 Analizando URLs:")
    regex = re.compile(
        r'^(https?://)?(www\.)?[\w\-]+\.(com)(/|\?.*)?$'
    )
    with open(archivo, 'r') as f:
        for linea in f:
            url = linea.strip()
            if regex.match(url):
                print(f"✅ Válida: {url}")
            else:
                print(f"❌ Inválida: {url}")
    print()


def analizar_ips(archivo):
    print("🔢 Analizando Direcciones IP:")
    def ip_valida(ip):
        partes = ip.split('.')
        return len(partes) == 4 and all(
            parte.isdigit() and 0 <= int(parte) <= 255 for parte in partes
        )
    with open(archivo, 'r') as f:
        for linea in f:
            ip = linea.strip()
            if ip_valida(ip):
                print(f"✅ Válida: {ip}")
            else:
                print(f"❌ Inválida: {ip}")
    print()


def contar_palabras(archivo):
    print("📊 Conteo de Palabras:")
    with open(archivo, 'r') as f:
        texto = f.read().lower()
        palabras = re.findall(r'\b\w+\b', texto)
        conteo = Counter(palabras)
        palabra_mas_comun, cantidad = conteo.most_common(1)[0]
        print(f"Total de palabras: {len(palabras)}")
        print(f"Palabra más repetida: '{palabra_mas_comun}' aparece {cantidad} veces.")
    print()


def main():
    crear_archivos()
    analizar_emails("emails.txt")
    analizar_urls("urls.txt")
    analizar_ips("ips.txt")
    contar_palabras("texto.txt")

if __name__ == "__main__":
    main()

