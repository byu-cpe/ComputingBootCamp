FASM2BELS_PATH=~/symbiflow-xc-fasm2bels
FASM2BELS_PATH_PY=$(FASM2BELS_PATH)/env/bin/python3
XRAY_PATH=$(FASM2BELS_PATH)/third_party/prjxray
XRAY_DB_PATH=$(FASM2BELS_PATH)/third_party/prjxray-db
DB_ROOT=$(XRAY_DB_PATH)/artix7
PART=xc7a200tsbg484-1

# You need to add the XRAY binaries to your PATH 
# (this is needed by bit2fasm)
export PATH := $(XRAY_PATH)/build/tools:$(PATH)

BIT_FILE = add16.bit
FASM_FILE = add16.fasm
REVERSED_VERILOG_FILE = add16_reversed.v
CONSTRAINTS_FILE = constraints.xdc

all: $(REVERSED_VERILOG_FILE)
 
clean:
	rm -rf $(FASM_FILE) $(REVERSED_VERILOG_FILE)

fasm2verilog: $(REVERSED_VERILOG_FILE)

bit2fasm: $(FASM_FILE)

# This is how you convert a .bit file to a fasm file.  
# Note that it is running the python from within the fasm2bels virtual environment.
$(FASM_FILE): $(BIT_FILE)
	$(FASM2BELS_PATH_PY) $(XRAY_PATH)/utils/bit2fasm.py --db-root $(DB_ROOT) --part $(PART) $< > $@

# This is how you convert a fasm file to a Verilog netlist
# Note that it is running the python from within the fasm2bels virtual environment, and calling the fasm2bels python package (-mfasm2bels)
#
#	The fasm file and constraints file are provided as inputs
#	A verilog netlist is produced, along with an XDC output.
$(REVERSED_VERILOG_FILE): $(FASM_FILE) $(CONSTRAINTS_FILE)
	$(FASM2BELS_PATH_PY) -mfasm2bels --connection_database $(PART)_db --db_root $(DB_ROOT) --part $(PART) --fasm_file $< --verilog_file $@ --xdc_file output.xdc --input_xdc constraints.xdc
