""""/*
 * ¡Estoy de celebración! He publicado mi primer libro:
 * "Git y GitHub desde cero"
 * - Papel: mouredev.com/libro-git
 * - eBook: mouredev.com/ebook-git
 *
 * ¿Sabías que puedes leer información de Git y GitHub desde la gran
 * mayoría de lenguajes de programación?
 *
 * Crea un programa que lea los últimos 10 commits de este repositorio y muestre:
 * - Hash
 * - Autor
 * - Mensaje
 * - Fecha y hora
 *
 * Ejemplo de salida:
 * Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21:00
 *
 * Se permite utilizar librerías que nos faciliten esta tarea.
 */"""

import requests
from datetime import datetime

def leerUltimosCommits(num, usuario, repo):
    commits=f"https://api.github.com/repos/{usuario}/{repo}/commits"
    commits=requests.get(commits)
    
    if commits.status_code ==200: #Conexión exitosa a la api
        commits=commits.json() 
        i=0
        while i < num and i< len(commits):
           fecha=datetime.strptime(commits[i]["commit"]["committer"]["date"],"%Y-%m-%dT%H:%M:%SZ")
           print(f"Commit {i+1} | {commits[i]["sha"]} | {commits[i]["commit"]["author"]["name"]} | {commits[i]["commit"]["message"]} | {fecha.strftime("%d/%m/%Y %H:%M")}")
           i+=1

leerUltimosCommits(10,"mouredev","retos-programacion-2023")