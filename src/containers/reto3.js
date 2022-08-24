
let num=(prompt("Ingrese un número: "))
function primo(número){
  if (número>2){
    for (var i = 2; número > 2 ; i++) {
      if (número%i == 0){
          return ("False")
      }
    return ("True")
 }
}
else{
    console.log("ha ingresado un numero que no es primo o ha ingresado numero 2 que si lo es")
 }
}
console.log(primo(num))


    