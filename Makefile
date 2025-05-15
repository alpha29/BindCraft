default:
	@echo "Makefile for BindCraft; please specify a target."

set-perms:
	@echo "Setting permissions for all files in the current directory..."
	chmod +x ./functions/dssp
	chmod +x ./functions/DAlphaBall.gcc
	@echo "Done."

setup-pyrosetta:
	@echo "Setting up PyRosetta..."
	#python -c "import pyrosettacolabsetup; pyrosettacolabsetup.install_pyrosetta(serialization=True, cache_wheel_on_google_drive=False)"
	#python -c "import pyrosetta_installer; pyrosetta_installer.install_pyrosetta()"
	@echo "Look, neither of these functions work right.  Instead, we specify the wheel URL in pyproject.toml, even though this will break on other platforms."
	@echo "Done."

download-af2-weights:
	@echo "Downloading AlphaFold2 weights..."
	mkdir -p ./params
	aria2c -x 16 https://storage.googleapis.com/alphafold/alphafold_params_2022-12-06.tar
	tar -xf alphafold_params_2022-12-06.tar -C ./params
	@echo "Done."
