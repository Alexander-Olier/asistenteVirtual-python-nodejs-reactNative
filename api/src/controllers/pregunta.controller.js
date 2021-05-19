const Datos = require('../models/pregunta.model')

exports.listar = function(req, res){
        Datos.lista(function (err, datos){
            console.log('controllers')
            if(err)
            res.send(err)
            console.log('res', datos)
            res.send(datos)
            
        })
}
exports.buscarPregunta = function(req, res){
    Datos.buscarPregunta(req.params.pregunta,function (err, datos){
        console.log('controllers')
        if(err)
        res.send(err)
        console.log('res', datos)
        res.send(datos)
    })
}