# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeneticSimplifier
                                 A QGIS plugin
 Line simplification tool using genetic algorithms
                             -------------------
        begin                : 2014-09-11
        copyright            : (C) 2014 by Luiz Andrade
        email                : luiz.claudio@dsg.eb.mil.br
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load GeneticSimplifier class from file GeneticSimplifier
    from geneticsimplifier import GeneticSimplifier
    return GeneticSimplifier(iface)
