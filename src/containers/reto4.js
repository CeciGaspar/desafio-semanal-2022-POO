let base= (prompt("Ingrese el valor de base"))
let altura= (prompt("Ingrese el valor de la altura"))
let tipoPoligono= (prompt("Ingrese el tipo de poligono"))

function areaPoligono(pbase, paltura, ppoligono){
    if (ppoligono == "triangulo"|| ppoligono== "rectangulo"|| ppoligono== "cuadrado"){
    
        if (ppoligono == "triangulo"){
            let area = (pbase * paltura/2)
            console.log("el area del", ppoligono, "es", area)}
        else{
            let area= (pbase * paltura)
            console.log("el area del", ppoligono, "es", area)}
    }else{
        console.log("ha ingresado una figura geometrica incorrecta")}
}
areaPoligono(base,altura,tipoPoligono)