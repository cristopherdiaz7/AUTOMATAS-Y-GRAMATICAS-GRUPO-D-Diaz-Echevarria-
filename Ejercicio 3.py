import re
from collections import Counter

# ---------- A) Analizador de Email ----------
def analizar_emails(archivo):
    print("📧 Analizando Emails:")
    # Definimos 5 dominios y 5 países válidos
    dominios = ['gmail', 'outlook', 'yahoo', 'hotmail', 'live']
    paises = ['com', 'net', 'org', 'edu', 'ar']
    # Expresión regular
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

# ---------- B) Analizador de URLs ----------
def analizar_urls(archivo):
    print("🌐 Analizando URLs:")
    # Expresión regular de URL simplificada según las reglas
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

# ---------- C) Analizador de IPs ----------
def analizar_ips(archivo):
    print("🔢 Analizando Direcciones IP:")
    def ip_valida(ip):
        partes = ip.split('.')
        if len(partes) != 4:
            return False
        for parte in partes:
            if not parte.isdigit() or not (0 <= int(parte) <= 255):
                return False
        return True
    with open(archivo, 'r') as f:
        for linea in f:
            ip = linea.strip()
            if ip_valida(ip):
                print(f"✅ Válida: {ip}")
            else:
                print(f"❌ Inválida: {ip}")
    print()

# ---------- D) Contador de Palabras ----------
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

# ---------- Ejecutar todos ----------
def main():
    analizar_emails("emails.txt")
    analizar_urls("urls.txt")
    analizar_ips("ips.txt")
    contar_palabras("texto.txt")

if __name__ == "__main__":
    main()
