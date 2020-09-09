#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 18:38:00 2020

@author: avmejia
"""

import unittest

import busqueda_numero
import infraccion


class Testprueba (unittest.TestCase):

    def test_velocidad(self):
        self.assertEqual(infraccion.calculo_multa(60,False),0)
        self.assertEqual(infraccion.calculo_multa(65,False),1)
        self.assertEqual(infraccion.calculo_multa(85,False),2)
        self.assertEqual(infraccion.calculo_multa(85,True),1)
        self.assertEqual(infraccion.calculo_multa(64,True),0)
        self.assertEqual(infraccion.calculo_multa(65,True),0)
        
        
    def test_medio(self):
        self.assertEqual(busqueda_numero.encontrar_el_medio(15,10,30),15)
        self.assertEqual(busqueda_numero.encontrar_el_medio(1,2,3),2)
        self.assertEqual(busqueda_numero.encontrar_el_medio(11,12,15),12)
        
       




if __name__ == '__main__':
    unittest.main()