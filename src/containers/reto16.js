class Mayuscula{
    constructor(frase){
    this.frase=frase;
    }
    convertir(frase){
        if (typeof this.frase != 'string') {
            throw TypeError('El argumento debe ser una cadena de caracteres (texto).');
        }
    
        this.palabras = this.frase.split(' ');
    
        return this.palabras.map(p => p[0].toUpperCase() + p.slice(1)).join(' ');
    }
}

prueba = new Mayuscula("argentina campeón")
console.log(a.convertir(prueba));