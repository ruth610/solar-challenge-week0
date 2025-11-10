# Solar Challenge Week 0

This repository contains the Solar Challenge Week 0 project.  
Follow the steps below to reproduce the environment using **Conda**.

---

## Environment Setup (Conda)

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

# 2. Create a conda environment with Python 3.11
conda create --yes --name solar-env python=3.11

# 3. Activate the environment
conda activate solar-env

# 4. Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# 5. (Optional) Install common packages if requirements.txt doesn't exist
pip install requests flask pytest

# 6. Freeze installed packages into requirements.txt
pip freeze > requirements.txt

# 7. Verify the environment
python --version        # should report Python 3.11.x
pip --version
pip list                # lists installed packages

# 8. Run the project (replace main.py if your entry point differs)
python main.py

# 9. Run tests
pytest -v

# 10. Deactivate the environment when done
conda deactivate

