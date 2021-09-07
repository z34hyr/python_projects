

def macro_template():
	begin = """macro_command main()
bool errors // слово с ошибками по модулю
unsigned short error
unsigned short vhodi, vhodi1, vhodi2, vihod1, vihod2, vihod3
unsigned short vhod_pH[2], vhod_an
"""
	end = "end macro_command"
	return [begin, end]

def owen_mv_16_exch(addr : int, word : int, err_word : int, mbrtu_name = "MODBUS RTU (Zero-based Addressing)") -> list :
	err_word += addr // 16
	s = f"""//==================================
//МВ110-16ДН | адрес {addr}
GetDataEx(vhodi, {mbrtu_name}, 3x, {addr}#51, 1)
GetError(error)
if error <> 0 then
	errors = true
else
	errors = false
end if
SetData(errors, "Local HMI", LW_Bit, {err_word}{addr // 16}, 1)
SetData(vhodi, "Local HMI", LW, {word}, 1)
"""
	return [s, 1]

def owen_mv_32_exch(addr : int, word : int, err_word : int, mbrtu_name = "MODBUS RTU (Zero-based Addressing)") -> list :
	err_word += addr // 16
	s = f"""//==================================
//МВ110-32ДН | адрес {addr}
GetDataEx(vhodi1, {mbrtu_name}, 3x, {addr}#99, 1)
GetDataEx(vhodi2, {mbrtu_name}, 3x, {addr}#100, 1)
GetError(error)
if error <> 0 then
	errors = true
else
	errors = false
end if
SetData(errors, "Local HMI", LW_Bit, {err_word}{addr // 16}, 1)

SetData(vhodi2, "Local HMI", LW, {word}, 1) // выходы с 1 по 16
SetData(vhodi1, "Local HMI", LW, {word + 1}, 1) // входы с 17 по 32
"""
	return [s, 2]

def owen_mu_16_exch(addr : int, word : int, err_word : int, mbrtu_name = "MODBUS RTU (Zero-based Addressing)") -> list :
	err_word += addr // 16
	s = f"""//==================================
// МУ110-16Р | адрес {addr}
GetData(vihod1, "Local HMI", LW, 20, 1)
SetDataEx(vihod1, {mbrtu_name}, 4x, {addr}#50, 1)
GetError(error)
if error <> 0 then
	errors = true
else
	errors = false
end if
SetData(errors, "Local HMI", LW_Bit, {err_word}{addr // 16}, 1)
"""
	return [s, 1]
