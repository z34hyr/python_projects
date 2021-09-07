#!/usr/bin/python3

import xlrd
from modules import *
#import os
KNOWN_EXCH_TEMPL = [owen_mv_16_exch, owen_mv_32_exch, owen_mu_16_exch]
KNOWN_MODULES = {"МВ110-32ДН" : ["МВ110-32ДН", "D_IN", 32, owen_mv_32_exch],
					"МВ110-16ДН" : ["МВ110-16ДН", "D_IN", 16, owen_mv_16_exch],
					"МУ110-32Р" : ["МУ110-32ДН", "D_OUT", 32],
					"МУ110-16Р" : ["МУ110-16Р", "D_OUT", 16, owen_mu_16_exch],
					"МВ110-8А" : ["МВ110-8А", "A_IN", 8],
					}



class Base_module():
	def __init__(self, params : list): #(str, str, int)
		self.name = params[0]
		self.type = params[1]
		print(self.type)
		self.n_channels = params[2]
		self.correlation = []
		#self.known_gen_type = [self.generate_corr_str_bool, self.generate_corr_str_word]

	

	def generate_corr_str_word(self, data_word : int, node_corr : list) ->str :
		"""Генерирует строку корреляции для LW температуры"""
		templ = f"""//	{self.name} связь канала {node_corr[0]} и LW {50 + node_corr[2]}
GetData(node, "Local HMI", LW, {data_word + node_corr[2]}, 1)
SetData(node, "Local HMI", LW, {50 + node_corr[2]}, 1)
"""
		return templ

	def generate_corr_str_bool(self, data_word : int, node_corr : list) -> str:
		"""Генерирует 2 строки для корреляции LW_Bit
		и номера в карте битов адресов weintek (ID ванны)
		word - номер LW модуля
		node_corr - list с параметрами коррелияции ноды
		node_corr[0] - порядковый номер входа\выхода модуля
		node_corr[1] - имя ванны
		node_corr[2] - ID ванны в панели Weintek
		node_corr[3] - нагрев или охлаждение. Опционально, только для МУ
		"""
		start_LB = 0
		if self.type == "D_IN":
			start_LB = 50
		elif self.type == "D_OUT":
			if node_corr[3] == "N":
				start_LB = 51
			else:
				start_LB = 53
		templ = f"""//	{self.name} связь канала {node_corr[0]} и LB {start_LB + node_corr[2] * 16}
GetData(node, "Local HMI", LW_Bit, {data_word + node_corr[0] // 16}{(node_corr[0] + node_corr[0] // 16):02}, 1)
SetData(node, "Local HMI", LB, {start_LB + node_corr[2] * 16})
"""
		
		return templ

	def generate_corr(self, data_word : int, node_corr : list) -> str:
		if self.type != "A_IN":
			return self.generate_corr_str_bool(data_word, node_corr)
		else:
			return self.generate_corr_str_word(data_word, node_corr)

	def generate_exch_str(self):
		pass

	def show_module_info(self):
		s = f"""===============================
	Модуль {self.name}, {self.n_channels} канала(ов), тип - {self.type}
{self.correlation}"""
		return s

def read_map(map_path = "", map_name = "/home/zephyr/Desktop/map.xls") -> list:
	try:
		book = xlrd.open_workbook(filename=map_name)
		print("Xls opened successfully")
		print(f"Worksheet(s): {book.nsheets}")
		sheet = book.sheet_by_index(0)
		print(f"Sheet name: {sheet.name}")
		table_len = len(sheet.col(0))
		modules_list = []
		#print(table_len)
		i = 0
		while i < table_len:
			cell_val = sheet.cell_value(rowx=i, colx=0)
			if cell_val in KNOWN_MODULES:
				#print(f"FOUND MODULE {cell_val}")
				new_mod = None
				data_list = []
				for j in range(i + 1, table_len):
					i = j
					subc = sheet.row(j)
					if subc[0].value in KNOWN_MODULES:
						break
					elif subc[0].value == "":
						#print("skip empty cell")
						continue
					elif subc[2].value == "":
						#print("skip channel with no specified ID")
						continue
					elif KNOWN_MODULES[cell_val][1] == "D_OUT" and subc[3].value == "" and subc[4].value == "":
						#print("skip channel with no specified output type")
						continue
					curr_row = []
					curr_row.append(int(subc[0].value))
					curr_row.append(str(subc[1].value))
					curr_row.append(int(subc[2].value))
					if new_mod == None:
						new_mod = Base_module(KNOWN_MODULES[cell_val])
					if KNOWN_MODULES[cell_val][1] == "D_OUT":
						if subc[3].value != "":
							curr_row.append("N")
						elif subc[4].value != "":
							curr_row.append("O")
					data_list.append(curr_row)
				if new_mod != None:
					if len(data_list):
						new_mod.correlation = data_list
					modules_list.append(new_mod)
			else:
				#print("SKIP")
				i += 1
				continue
		return modules_list
	except Exception as x:
		print(x)

if __name__ == "__main__":
	m_l = read_map()
	for i in m_l:
		print(i.show_module_info())
	for i in m_l:
		for j in i.correlation:
			print(i.generate_corr(10, j))
	#print(owen_mv_16_exch(1, 100, 10))
	#print(owen_mv_32_exch(1, 100, 10))