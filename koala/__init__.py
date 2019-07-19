# Copyright (c) 2019 Yann BOUYERON
#
#
# licensed under GNU GPL version 3 (or later)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>. 




import os

import matplotlib

if 'DISPLAY' not in os.environ:
	
	matplotlib.use('Agg') 

import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame
import attrdict
import ipfshttpclient

__version__ = "0.0.1"

__author__ = "Yann Bouyeron"

__all__ = ["Koala"]


try:

	ipfs = ipfshttpclient.connect('/dns/ipfs.infura.io/tcp/5001/https')

except:

	pass



class Koala(DataFrame):

	""" 
	Classe héritant de pandas.DataFrame

	Les objets de cette classe s’instancient comme un DataFrame classique

      """
	
	def __init__(self, data):
		
		super().__init__(data)
		
		
	def selection(self,x,y):
		
		if type(x) == type(int()) and type(y) == type(int()) and x < len(self.columns) and y < len(self.columns) and x >= 0 and y >= 0:
			
			x_name = self.columns[x]
			y_name = self.columns[y]
			
			
			
		elif type(x) == type(str()) and type(y) == type(str()) and x in self.columns and y in self.columns:
			
			x_name = x
			y_name = y
			
		else:
			
			return None
			
		
		x = self[x_name]
		y = self[y_name]
		
		return x_name, y_name, np.array(x,dtype=float), np.array(y,dtype=float)
		
		
		
	def lin(self, x, y, show=True):
		
		"""Teste une régression linéaire.

		Arguments:

			x: nom [str] ou index [int] de colonne
			y: nom [str] ou index [int] de colonne
			show: [bool] , défaut=True, Si True, le graphique avec la droite de regression est affiché

		Return:

			AttrDict {'a', 'b', 'r', 'equation', 'graph'}

		"""
		
		x_name, y_name, x, y = self.selection(x, y)
		
		l = np.polyfit(x,y,1)
		a = l[0]
		b = l[1]
		cc = np.corrcoef(x,y)
		r = cc[0,1]
		f = 'y = '+ str(round(a,2)) + 'x + ' + str(round(b,2))
		
		
		plt.close()
		plt.plot(x, y, '^k', label='Original data', markersize=4)
		plt.plot(x, [a*i + b for i in x], '--b', label='Fitted line - linear regression')
		plt.title('{0} = a * {1} + b'.format(y_name,x_name),fontsize=7)
		plt.xlabel(x_name,fontsize=7)
		plt.ylabel(y_name,fontsize=7)
		plt.legend(fontsize=6)
		
		if show == True:
				
				try:
					
					plt.show()
					
				except:
					
					pass
			
		return attrdict.AttrDict({"a":a, "b":b, "r":r, "equation":f, "graph":plt})
	
	
	
	def exp(self, x, y, show=True):

		"""
		Teste une régression exponentielle.

		Arguments:

			x: nom [str] ou index [int] de colonne
			y: nom [str] ou index [int] de colonne
			show: [bool] , défaut=True, Si True, le graphique avec la droite de regression est affiché

		Return:

			AttrDict {'a', 'b', 'r', 'equation', 'graph'}

		"""
	
		x_name, y_name, x, y = self.selection(x, y)
		
		try: 
			
			Y = np.log(y)
			p = np.polyfit(x,Y,1)
			N = p[1]
			a = np.exp(N)
			b = p[0]
			cc = np.corrcoef(x,Y)
			r = cc[0,1]
			f = 'y = '+ str(round(a,2)) + ' *exp(' + str(round(b,2)) + 'x)'
							
			plt.close()
			plt.plot(x, y, '^k', label='Original data', markersize=2)
			plt.plot(x, [a*np.exp(b*i) for i in x], '--r', label='Fitted line - Exponential regression')
			plt.title('Regression Exponentielle y = a.exp(bx)', fontsize=5)
			plt.xlabel(x_name,fontsize=5)
			plt.ylabel(y_name,fontsize=5)
			plt.legend(fontsize=5)
			
			if show == True:
				
				try:
					
					plt.show()
					
				except:
					
					pass
				
			return attrdict.AttrDict({"a":a, "b":b, "r":r, "equation":f, "graph":plt})
		
		except:
			
			return None
			
			
	
	def pwr(self, x, y ,show=True):

		"""
		Teste une régression puissance.

		Arguments:

			x: nom [str] ou index [int] de colonne
			y: nom [str] ou index [int] de colonne
			show: [bool] , défaut=True, Si True, le graphique avec la droite de regression est affiché

		Return:

			AttrDict {'a', 'b', 'r', 'equation', 'graph'}
		"""
		
		x_name, y_name, x, y = self.selection(x, y)
		
		try:
	
			Y = np.log(y)
			X = np.log(x)
			p = np.polyfit(X,Y,1)
			N = p[1]
			a = np.exp(N)
			b = p[0]
			cc = np.corrcoef(X,Y)
			r = cc[0,1]
			f = 'y = '+ str(round(a,2))+' * x^' + str(round(b,2))
					
			plt.close()				
			plt.plot(x, y, '^k', label='Original data', markersize=2)
			plt.plot(x, a*(x**b), '--g', label='Fitted line - Regression puissance')
			plt.title('Regression puissance y = ax^b',fontsize=5)
			plt.xlabel(x_name,fontsize=5)
			plt.ylabel(y_name,fontsize=5)
			plt.legend(fontsize=5)
			
			if show == True:
				
				try:
					
					plt.show()
					
				except:
					
					pass
				
			
			return attrdict.AttrDict({"a":a, "b":b, "r":r, "equation":f, "graph":plt})
	
		except:
			
			return None
	
	
	
	
	
	
	
	
	def reg(self, X, Y, show=True):

		"""

		Teste une régréssion puissance.

		Arguments:

			x: nom [str] ou index [int] de colonne
			y: nom [str] ou index [int] de colonne
			show: [bool] , défaut=True, Si True, le graphique avec la droite de regression est affiché

		Return:

			AttrDict {'plot', 'lin', 'exp', 'pwr', 'plt'}

		"""
		
		
		
		x_name, y_name, x, y = self.selection(X, Y)
		
		if 0 in x or 0 in y:
			
			return self.lin(X, Y)
		
		
		
		lin = self.lin(X, Y,show=False)
		
		exp = self.exp(X, Y,show=False)
		
		pwr = self.pwr(X, Y,show=False)
		
		
		
		# affichage graphique
		
		plt.close()
		plt.figure(1)
		
		g1 = plt.subplot(2,2,1)
		plt.plot(x, y, '^k', label='Original data', markersize=2)
		plt.title('Nuage de point', fontsize=5)
		plt.xlabel(x_name,fontsize=5)
		plt.ylabel(y_name,fontsize=5)
		plt.legend(fontsize=5)
		
		g2 = plt.subplot(2,2,2)
		plt.plot(x, y, '^k', label='Original data', markersize=2)
		plt.plot(x, [lin.a*i+lin.b for i in x], '--b', label='Fitted line - linear regression')
		plt.title('Regression lineaire y = ax + b',fontsize=5)
		plt.xlabel(x_name,fontsize=5)
		plt.ylabel(y_name,fontsize=5)
		plt.legend(fontsize=5)
		
		g3 = plt.subplot(2,2,3)
		plt.plot(x, y, '^k', label='Original data', markersize=2)
		plt.plot(x, [exp.a*np.exp(exp.b*i) for i in x], '--r', label='Fitted line - Exponential regression')
		plt.title('Regression Exponentielle y = a.exp(bx)', fontsize=5)
		plt.xlabel(x_name,fontsize=5)
		plt.ylabel(y_name,fontsize=5)
		plt.legend(fontsize=5)
		
		g4 = plt.subplot(2,2,4)
		plt.plot(x, y, '^k', label='Original data', markersize=2)
		plt.plot(x, pwr.a*(x**pwr.b), '--g', label='Fitted line - Regression puissance')
		plt.title('Regression puissance y = ax^b',fontsize=5)
		plt.xlabel(x_name,fontsize=5)
		plt.ylabel(y_name,fontsize=5)
		plt.legend(fontsize=5)
		
		if show == True:
		
			plt.tight_layout() # Or equivalently,  "plt.tight_layout()"
			plt.show()
		
		lin.graph = g2
		exp.graph = g3
		pwr.graph = g4
			
		return attrdict.AttrDict({"plot":g1, "lin":lin, "exp":exp, "pwr":pwr, "plt":plt})
