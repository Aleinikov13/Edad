Feature: Edad de una persona
	Como usuario de la calculadora de edades
	deseo obtener una descripcion segun la edad
	para obtener el resultado

	Scenario: edad de una persona
		Dado que ingreso la edad "0"
		cuando realizo la operación
		entonces obtengo el resultado "No Existes"

	Scenario: edad de una persona
		Dado que ingreso la edad "12"
		cuando realizo la operación
		entonces obtengo el resultado "Eres Nino"

	Scenario: edad de una persona
		Dado que ingreso la edad "17"
		cuando realizo la operación
		entonces obtengo el resultado "Eres Adolescente"

	Scenario: edad de una persona
		Dado que ingreso la edad "64"
		cuando realizo la operación
		entonces obtengo el resultado "Eres Adulto"

	Scenario: edad de una persona
		Dado que ingreso la edad "119"
		cuando realizo la operación
		entonces obtengo el resultado "Eres Adulto Mayor"

	Scenario: edad de una persona
		Dado que ingreso la edad "150"
		cuando realizo la operación
		entonces obtengo el resultado "Eres Mumm-Ra"






		

