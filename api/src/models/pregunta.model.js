var conexion = require('../../config/concection')

var Datos = function(datos){
    this.pregunta = dato.pregunta
    this.respuesta = dato.respuesta;
};

Datos.lista = function( result){
    conexion.query("SELECT * FROM pregunta", function(res, err){
        if (err){
            console.log(err)
            result(null, err)
        }else{
            console.log(res)
            result(null,res)
        }
    })
}

Datos.listaUno = function(id, result){
        conexion.query(`SELECT * FROM pregunta WHERE id =`,id, function(err, res){
        if (err){
            console.log(err)
            result(null, err)
        }else{
            console.log(res) 
            result(null,res)
        }
    });
}
Datos.buscarPregunta = function(pregunta,result){
    conexion.query(`SELECT respuesta FROM pregunta WHERE pregunta ='${pregunta}'`, function(err, res){
        if (err == true){
            console.log(err)
            result(null, err)
        }else{
            console.log(res)
            result(null,res)
        }
    })
}
module.exports = Datos;