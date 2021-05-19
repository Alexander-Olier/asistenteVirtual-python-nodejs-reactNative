const express = require('express')
const router = express.Router()
module.exports = router ;
const preguntaController = require('../controllers/pregunta.controller')


router.get('/', preguntaController.listar)
router.get('/:pregunta',preguntaController.buscarPregunta)