# -*- coding: utf-8 -*-
from lettuce import step, world
from edad import Edad

@step(u'Dado que ingreso la edad "([^"]*)"')
def dado_que_ingreso_la_edad_group1(step, edad):
	world.ed = Edad()
	world.ed.edad(int(edad))

@step(u'cuando realizo la operación')
def cuando_realizo_la_operacion(step):
	pass

@step(u'entonces obtengo el resultado "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
	assert esperado == world.ed.obtener_resultado(), 'El resultado esperado es '+esperado+ ' y el obtenido es '+str(world.ed.obtener_resultado())
